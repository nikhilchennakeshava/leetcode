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
