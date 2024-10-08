from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import hashlib

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=10)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/flask_python15'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    _id = db.Column('user_id', db.Integer, primary_key=True)
    login = db.Column('login', db.String(20), unique=True)
    password = db.Column('password', db.String(32))
    email = db.Column('email', db.String(100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email


@app.route('/')
def home():
    return render_template(
        'index.html',
    )


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_name = request.form['user-name']
        user_pass = hashlib.md5(request.form['user-pass'].encode()).hexdigest()
        user_in_db = User.query.filter_by(login=user_name).first()
        if user_in_db:
            if user_pass == user_in_db.password:
                session['login'] = user_name
                session['email'] = user_in_db.email
                flash('Logged in successfully.', 'success')
                return redirect(url_for('user_profile'))
            else:
                flash('Wrong password.', 'danger')
                return redirect(url_for('login'))
        else:
            new_user = User(user_name, user_pass, '')
            db.session.add(new_user)
            db.session.commit()
            session['login'] = user_name
            session['email'] = ''
            flash('User account is created.', 'success')
            return redirect(url_for('user_profile'))
    else:
        if 'login' in session:
            flash('You are already logged in.', 'info')
            return redirect(url_for('user_profile'))
        return render_template('login.html')


@app.route('/user_profile/', methods=['GET', 'POST'])
def user_profile():
    if 'login' in session:
        if request.method == 'POST':
            user_email = request.form['user-email']
            user_in_db = User.query.filter_by(login=session['login']).first()
            user_in_db.email = user_email
            db.session.commit()
            session['email'] = user_email
            flash('Email was saved.', 'success')
        return render_template('user.html', login=session['login'], email=session['email'])
    else:
        flash('Please log in.', 'info')
        return redirect(url_for('login'))


@app.route('/admin/')
def admin():
    return redirect(url_for('home'))


@app.route('/logout/')
def logout():
    session.pop('login', None)
    session.pop('email', None)
    flash('Logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/delete_user/')
def delete_user():
    User.query.filter_by(login=session['login']).delete()
    db.session.commit()
    session.pop('login', None)
    session.pop('email', None)
    flash('User was deleted', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
