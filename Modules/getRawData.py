# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 21:37:53 2022

@author: damba
"""

import json

#import exceptions
from Checkatrade.Utils.dbPgUtils import *
from Checkatrade.SQLs.insertQueries import *
from Checkatrade.SQLs.selectQueries import *
from Checkatrade.Configs.apiConfig import *
from Checkatrade.Configs.pgConfig import *
from Checkatrade.Modules.requestAPI import *


def getRawData():

    conn = connect(PG_PARAM_DICT)
    set_schema(conn,SCHEMA_NAME)
    
    results_films = all_resource_results(all_films_query,conn)
    #print(type(results_films))
    
    json_results_films = json.dumps(results_films, sort_keys=True, indent=4)
    tuple_films_raw = (json_results_films,)
    insert_param(conn,sql_insert_films_raw,tuple_films_raw)
    
    results_people = all_resource_results(all_people_query,conn)
    #print(type(results_people))
    
    json_results_people = json.dumps(results_people, sort_keys=True, indent=4)
    tuple_people_raw = (json_results_people,)
    insert_param(conn,sql_insert_people_raw,tuple_people_raw)
    
    close(conn)
