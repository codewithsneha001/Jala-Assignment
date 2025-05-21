create database JalaSQL;
use JalaSQL;
create table salespeople
(snum int primary Key,
sname varchar(255),
city varchar(255),
comm decimal(4,2)
);
select * from salespeople;
insert into salespeople (snum, sname, city, comm) VALUES (1001, 'Peel', 'London', 0.12);
insert into salespeople (snum, sname, city, comm) VALUES (1002, 'Serres', 'San Jose', 0.13);
insert into salespeople (snum, sname, city, comm) VALUES (1004, 'Motika', 'London', 0.11);
insert into salespeople (snum, sname, city, comm) VALUES (1007, 'Rafkin', 'Barcelona', 0.15);
insert into salespeople (snum, sname, city, comm) VALUES (1003, 'Axelrod', 'New york', 0.10);
create table cust(
cnum int primary key,
cname varchar(255),
city varchar(255),
rating int,
snum int,
FOREIGN KEY (snum) REFERENCES salespeople(snum)
);
INSERT INTO cust (cnum, cname, city, rating, snum) VALUES (2001, 'Hoffman', 'London', 100, 1001);
INSERT INTO cust (cnum, cname, city, rating, snum) VALUES (2002, 'Giovanne', 'Rome', 200, 1003);
INSERT INTO cust (cnum, cname, city, rating, snum) VALUES (2003, 'Liu', 'San Jose', 300, 1002);
INSERT INTO cust (cnum, cname, city, rating, snum) VALUES (2004, 'Grass', 'Brelin', 100, 1002);
INSERT INTO cust (cnum, cname, city, rating, snum) VALUES (2006, 'Clemens', 'London', 300, 1007);
INSERT INTO cust (cnum, cname, city, rating, snum) VALUES (2007, 'Pereira', 'Rome', 100, 1004);
insert into cust (cnum, cname, city, rating, snum) values (2008, 'Cisneros', 'San Jose', 300, 1007);
select * from cust;
CREATE TABLE orders (
    onum INT PRIMARY KEY,
    amt DECIMAL(10, 2),
    odate DATE,
    cnum INT,
    snum INT,
    FOREIGN KEY (cnum) REFERENCES cust(cnum),
    FOREIGN KEY (snum) REFERENCES salespeople(snum)
);
insert into orders values (3001, 18.69, '1994-10-03', 2008, 1007);
insert into orders values (3003, 767.19, '1994-10-03', 2001, 1001);
insert into orders values (3002, 1900.10, '1994-10-03', 2007, 1004);
insert into orders values (3005, 5160.45, '1994-10-03', 2003, 1002);
insert into orders values (3006, 1098.16, '1994-10-04', 2008, 1007);
insert into orders values (3009, 1713.23, '1994-10-04', 2002, 1003);
insert into orders values (3007, 75.75, '1994-10-05', 2004, 1002);
insert into orders values (3008, 4723.00, '1994-10-05', 2006, 1001);
insert into orders values (3010, 1309.95, '1994-10-06', 2004, 1002);
insert into orders values (3011, 9891.88, '1994-10-06', 2006, 1001);
select * from orders;

