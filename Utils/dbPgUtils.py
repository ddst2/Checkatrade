# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 17:55:57 2022

@author: damba
"""
import psycopg2 as pg
import pandas as pd
import sys

def connect(param_dict):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = pg.connect(**param_dict)
    except (Exception, pg.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

# function to set schema in projects database     
def set_schema(conn, schema):
    cursor = conn.cursor() # create cursor object
    sql_set = 'SET search_path to '+ schema
    cursor.execute(sql_set) # execute query
    print('Schema has been set successfully!!!')


# function to read from database
def read(conn, read_):
    print('Read')
    cursor = conn.cursor()
    cursor.execute(read_)
    for row in cursor:
        print(f'row = {row}')
    print()
    
# function to create in projects database     
def create(conn, create_):
    cursor = conn.cursor() # create cursor object
    cursor.execute(create_) # execute query
    conn.commit() # commit query to database
    print('Table have been created successfully!!!')
    
# function to insert in projects database     
def insert(conn, insert_):
    cursor = conn.cursor()
    cursor.execute(insert_)
    conn.commit()
    print('Records have been successfully inserted!!!')
    
# function to insert in projects database     
def insert_param(conn, insert_param_,tuple_param):
    cursor = conn.cursor()
    cursor.execute(insert_param_,tuple_param)
    conn.commit()
    print('Records have been successfully inserted!!!')    
    
# function to update table
def update(conn, update_):
    print('Update')
    cursor = conn.cursor()
    cursor.execute(update_)
    conn.commit()
    
# function to delete in projects database
def delete(conn, delete_):
    print('Delete')
    cursor = conn.cursor()
    cursor.execute(delete_)
    conn.commit()
    
# close the cursor and connection to the server 
def close(conn):
    #cursor.close()
    conn.close()   
    
# function to create pandas dataframe
def create_pandas_df(sql_query, database):
    table = pd.read_sql_query(sql_query, database)
    return table
