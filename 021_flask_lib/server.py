from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(seconds=10)


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
        user_pass = request.form['user-pass']
        session['login'] = user_name
        return redirect(url_for('user', name=user_name))
    else:
        if 'login' in session:
            return redirect(url_for('user', name=session['login']))
        return render_template('login.html')


@app.route('/<name>/')
def user(name):
    return f'Hello {name}'


@app.route('/admin/')
def admin():
    return redirect(url_for('home'))


@app.route('/logout/')
def logout():
    session.pop('login', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
