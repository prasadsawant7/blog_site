import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

tag = "Redis"
tagDescription = "Caching Database"

sql = f"""insert into bs_tag(
tag,
tagDescription
) 
values
(
'{tag}',
'{tagDescription}'
);
"""

cur.execute(sql)

conn.commit()
conn.close()