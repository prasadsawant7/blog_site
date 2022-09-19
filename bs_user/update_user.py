import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

username = "john9097283"
bio = "Johnny The Reaper"

sql = f"""update bs_user set bio = '{bio}' where username = '{username}';"""

cur.execute(sql)

conn.commit()
conn.close()