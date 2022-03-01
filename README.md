# Checkatrade

Project Structure

/Checkatrade
├── _init_.py
├── dataPipeline.py 		- master script to run pipiline1 and wait to finish before executing pipeline2
├── dataPipeline1.py		- create table in schema if not exists and wait to finish before pulling the data and storing in raw tables
├── dataPipeline2.py		- Load data from raw table to sanitised table and wait to finish before extracting the oldest character details to excel or email
├───Configs
│   └─── _init_.py
│   └─── apiConfig.py		- has base url and header details, can hold api authentication details
│   └─── emailConfig.py		- has email server, sender snd recipient details
│   └─── pgConfig.py		- has postgres databse details
├───DAGs
│   └─── _init_.py
│   └─── SQLs			- to hold .sql files which can be executed using postgresOperators, for future use
│   └─── dagPipeline.py		- to execute the different pipeline with required dependency and schedule, for future use
├───Exceptions
│   └─── _init_.py
│   └─── exceptions.py		- to cutomise exceptions, for future use
├───Modules
│   └─── _init_.py
│   └─── createTables.py	- create require database tables
│   └─── getOldestCharacter.py	- List Oldest characters by film
│   └─── getRawData.py		- Call APIs to pull all required data
│   └─── loadRawToSan.py	- Load data from raw tables to sanitised tables
│   └─── requestAPI.py		- Modules to call different swapi APIs and capture the details in Audit table
├───SQLs
│   └─── _init_.py
│   └─── createQueries.py	- Holds create tables query
│   └─── insertQueries.py	- holds insert queries, has delete commands for raw tables for truncate and reload
│   └─── selectQueries.py	- holds select queries for oldest character
│   └─── updateQueries.py	- holds updates queries to manage change data
├───Utils
│   └─── _init_.py
│   └─── dbPgUtils.py		- holds all type of database operation
│   └─── sendEmail.py		- send email with HTML structure of oldest charactrs (not able to test in my windows laptop)
│   └─── setupLogger.py		- to cpature the execution to log, for future use
└─── readMe.txt
└─── requirements.txt


--------
Pre-requisite: Before Start Executing Pipeline
Step1 - Install Anaconda Python(3.8.8) Distributor
Step2 - Install Postgres Server with pgAdmin4

Then, Copy the folder Checkatrade
Step1 - Install python modules from requirements.txt 
Step2 - Create Database in postgres and create schema
Step3 - Update the DB details in PG_PARAM_DICT and change SCHEMA_NAME in config folder

Then, change the working directory to 'Checkatrade'
Step1 - execute the dataPipeline.py - this will execute ened to end flow
Step2 - Check "export_Oldest_Character_films.xlxs" in .../Checkatrade path

Note - the logging, exception and airflow modules/parts are missing
