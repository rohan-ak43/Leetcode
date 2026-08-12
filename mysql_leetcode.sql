#175. Combine Two Tables

select p.firstName,p.lastName,c.city,c.state from person p left join Address c on p.personId = c.personId;

# 183. Customers Who Never Order
select name as Customers from Customers where id not in (select customerId from Orders);

# 1890. The Latest Login in 2020
select user_id, max(time_stamp) as last_stamp 
FROM Logins 
where time_stamp >= '2020-01-01 00:00:00' and time_stamp < '2021-01-01 00:00:00' 
GROUP BY user_id;