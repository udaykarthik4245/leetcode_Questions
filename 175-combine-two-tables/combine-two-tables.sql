# Write your MySQL query statement below
-- select p.firstName,p.lastName,a.city,a.state from 
-- person p
-- inner join address a on 
-- p.personId=a.personId;
SELECT p.firstName, p.lastName, a.city, a.state
FROM person p
LEFT JOIN address a ON p.personId = a.personId;
