# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 18:32:02 2022

@author: damba
"""
import requests
import json

from  Checkatrade.Configs.apiConfig import *
from Checkatrade.Utils.dbPgUtils import *
from Checkatrade.SQLs.insertQueries import *

def single_response(query):
    try:
        response = requests.get(query, headers=HEADERS)
        response.raise_for_status()
    
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    
    if response.status_code != 200:
        raise exceptions.ResourceDoesNotExist('Resource does not exist')
    
    return response


def all_resource_results(query,conn):
    ''' Get all the URLs for every resource '''
    results = []
    next = True
    
    while next:
        try:
            response = requests.get(query, headers=HEADERS)
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)            
        
            
        if response.status_code != 200:
            raise exceptions.ResourceDoesNotExist('Resource does not exist')
        
        #json_data = json.loads(response.content)
        json_data = response.json()
        json_headers = json.dumps(dict(response.headers), sort_keys=True, indent=4)
        json_results = json.dumps(json_data['results'], sort_keys=True, indent=4)
        
        tuple_audit = (response.url, json_headers, json_data['count'], json_data['previous'], json_data['next'],json_results) 
        #print(type(json_headers))
        #print(json_results)
        insert_param(conn,sql_insert_audit,tuple_audit)
        
        for resource in json_data['results']:
            results.append(resource)
        if bool(json_data['next']):
            query = json_data['next']
        else:
            next = False
    return results