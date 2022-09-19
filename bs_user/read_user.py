import pyodbc
# from tabulate import tabulate

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''select * from bs_user;''')

for row in cur:
    print(row)

# users = []
# for user in cur:
#     users.append(list(user))

# columns = ["userId", "firstName", "lastName", "email", "username", "salt", "passwdHash", "registered_at", "last_login", "bio", "country"]
# print(tabulate(users, headers=columns, tablefmt="grid"))

conn.commit()
conn.close()