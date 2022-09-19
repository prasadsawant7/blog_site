import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''
create table bs_post(
	postId bigint identity(1,1) not null primary key,
	authorId bigint not null foreign key references bs_user(userId),
	title varchar(100) not null,
	content text null default null,
	createdAt datetime not null,
	updatedAt datetime not null,
	publishedAt datetime not null
);
''')

conn.commit()

conn.close()