# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 21:45:33 2022

@author: damba
"""


#import exceptions
from Checkatrade.Utils.dbPgUtils import *
from Checkatrade.SQLs.insertQueries import *
from Checkatrade.SQLs.updateQueries import *
from Checkatrade.Configs.apiConfig import *
from Checkatrade.Configs.pgConfig import *
from Checkatrade.Modules.requestAPI import *


def loadRawToSan():

    conn = connect(PG_PARAM_DICT)
    set_schema(conn,SCHEMA_NAME)
    
    update(conn, sql_update_films_san_)
    insert(conn, sql_insert_films_san_)
    
    update(conn, sql_update_people_san_)
    insert(conn, sql_insert_people_san_)
    
    update(conn, sql_update_films_people_rel_san_)
    insert(conn, sql_insert_films_people_rel_san_)    
    
    close(conn)