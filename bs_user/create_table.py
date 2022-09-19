import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('''
create table bs_user(
	userId bigint identity(1,1) not null primary key,
	firstName varchar(20) default null,
	lastName varchar(20) default null,
	email varchar(50) not null unique,
	username varchar(20) not null unique,
	salt varchar(15) not null unique,
	passwdHash text not null,
	registered_at datetime not null,
	last_login datetime not null,
	bio text default null,
	country varchar(30) default null
);
''')

conn.commit()

conn.close()