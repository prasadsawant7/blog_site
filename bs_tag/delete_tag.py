import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

tagId = 4

sql = f"""delete from bs_tag where tagId = '{tagId}';"""

cur.execute(sql)

conn.commit()
conn.close()