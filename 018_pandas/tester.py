import pandas as pd

df = pd.read_csv('csv_files/2019.csv')
# df = pd.read_csv('csv_files/test.csv', header=None, names=['Name', 'Date of birth', 'Town'])
pd.set_option('display.max_columns', 9)
# pd.set_option('display.max_rows', 160)
#
# print(df.head(10))
# print(df.tail(10))

# df.to_csv('csv_files/new.csv', index=False, header=None)
# df.to_csv('csv_files/new.csv', index_label='Index')
# df.to_csv('csv_files/new.csv', columns=['Town', 'Name'])

# print(df.columns)
# print(type(df.columns))

# people = {
#     "first": ['Bob', 'Alex', 'John', 'Mary'],
#     "last": ['Smith', 'Green', 'Black', 'Gold'],
#     "email": ['bob@example.com', 'alex@example.com', "john@example.com", 'mary@example.com']
# }
# # print(people['email'])
#
# # Converting python dictionary to data frame
# df = pd.DataFrame(people)
# print(df)

# for country in df['Country or region']:
#     print(country)

# print(df['Country or region'][45:55])
# print(df[['Country or region', 'Score']])
# print(df[45:55])

# print(df.iloc[[34, 42, 54]])
# print(df.iloc[45:55, [1, 4, 6]])

# print(df.loc[45:54, ['Country or region', 'Social support']])

# print(df.shape)
# print(df['Country or region'].value_counts())

# import mysql.connector
#
# conn = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     port=3306,
#     password='12345678',
#     database='sakila'
# )
#
# df = pd.read_sql_query('SELECT * FROM actor', conn)
# print(df)


# for index, row in df.iterrows():
#     print(index, type(row))

# print(df.loc[df['Country or region'] == 'Estonia'])
# print(df.loc[df['Score'] > 5])

# print(df.describe())
# print(df.dtypes)
# print(df.memory_usage(deep=True))

# print(df.sort_values(['Country or region', 'Perceptions of corruption'], ascending=[True, False]))

# df['Total'] = df['Perceptions of corruption'] * 2 + df['Score']
# df.insert(loc=3, column='New', value=(df['Score'] ** 2))
# df = df.drop(columns=['New'])
# print(df)
# print(df.groupby('Country or region').min()['Social support'])
# print(df.loc[df['Country or region'].str.contains('on|an')])
# print(df.loc[df['Country or region'].str.endswith('land')])

print(df.nlargest(10, 'GDP per capita'))
print(df.nsmallest(10, 'GDP per capita').reset_index(drop=True))

print(pd.concat([df.nlargest(10, 'GDP per capita'), df.nsmallest(10, 'GDP per capita').reset_index(drop=True)]))