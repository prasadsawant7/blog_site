import pyodbc
# from tabulate import tabulate

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''select * from bs_tag;''')

for row in cur:
    print(row)

# tags = []
# for tag in cur:
#     tags.append(list(tag))

# columns = ["tagId", "tag", "tagDescription"]
# print(tabulate(tags, headers=columns, tablefmt="grid"))

conn.commit()
conn.close()