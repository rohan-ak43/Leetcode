#175. Combine Two Tables

select p.firstName,p.lastName,c.city,c.state from person p left join Address c on p.personId = c.personId;

# 183. Customers Who Never Order
select name as Customers from Customers where id not in (select customerId from Orders);

# 1890. The Latest Login in 2020
select user_id, max(time_stamp) as last_stamp 
FROM Logins 
where time_stamp >= '2020-01-01 00:00:00' and time_stamp < '2021-01-01 00:00:00' 
GROUP BY user_id;

# 182. Duplicate Emails
select email from Person 
GROUP BY email 
having COUNT(EMAIL) > 1;

# 196. Delete Duplicate Emails
delete p from Person p
JOIN Person p2
ON p.email = p2.email AND p.id>p2.id;

# 197. Rising Temperature
SELECT weather1.id FROM weather weather1, weather weather2
WHERE DATEDIFF(weather1.recordDate, weather2.recordDate) = 1 
AND weather1.temperature>weather2.temperature;

# 511. Game Play Analysis I
SELECT player_id,min(event_date) 
AS first_login 
FROM Activity 
GROUP BY player_id;