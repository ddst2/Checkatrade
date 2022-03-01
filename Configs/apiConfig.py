# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 18:17:57 2022

@author: damba
"""

BASE_URL='https://swapi.dev/api'
HEADERS = {'User-Agent': 'swapi-python'}

PEOPLE = 'people'
FILMS = 'films'

single_people_query = "{0}/{1}/{2}/".format(BASE_URL, PEOPLE, str(1))
all_people_query = "{0}/{1}/".format(BASE_URL, PEOPLE)

single_films_query = "{0}/{1}/{2}/".format(BASE_URL, PEOPLE, str(1))
all_films_query = "{0}/{1}/".format(BASE_URL, FILMS)