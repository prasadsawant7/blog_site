import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''
create table bs_post_tag(
	postId bigint not null foreign key references bs_post(postId),
	tagId bigint not null foreign key references bs_tag(tagId)
);
''')

conn.commit()

conn.close()