import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postId = 3
tagId = 6

sql = f"""delete from bs_post_tag where postId = {postId} and tagId = {tagId};"""

cur.execute(sql)

conn.commit()
conn.close()