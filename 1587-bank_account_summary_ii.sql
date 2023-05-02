# Write your MySQL query statement below

select name, sum(amount) balance
from Users join Transactions using (account)
group by name having balance > 10000;
