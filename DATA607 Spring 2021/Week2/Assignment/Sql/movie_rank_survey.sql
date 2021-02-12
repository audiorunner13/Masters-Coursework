select  cd.first_name as 'First Name',
 cd.last_name as 'Last Name',
 md.movie_name as 'Movie Title',
 mr.movie_rank_nr as 'Movie Rank',
 md.actor_1 as 'Lead Actor',
 case 
   when md.afi_100_rank is null then 'Not Ranked'
   else md.afi_100_rank 
 end as 'AFI 100 Rank',
 md.release_year as 'Year Released'
from movie_rank mr
join customer_dim cd on mr.cust_id = cd.cust_id
join movie_dim md on mr.movie_id = md.movie_id
order by cd.first_name, cd.last_name, md.movie_name;
