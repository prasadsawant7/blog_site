import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

username = "john9097283"

sql = f"""delete from bs_user where username = '{username}';"""

cur.execute(sql)

conn.commit()
conn.close()