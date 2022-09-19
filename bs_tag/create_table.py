import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''
create table bs_tag(
	tagId bigint identity(1,1) not null primary key,
	tag varchar(20) not null unique,
	tagDescription text null default null
);
''')

conn.commit()

conn.close()