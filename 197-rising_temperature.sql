# Write your MySQL query statement below

select w1.id id 
from Weather w1, Weather w2
where w1.temperature > w2.temperature and subdate(w1.recordDate,1) = w2.recordDate;
