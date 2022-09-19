import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''
create table bs_post_category(
	postId bigint not null foreign key references bs_post(postId),
	categoryId bigint not null foreign key references bs_category(categoryId)
);
''')

conn.commit()

conn.close()