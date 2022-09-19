import pyodbc
import datetime

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postId = 1
commentedBy = "David Malan"
comment = "Make more blogs on this topic."
commentedAt = str(datetime.datetime.now())[:19+4]

sql = f"""insert into bs_post_comment(
postId,
commentedBy,
comment,
commentedAt
) 
values
(
'{postId}',
'{commentedBy}',
'{comment}',
'{commentedAt}'
);
"""

cur.execute(sql)

conn.commit()
conn.close()