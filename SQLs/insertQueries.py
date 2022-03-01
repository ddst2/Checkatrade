# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:16:52 2022

@author: damba
"""

sql_insert_audit = '''
    INSERT INTO swapi_api_call_audit(
        request_url, response_header, record_count, previous_url, next_url, results)
	VALUES (%s,%s,%s,%s,%s,%s);
    '''
    
sql_insert_films_raw = '''
    DELETE FROM swapi_api_films_raw;
    INSERT INTO swapi_api_films_raw
        SELECT * FROM json_populate_recordset (NULL::swapi_api_films_raw,%s);
    '''
    
sql_insert_people_raw = '''
    DELETE FROM swapi_api_people_raw;
    INSERT INTO swapi_api_people_raw
        SELECT name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, homeworld, films, species, vehicles, starships, created, edited, url 
            FROM json_populate_recordset (NULL::swapi_api_people_raw,%s);
    '''

sql_insert_films_san_ = '''
	INSERT INTO swapi_api_films_san
	SELECT CAST(split_part(url,'/',6) AS INTEGER) as films_id,
             r.title, r.episode_id, r.opening_crawl, r.director, r.producer, r.release_date, r.created, r.edited, 'Y' as current_flag
	from swapi_api_films_raw r left join swapi_api_films_san s
        on CAST(split_part(r.url,'/',6) AS INTEGER) = s.films_id
    where r.edited < s.edited
      and s.current_flag = 'Y';
    '''


sql_insert_people_san_ = '''
	INSERT INTO swapi_api_people_san
	SELECT CAST(split_part(url,'/',6) AS INTEGER) as people_id,
            r.name, r.height, r.mass, r.hair_color, r.skin_color, r.eye_color, r.birth_year, r.gender, r.created, r.edited, 'Y' as current_flag
	from swapi_api_people_raw r left join swapi_api_people_san s
    on CAST(split_part(r.url,'/',6) AS INTEGER) = s.people_id
    where r.edited < s.edited
      and s.current_flag = 'Y';
    '''

sql_insert_films_people_rel_san_ = '''
    INSERT INTO swapi_films_people_rel_san(
			films_id, people_id, created, edited, active)
	WITH tbl AS(
	SELECT  
			CAST(split_part(url,'/',6) as integer) as films_id, 
			CAST(split_part(regexp_split_to_table(regexp_replace(substring(characters,2,length(characters)-2),E'[\\n\\r ]+', ' ', 'g'), ','),'/',6) as smallint) as people_id,
			CAST(now() as timestamp) as created,
			CAST(now() as timestamp) as edited,
			'Y' as active
	FROM swapi_api_films_raw)
	SELECT * FROM tbl;
    '''
