import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postCommentId = 1

sql = f"""delete from bs_post_comment where postCommentId = '{postCommentId}';"""

cur.execute(sql)

conn.commit()
conn.close()