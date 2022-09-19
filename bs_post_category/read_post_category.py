import pyodbc
# from tabulate import tabulate

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''select * from bs_post_category;''')

for row in cur:
    print(row)

# post_categories = []
# for post_category in cur:
#     post_categories.append(list(post_category))

# columns = ["postId", "categoryId"]
# print(tabulate(post_categories, headers=columns, tablefmt="grid"))

conn.commit()
conn.close()