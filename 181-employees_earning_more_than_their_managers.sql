# Write your MySQL query statement below
select e2.name Employee
from Employee e1 join Employee e2 on e1.id = e2.managerId
where e1.salary < e2.salary;
