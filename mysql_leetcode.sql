#175. Combine Two Tables

select p.firstName,p.lastName,c.city,c.state from person p left join Address c on p.personId = c.personId;

# 183. Customers Who Never Order
select name as Customers from Customers where id not in (select customerId from Orders);