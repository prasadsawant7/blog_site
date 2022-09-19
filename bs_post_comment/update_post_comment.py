import pyodbc
import datetime

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postCommentId = 3
comment = "Nicely Explained, more content needed."
commentedAt = str(datetime.datetime.now())[:19+4]

sql = f"""update bs_post_comment set comment = '{comment}', commentedAt = '{commentedAt}' where postCommentId = '{postCommentId}';"""

cur.execute(sql)

conn.commit()
conn.close()