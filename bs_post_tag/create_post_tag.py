import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postId = 3
tagId = 6

sql = f"""insert into bs_post_tag(
postId,
tagId
) 
values
(
{postId},
{tagId}
);
"""

cur.execute(sql)

conn.commit()
conn.close()