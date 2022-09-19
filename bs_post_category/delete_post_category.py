import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postId = 3
categoryId = 7

sql = f"""delete from bs_post_category where postId = {postId} and categoryId = {categoryId};"""

cur.execute(sql)

conn.commit()
conn.close()