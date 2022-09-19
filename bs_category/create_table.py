import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''
create table bs_category(
	categoryId bigint identity(1,1) not null primary key,
	category varchar(20) not null unique,
	categoryDescription text null default null
);
''')

conn.commit()

conn.close()