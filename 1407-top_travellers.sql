# Write your MySQL query statement below

select name, if(sum(distance) is not null, sum(distance), 0) travelled_distance
from Users left join Rides on Users.id = Rides.user_id
group by Users.id order by travelled_distance desc, name;
