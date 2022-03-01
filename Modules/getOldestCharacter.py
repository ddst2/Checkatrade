# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 07:50:26 2022

@author: damba
"""

import pandas as pd

#import exceptions
from Checkatrade.Utils.dbPgUtils import *
from Checkatrade.SQLs.selectQueries import *
from Checkatrade.Configs.pgConfig import *
from Checkatrade.Modules.requestAPI import *


def getOldestCharacter():

    conn = connect(PG_PARAM_DICT)
    set_schema(conn,SCHEMA_NAME)
    
    df = create_pandas_df(sql_select_films_people_oldest_san_, database=conn)
    print(df.head(10))
    
    close(conn)
    
    return df