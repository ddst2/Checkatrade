# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:19:39 2022

@author: damba
"""

import threading
import time

from Checkatrade.dataPipeline1 import *
from Checkatrade.dataPipeline2 import *

result_available = threading.Event()

def background_pipeline():

    dataPipeline1()

    # when the table creation is done
    result_available.set()


def main():
    thread = threading.Thread(target=background_pipeline)
    thread.start()

    # wait here for the result to be available before continuing
    result_available.wait()
    
    dataPipeline2()

if __name__ == '__main__':
    main()