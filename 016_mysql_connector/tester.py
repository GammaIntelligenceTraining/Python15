import mysql.connector
import os

conn = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    username='root',
    password=os.environ.get('database_password'),
    # database='python15'
    database='sakila'
)

mycursor = conn.cursor()
# print(mycursor)
# mycursor.execute('CREATE TABLE student (name VARCHAR(255), age INTEGER(2));')

# user = ('Bob', 30)
# sql_formula = f'INSERT INTO student (name, age) VALUES ("{user[0]}", {user[1]})'
# mycursor.execute(sql_formula)
#
# user = ('Mary', 18)
# sql_formula = f'INSERT INTO student (name, age) VALUES ("{user[0]}", {user[1]})'
# mycursor.execute(sql_formula)

# sql_formula = 'INSERT INTO student (name, age) VALUES (%s, %s)'
# # user = ('Sarah', 27)
# # mycursor.execute(sql_formula, user)
# users = [('Jonny', 32), ('Max', 15), ('Samantha', 26)]
# mycursor.executemany(sql_formula, users)
# conn.commit()

mycursor.execute('SELECT * FROM actor;')


result = mycursor.fetchmany(5)
print(result)