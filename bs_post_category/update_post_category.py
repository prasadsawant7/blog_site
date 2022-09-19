import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postId = 3
previousCategoryId = 6
newCategoryId = 5

sql = f"""update bs_post_category set categoryId = {newCategoryId} where postId = {postId} and categoryId = '{previousCategoryId}';"""

cur.execute(sql)

conn.commit()
conn.close()