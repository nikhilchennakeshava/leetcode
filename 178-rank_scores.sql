# Write your MySQL query statement below

# select score, (select count(distinct score) from Scores where score >= s.score) `rank`
# from Scores s
# order by score desc;

SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) `rank`
FROM Scores ORDER BY score DESC;
