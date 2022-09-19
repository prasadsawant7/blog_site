import pyodbc
# from tabulate import tabulate

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''select * from bs_post;''')

for row in cur:
    print(row)

# posts = []
# for post in cur:
#     posts.append(list(post))

# columns = ["postId", "authorId", "title", "content", "createdAt", "updatedAt", "publishedAt"]
# print(tabulate(posts, headers=columns, tablefmt="grid"))

conn.commit()
conn.close()