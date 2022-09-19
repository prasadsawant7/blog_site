import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postId = 1
categoryId = 3

sql = f"""insert into bs_post_category(
postId,
categoryId
) 
values
(
{postId},
{categoryId}
);
"""

cur.execute(sql)

conn.commit()
conn.close()