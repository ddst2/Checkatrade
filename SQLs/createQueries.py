# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:16:52 2022

@author: damba
"""

# create table swapi
sql_create_audit_ =  '''CREATE TABLE IF NOT EXISTS swapi_api_call_audit
                    (
                        batch_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
                        batch_run_date timestamp without time zone DEFAULT now(),
                        request_url character varying(500) COLLATE pg_catalog."default",
                        response_header text COLLATE pg_catalog."default",
                        record_count integer,
                        previous_url character varying(500) COLLATE pg_catalog."default",
                        next_url character varying(500) COLLATE pg_catalog."default",
                        results jsonb
                    )'''

sql_create_films_raw_ = '''CREATE TABLE IF NOT EXISTS swapi_api_films_raw
                        (
                            title character varying(100) COLLATE pg_catalog."default",
                            episode_id smallint,
                            opening_crawl character varying(4000) COLLATE pg_catalog."default",
                            director character varying(200) COLLATE pg_catalog."default",
                            producer character varying(500) COLLATE pg_catalog."default",
                            release_date character varying(29) COLLATE pg_catalog."default",
                            characters character varying(4000) COLLATE pg_catalog."default",
                            planets character varying(4000) COLLATE pg_catalog."default",
                            starships character varying(4000) COLLATE pg_catalog."default",
                            vehicles character varying(4000) COLLATE pg_catalog."default",
                            species character varying(4000) COLLATE pg_catalog."default",
                            created character varying(50) COLLATE pg_catalog."default",
                            edited character varying(50) COLLATE pg_catalog."default",
                            url character varying(200) COLLATE pg_catalog."default"
                        )'''

sql_create_people_raw_ = '''CREATE TABLE IF NOT EXISTS swapi_api_people_raw
                        (
                            name character varying(100) COLLATE pg_catalog."default",
                            height character varying(10) COLLATE pg_catalog."default",
                            mass character varying(10) COLLATE pg_catalog."default",
                            hair_color character varying(200) COLLATE pg_catalog."default",
                            skin_color character varying(200) COLLATE pg_catalog."default",
                            eye_color character varying(200) COLLATE pg_catalog."default",
                            birth_year character varying(200) COLLATE pg_catalog."default",
                            gender character varying(200) COLLATE pg_catalog."default",
                            homeworld character varying(200) COLLATE pg_catalog."default",
                            films character varying(4000) COLLATE pg_catalog."default",
                            species character varying(4000) COLLATE pg_catalog."default",
                            vehicles character varying(4000) COLLATE pg_catalog."default",
                            starships character varying(4000) COLLATE pg_catalog."default",
                            created character varying(50) COLLATE pg_catalog."default",
                            edited character varying(50) COLLATE pg_catalog."default",
                            url character varying(200) COLLATE pg_catalog."default"
                        )'''

sql_create_film_san_ = '''
                        CREATE TABLE IF NOT EXISTS swapi_api_films_san
                        (
                            films_id smallint NOT NULL,
                            title character varying(100) COLLATE pg_catalog."default",
                            episode_id smallint,
                            opening_crawl character varying(4000) COLLATE pg_catalog."default",
                            director character varying(200) COLLATE pg_catalog."default",
                            producer character varying(500) COLLATE pg_catalog."default",
                            release_date character varying(29) COLLATE pg_catalog."default",
                            created character varying(50) COLLATE pg_catalog."default",
                            edited character varying(50) COLLATE pg_catalog."default" NOT NULL,
                            current_flag character varying(1) COLLATE pg_catalog."default" NOT NULL,
                            CONSTRAINT swapi_api_films_san_pkey PRIMARY KEY (films_id, edited, current_flag)
                        )'''

sql_create_people_san_ = '''
                        CREATE TABLE IF NOT EXISTS swapi_api_people_san
                        (
                            people_id smallint NOT NULL,
                            name character varying(100) COLLATE pg_catalog."default",
                            height character varying(20) COLLATE pg_catalog."default",
                            mass character varying(20) COLLATE pg_catalog."default",
                            hair_color character varying(200) COLLATE pg_catalog."default",
                            skin_color character varying(200) COLLATE pg_catalog."default",
                            eye_color character varying(200) COLLATE pg_catalog."default",
                            birth_year character varying(200) COLLATE pg_catalog."default",
                            gender character varying(200) COLLATE pg_catalog."default",
                            created character varying(50) COLLATE pg_catalog."default",
                            edited character varying(50) COLLATE pg_catalog."default" NOT NULL,
                            current_flag character varying(1) COLLATE pg_catalog."default" NOT NULL,
                            CONSTRAINT swapi_api_people_san_pkey PRIMARY KEY (people_id, edited, current_flag)
                        )'''

sql_create_relation_san_ = '''
                        CREATE TABLE IF NOT EXISTS swapi_films_people_rel_san
                        (
                            fp_rel_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 32767 CACHE 1 ),
                            films_id smallint,
                            people_id smallint,
                            created timestamp without time zone,
                            edited timestamp without time zone,
                            active character varying(1) COLLATE pg_catalog."default" NOT NULL,
                            CONSTRAINT swapi_films_people_rel_san_pkey PRIMARY KEY (fp_rel_id),
                            CONSTRAINT swapi_films_people_rel_san_ukey UNIQUE (films_id, people_id, edited)
                        )
                        '''
