use company;
alter table departments rename to dept;
alter table employees modify salary smallint;
alter table employees add Commission int(10);
select * from dept;
desc employees;