import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

categoryId = 4

sql = f"""delete from bs_category where categoryId = {categoryId};"""

cur.execute(sql)

conn.commit()
conn.close()