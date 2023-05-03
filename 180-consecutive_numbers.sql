/*
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id is the primary key for this table.
id is an autoincrement column.

Write an SQL query to find all numbers that appear at least three times consecutively.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
*/


# Write your MySQL query statement below

select distinct L1.num ConsecutiveNums
from Logs L1, Logs L2, Logs L3
where L1.num = L2.num and L2.num = L3.num and L1.id = L2.id+1 and L1.id = L3.id+2;

# select distinct t.num as ConsecutiveNums
# from (
#     select
#         lag(num) over (order by id) as prev_num,
#         num,
#         lead(num) over (order by id) as next_num
#     from Logs
# ) t
# where t.num = t.prev_num and t.num = t.next_num;

# with t as (
#     select num,
#     lead(num,1) over() num1,
#     lead(num,2) over() num2
#     from logs
# )
# select distinct num ConsecutiveNums from t where (num=num1) and (num=num2)
