# Write your MySQL query statement below
# select name Customers from Customers
# where id not in (select customerId from Orders);

select name Customers
from Customers left join Orders on Customers.id = Orders.CustomerId
where Orders.id is null;
