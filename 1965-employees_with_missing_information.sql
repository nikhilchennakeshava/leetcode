SELECT T.employee_id
FROM  
  (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
   UNION 
   SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
AS T
WHERE T.salary IS NULL OR T.name IS NULL
ORDER BY employee_id;

# Write your MySQL query statement below
# select distinct e.employee_id employee_id
# from Employees e full outer join Salaries s on e.employee_id = s.employee_id
# where name is null or salary is null
# order by employee_id;

# select distinct e.employee_id employee_id
# from Employees e, Salaries s
# where name is null or salary is null
# order by employee_id;
