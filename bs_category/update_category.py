from unicodedata import category
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

categoryId = 5
category = "Cloud Computing"
categoryDescription = "Cloud computing is the on-demand availability of computer system resources."

sql = f"""update bs_category set category = '{category}', categoryDescription = '{categoryDescription}' where categoryId = {categoryId};"""

cur.execute(sql)

conn.commit()
conn.close()