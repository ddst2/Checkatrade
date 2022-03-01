# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:59:48 2022

@author: damba
"""

from Checkatrade.Utils.dbPgUtils import *
from Checkatrade.SQLs.createQueries import *
from Checkatrade.Configs.pgConfig import *


def create_tables():
    
    conn = connect(PG_PARAM_DICT)
    set_schema(conn,SCHEMA_NAME)
    
    create(conn, sql_create_audit_)
    create(conn, sql_create_films_raw_)
    create(conn, sql_create_people_raw_)
    create(conn, sql_create_film_san_)
    create(conn, sql_create_people_san_)
    create(conn, sql_create_relation_san_)