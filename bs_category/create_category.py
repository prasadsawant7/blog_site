import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

category = "Frontend"
categoryDescription = "Frontend topics"

sql = f"""insert into bs_category(
category,
categoryDescription
) 
values
(
'{category}',
'{categoryDescription}'
);
"""

cur.execute(sql)

conn.commit()
conn.close()