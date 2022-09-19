import pyodbc
# from tabulate import tabulate

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''select * from bs_post_comment;''')

for row in cur:
    print(row)

# post_comments = []
# for post_comment in cur:
#     post_comments.append(list(post_comment))

# columns = ["postCommentId", "postId", "commentedBy", "comment", "commentedAt"]
# print(tabulate(post_comments, headers=columns, tablefmt="grid"))

conn.commit()
conn.close()