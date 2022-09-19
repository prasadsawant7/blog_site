create database blog_site;

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

create table bs_post(
	postId bigint identity(1,1) not null primary key,
	authorId bigint not null foreign key references bs_user(userId),
	title varchar(100) not null,
	content text null default null,
	createdAt datetime not null,
	updatedAt datetime not null,
	publishedAt datetime not null
);

create table bs_post_comment(
	postCommentId bigint identity(1,1) not null primary key,
	postId bigint not null foreign key references bs_post(postId),
	commentedBy varchar(30) not null,
	comment text not null,
	commentedAt datetime not null,
);

create table bs_tag(
	tagId bigint identity(1,1) not null primary key,
	tag varchar(20) not null unique,
	tagDescription text null default null
);

create table bs_post_tag(
	postId bigint not null foreign key references bs_post(postId),
	tagId bigint not null foreign key references bs_tag(tagId)
);

create table bs_category(
	categoryId bigint identity(1,1) not null primary key,
	category varchar(20) not null unique,
	categoryDescription text null default null
);

create table bs_post_category(
	postId bigint not null foreign key references bs_post(postId),
	categoryId bigint not null foreign key references bs_category(categoryId)
);

drop table bs_post_comment;
drop table bs_post_tag;
drop table bs_tag;
drop table bs_post_category;
drop table bs_category;
drop table bs_post;
drop table bs_user;

select * from bs_user;
select * from bs_post_comment;
select * from bs_post_tag;
select * from bs_tag;
select * from bs_post;
select * from bs_post_category;
select * from bs_category;