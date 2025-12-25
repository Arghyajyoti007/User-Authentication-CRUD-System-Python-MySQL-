-- It will show all the databases present in your system
show databases;

-- If the Database with same name already exists
DROP DATABASE login_page_curd;

-- To Create the new Database 
create database login_page_curd;

-- To use the Database that we had created
use login_page_curd;

-- If the Table with same name already exists
drop table cust_login_details; 

-- Create the main table 
create table cust_login_details (
	cust_id int auto_increment not null primary key ,
	cust_full_name text,
	cust_address text,
	cust_phone_number varchar(10) unique,
	cust_username varchar(50) unique,
	cust_password varchar(50),
    create_time timestamp default current_timestamp
);

-- Test the table
select * from cust_login_details;
