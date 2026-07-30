#175. Combine Two Tables

select p.firstName,p.lastName,c.city,c.state from person p left join Address c on p.personId = c.personId;