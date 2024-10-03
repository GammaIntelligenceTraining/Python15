import pandas as pd
# import json
#
# with open('json_files/sample2.json', 'r') as file:
#     data = json.load(file)
#
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('csv_files/2019.csv', skiprows=1)

# df = pd.read_csv('csv_files/2019.csv', header=1)

# df = pd.read_csv('csv_files/2019.csv', header=None)

# df = pd.read_csv('csv_files/test.csv', header=None, names=['Name', 'Date of birth', 'Hometown'])

# df = pd.read_csv('csv_files/2019.csv', nrows=5)
#
# df.to_csv('csv_files/2019_copy.csv', index=False, header=False)

# df = pd.read_csv('csv_files/2019.csv')
# pd.set_option('display.max_columns', 9)
# pd.set_option('display.max_rows', 160)

# print(df.head(3))
# print(df.tail(2))

# print(df['Country or region'][140])
# print(df[['Country or region', 'GDP per capita']])
#
# for line in df['Country or region']:
#     print(line)

# print(df.iloc[0])
# print(df.iloc[40:50])
# print(df.iloc[[53, 48, 104]])
# print(df.iloc[[45, 23, 140], [1, 3, 7]])

# print(df.loc[[1, 5, 6, 123], ['Country or region', 'Generosity']])

# print(df.loc[[1, 5, 6, 123], 'Country or region':'Generosity'])

# print(df.shape)

# print(df['Country or region'].value_counts())

# import mysql.connector
#
# conn = mysql.connector.connect(
#     user='root',
#     password='12345678',
#     host='localhost',
#     database='sakila'
# )

# df = pd.read_sql_query('SHOW TABLES FROM sakila', conn)

# df = pd.read_sql_query('''SELECT actor.first_name, actor.last_name, film.title
#                        FROM actor
#                        JOIN film_actor ON actor.actor_id = film_actor.actor_id
#                        JOIN film ON film.film_id = film_actor.film_id
#                        ;''', conn)
#

df = pd.read_csv('csv_files/2019.csv')

# print(df.describe())
# print(df.memory_usage(deep=True))
# print(df.dtypes)

# print(df.loc[df['Country or region'] == 'Estonia'])
# print(df.loc[df['GDP per capita'] > 1])
# print(df.loc[df['Country or region'].isin(['Estonia', 'Latvia', 'Lithuania'])])

# print(df.sort_values(['Country or region', 'Perceptions of corruption'], ascending=[True, False]))

# df['Total'] = df['GDP per capita'] + df['Generosity'] + df['Perceptions of corruption']
# df.insert(loc=8, column='New column', value=df['GDP per capita'] ** 2)
# df = df.drop(columns=['New column', 'Perceptions of corruption'])
pd.set_option('display.max_columns', 10)
# print(df.loc[df['Country or region'].str.contains('on|an')])
# print(df.loc[df['GDP per capita'] > 1, ['Country or region', 'GDP per capita']])
# print(df.groupby('Country or region').count())
# print(df)

# print(df.groupby('GDP per capita').sum())

df1 = df.nlargest(5, 'GDP per capita')
df2 = df.nsmallest(5, 'GDP per capita')
# print(df1)
# print(df2)
df3 = pd.read_csv('csv_files/test.csv', header=None, names=['Name', 'DOB', 'Town'])
print(pd.concat([df1, df2, df3]))
