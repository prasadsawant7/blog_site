import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

tagId = 6
tag = "Neo4j"
tagDescription = "Graph Database"

sql = f"""update bs_tag set tag = '{tag}', tagDescription = '{tagDescription}' where tagId = '{tagId}';"""

cur.execute(sql)

conn.commit()
conn.close()