create database company;
use company;
create table regions(region_id int(10) primary key,region_name varchar(20));
create table countries(country_id int(10),country_name varchar(20),region_id int,primary key(country_id),foreign key(region_id) references regions(region_id));
create table locations(location_id int(10),street_address varchar(50),postal_code int(10),city varchar(20),state_province varchar(20),country_id int,primary key(location_id),foreign key(country_id) references countries(country_id));
create table departments(department_id int(10),department_name varchar(20),location_id int,primary key(department_id),foreign key(location_id) references locations(location_id));
create table jobs(job_id int(10) primary key,job_title varchar(20),min_salary int(10),max_salary int(10));
create table employees(employee_id int(10) primary key,first_name varchar(20),last_name varchar(20),email varchar(30),phone_number int(10),hire_date date,job_id int,foreign key(job_id) references jobs(job_id),salary int(10),manager_id int,foreign key(manager_id) references employees(employee_id),department_id int,foreign key(department_id) references departments(department_id));
create table dependents(dependent_id int(10) primary key,first_name varchar(20),last_name varchar(20),relationship varchar(20),employee_id int,foreign key(employee_id) references employees(employee_id));
alter  table employees modify manager_id int default null;

