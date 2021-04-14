import MySQLdb


db = MySQLdb.connect(host='localhost',user='temp',passwd='password',database='library_management')

cursor = db.cursor()
# cursor.execute('create database library_management;')


create_table = """
CREATE TABLE `book` (
  `book_id` int not null auto_increment,
  `book_name` varchar(80) not null,
  `book_description` varchar(200),
  `book_code` varchar(50),
  `book_category` varchar(50),
  `book_author` varchar(50),
  `book_publisher` varchar(50),
  `book_price` varchar(50),
  PRIMARY KEY (`book_id`)
);

CREATE TABLE `users` (
  `user_id` int not null auto_increment,
  `user_name` varchar(80) not null,
  `email` varchar(50),
  `password` varchar(50),
  PRIMARY KEY (`user_id`)
);

CREATE TABLE `daily_operations` (
  `id` int not null auto_increment,
  `book_name` varchar(80) not null,
  `type` varchar(50),
  `days` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `categories` (
  `category_id` int not null auto_increment,
  `category_name` varchar(80) not null,
  PRIMARY KEY (`category_id`)
);

CREATE TABLE `authors` (
  `authors_id` int not null auto_increment,
  `author_name` varchar(80) not null,
  PRIMARY KEY (`authors_id`)
);

CREATE TABLE `publishers` (
  `publisher_id` int not null auto_increment,
  `publisher_name` varchar(80) not null,
  PRIMARY KEY (`publisher_id`)
);


"""
cursor.execute(create_table)
cursor.close()