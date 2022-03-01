# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:16:52 2022

@author: damba
"""

sql_update_films_san_ = '''	
	 WITH r as (	SELECT CAST(split_part(url,'/',6) AS INTEGER) as films_id,
								title, episode_id, opening_crawl, director, producer, release_date, created, edited, 'Y' as current_flag
							from swapi_api_films_raw)
	UPDATE swapi_api_films_san s SET current_flag = 'N'
	  from r
	 where s.films_id = r.films_id
	   and s.edited < r.edited
	   and s.current_flag = 'Y';
       '''

sql_update_people_san_ = '''		
	 WITH r as (	SELECT CAST(split_part(url,'/',6) AS INTEGER) as people_id,
								name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, created, edited, 'Y' as current_flag
							from swapi_api_people_raw)
	UPDATE swapi_api_people_san s SET current_flag = 'N'
	  from r
	 where s.people_id = r.people_id
	   and s.edited < r.edited
	   and s.current_flag = 'Y';
       '''
	
sql_update_films_people_rel_san_ = '''
	WITH r AS(
	SELECT  
			CAST(split_part(url,'/',6) as integer) as films_id, 
			CAST(split_part(regexp_split_to_table(regexp_replace(substring(characters,2,length(characters)-2),E'[\\n\\r ]+', ' ', 'g'), ','),'/',6) as smallint) as people_id,
			CAST(now() as timestamp) as created,
			CAST(now() as timestamp) as edited,
			'Y' as active
	FROM swapi_api_films_raw)
	UPDATE swapi_films_people_rel_san s	SET active='N'
	FROM r
	 where s.films_id = r.films_id
	   and s.people_id = r.people_id
	   and s.edited < r.edited
	   and s.active = 'Y'; 
       '''