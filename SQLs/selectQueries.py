# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 17:50:27 2022

@author: damba
"""

sql_select_films_people_oldest_san_ = '''
    WITH birth_year_order as(
    select f.films_id,f.title, p.people_id, p.name, p.birth_year, 
    	RANK () OVER ( PARTITION BY f.films_id
    		ORDER BY birth_year ASC
    	) birth_year_rank
    from 
    	swapi_films_people_rel_san r,
    	swapi_api_films_san f,
    	swapi_api_people_san p
    where 
    		r.films_id = f.films_id
    	and r.people_id = p.people_id
    	and r.active='Y' and f.current_flag='Y' and p.current_flag='Y'
    )
    select title, name 
      from birth_year_order
    where birth_year_rank=1;
    '''