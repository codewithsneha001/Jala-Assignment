use jalaSQL;
-- 1.	Display snum,sname,city and comm of all salespeople
select * from salespeople;
select snum, sname, city, comm from salespeople;

-- 2.	Display all snum without duplicates from all orders.
select distinct snum from orders;

-- 3.	Display names and commissions of all salespeople in london.
select sname, comm from salespeople where city='london';

-- 4.	All customers with rating of 100.
select * from cust where rating=100;
select cname from cust where rating=100;

-- 5.	Produce orderno, amount and date form all rows in the order table.
select onum, amt, odate from orders;

-- 6.	All customers in San Jose, who have rating more than 200.
select * from cust where city='San Jose' and rating>200;
select cname from cust where city='San Jose' and rating>200;

-- 7.	All customers who were either located in San Jose or had a rating above 200.
select * from cust where city='San Jose' or rating>200;
select cname from cust where city='San Jose' or rating>200;

-- 8.	All orders for more than $1000.
select * from orders where amt>1000;

-- 9.	Names and citires of all salespeople in london with commission above 0.10.
select sname, city from salespeople where comm>0.10;

-- 10.	All customers excluding those with rating <= 100 unless they are located in Rome.
select * from cust where city='Rome' or rating>100;

-- 11.	All salespeople either in Barcelona or in london.
select * from salespeople where city='Barcelona' or city='london';

-- 12.	All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded)
select * from salespeople where comm>0.10 and comm<0.12;

-- 13.	All customers with NULL values in city column.
select * from cust where city='NULL';
select * from cust where city is NULL;

-- 14.	All orders taken on Oct 3Rd   and Oct 4th  1994.
select * from orders where odate in ('1994-10-03','1994-10-04');

-- 15.	All customers serviced by peel or Motika.
select * from cust where snum in( select snum from salespeople where sname in('Peel', 'Motika'));  
select cname from cust, orders where orders.cnum = cust.cnum and orders.snum in (
    select snum from salespeople where sname in ('Peel', 'Motika'));

-- 16.	All customers whose names begin with a letter from A to B.
select cname from cust where cname like 'A%' or cname like 'B%';

-- 17.	All orders except those with 0 or NULL value in amt field.
select * from orders where amt!=0 or amt!='NULL';
select * from orders where amt!=0 or amt is not null;

-- 18.	Count the number of salespeople currently listing orders in the order table.
select count(distinct snum) from orders;

-- 19.	Largest order taken by each salesperson, datewise.
select odate, snum, max(amt) from orders group by odate, snum order by odate, snum;

-- 20.	Largest order taken by each salesperson with order value more than $3000.
select odate, snum, amt from orders where amt>3000;
select odate, snum, max(amt) from orders where amt>3000 group by odate, snum order by odate, snum;

-- 21.	Which day had the hightest total amount ordered.
select max(amt) from orders;
select odate, amt, snum, cnum from orders where amt=(select max(amt) from orders); 

-- 22.	Count all orders for Oct 3rd.
select odate, count(odate) from orders where odate='1994-10-03';
select count(*) from orders where odate='1994-10-03';

-- 23.	Count the number of different non NULL city values in customers table.
select count(distinct city) from cust;

-- 24.	Select each customer’s smallest order.
select cnum, min(amt) from orders group by cnum;

-- 25.	First customer in alphabetical order whose name begins with G.
select min(cname) from cust where cname like 'G%';
select * from cust where cname like 'G%' order by cname limit 1;

-- 26.	Get the output like “ For dd/mm/yy there are ___ orders.
select concat('For ', date_format(odate, '%d/%m/%y ') , 'there ', 'are ', count(*), ' orders.') as sentence from orders group by odate; 

-- 27.	Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson’s commission for that order.
select onum, snum, amt, amt*0.12 as commission from orders;
-- 28.	Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is : (rating).
select concat('For the city ', city, ' the highest rating is : ', max(rating)) as sentence from cust group by city;

-- 29.	Display the totals of orders for each day and place the results in descending order.
	Select odate, count(onum)
	from orders
	group by odate
	order by count(onum) desc;
    
-- 30.	All combinations of salespeople and customers who shared a city. (ie same city).
select sname,cname from salespeople, cust where salespeople.city=cust.city;
select * from salespeople, cust where salespeople.city=cust.city;

-- 31.	Name of all customers matched with the salespeople serving them.
	Select cname, sname, cust.snum, salespeople.snum
	from cust, salespeople
	where cust.snum = salespeople.snum;

-- 32.	List each order number followed by the name of the customer who made the order.
select onum,cname from orders, cust where orders.cnum=cust.cnum;

-- 33.	Names of salesperson and customer for each order after the order number.
select onum,cname,sname from orders,salespeople, cust where orders.cnum=cust.cnum and orders.snum=salespeople.snum;

-- 34.	Produce all customer serviced by salespeople with a commission above 12%.
select cname, sname, comm from salespeople, cust where comm>0.12 and cust.snum=salespeople.snum;

-- 35.	Calculate the amount of the salesperson’s commission on each order with a rating above 100.
select sname, amt*comm, cust.cnum from salespeople, orders, cust where rating>100 and 
salespeople.snum=orders.snum and salespeople.snum=cust.snum and orders.cnum=cust.cnum;

-- 36.	Find all pairs of customers having the same rating.
select a.cname, b.cname, a.rating from cust a, cust b where a.rating=b.rating and a.cnum<b.cnum;
select a.cname, b.cname, a.rating from cust a, cust b where a.rating=b.rating and a.cnum!=b.cnum;
-- 37.	Find all pairs of customers having the same rating, each pair coming once only.
select a.cname, b.cname, a.rating from cust a, cust b where a.rating=b.rating and a.cnum<b.cnum and a.cnum<b.cnum;

-- 38.	Policy is to assign three salesperson to each customers. Display all such combinations.
select c.cname as customer_name, s1.snum as salesperson1, s2.snum as salesperson2, s3.snum as salesperson3
from cust c, salespeople s1, salespeople s2, salespeople s3 where s1.snum < s2.snum and s2.snum < s3.snum;

-- 39.	Display all customers located in cities where salesman serres has customer.
select * from cust where city in (select city from cust where snum=(select snum from salespeople where sname='Serres'));

-- 40.	Find all pairs of customers served by single salesperson.
select c1.cname as customer1, c2.cname as customer2, c1.snum as salesperson from cust c1 join cust c2 on c1.snum = c2.snum and c1.cnum < c2.cnum;


-- 41.	Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed.
select s1.sname, s2.sname, s1.city from salespeople s1, salespeople s2 where s1.city=s2.city and s1.snum<s2.snum;
