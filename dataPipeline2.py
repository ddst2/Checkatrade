# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 08:18:26 2022

@author: damba
"""

import threading
import time
import pandas as pd

from Checkatrade.Modules.loadRawToSan import *
from Checkatrade.Modules.getOldestCharacter import *
from Checkatrade.Utils.sendEmail import *


result = pd.DataFrame()
result_available = threading.Event()

def background_loadRawToSan():

    loadRawToSan()

    # when the calculation is done, the result is stored in a global variable
    global result
    result = getOldestCharacter()
    result_available.set()


def dataPipeline2():
    thread = threading.Thread(target=background_loadRawToSan)
    thread.start()

    # wait here for the result to be available before continuing
    result_available.wait()
    
    #enable only on linux
    #sendEmail(result) 
    result.to_excel ('export_Oldest_Character_films.xlsx', index = False, header=True, sheet_name='Oldest')
