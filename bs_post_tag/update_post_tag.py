import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postId = 1
previousTagId = 1
newTagId = 3

sql = f"""update bs_post_tag set tagId = {newTagId} where postId = {postId} and tagId = '{previousTagId}';"""

cur.execute(sql)

conn.commit()
conn.close()