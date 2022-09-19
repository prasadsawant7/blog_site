import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

postId = 2

sql = f"""delete from bs_post where postId = '{postId}';"""

cur.execute(sql)

conn.commit()
conn.close()