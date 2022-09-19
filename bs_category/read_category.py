import pyodbc
# from tabulate import tabulate

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''select * from bs_category;''')

for row in cur:
    print(row)

# categories = []
# for category in cur:
#     categories.append(list(category))

# columns = ["categoryId", "category", "categoryDescription"]
# print(tabulate(categories, headers=columns, tablefmt="grid"))

conn.commit()
conn.close()