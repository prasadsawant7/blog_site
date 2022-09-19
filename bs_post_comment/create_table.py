import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''
create table bs_post_comment(
	postCommentId bigint identity(1,1) not null primary key,
	postId bigint not null foreign key references bs_post(postId),
	commentedBy varchar(30) not null,
	comment text not null,
	commentedAt datetime not null,
);
''')

conn.commit()

conn.close()