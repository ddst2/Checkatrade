# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 08:18:33 2022

@author: damba
"""

import threading


from Checkatrade.Modules.createTables import *
from Checkatrade.Modules.getRawData import *


result_available = threading.Event()

def background_CreateTables():

    create_tables()

    # when the table creation is done
    result_available.set()


def dataPipeline1():
    thread = threading.Thread(target=background_CreateTables)
    thread.start()

    # wait here for the result to be available before continuing
    result_available.wait()
    
    getRawData()
