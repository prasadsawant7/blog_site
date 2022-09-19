import pyodbc
# from tabulate import tabulate

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''select * from bs_post_tag;''')

for row in cur:
    print(row)

# post_tags = []
# for post_tag in cur:
#     post_tags.append(list(post_tag))

# columns = ["postId", "tagId"]
# print(tabulate(post_tags, headers=columns, tablefmt="grid"))

conn.commit()
conn.close()