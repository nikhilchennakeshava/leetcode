# Write your MySQL query statement below
with t as
(select max(salary) Salary, Department.name Department, departmentId
from Employee join Department on Employee.departmentId = Department.id 
group by departmentId)
select t.Department Department, Employee.name Employee, Employee.salary Salary
from Employee join t on Employee.departmentId = t.departmentId
where Employee.salary = t.Salary;
