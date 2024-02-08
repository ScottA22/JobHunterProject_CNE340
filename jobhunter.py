# Scott Ansman
# CNE 340
# Job Hunter

import mysql.connector
import json
import requests

# https://remotive.com/api/remote-jobs

def connect_to_sql():
    connection = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='jobhunter_db')
    return connection

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS characters (id INT PRIMARY KEY auto_increment, title TEXT, company_name TEXT, category TEXT, job_type TEXT, candidate_required_location TEXT, salary INT, description TEXT)''')

def query_sql(cursor, query):
    cursor.execute(query)
    return cursor

def add_new_remote_job(cursor, remote_job):
    title = remote_job['title']
    company_name = remote_job['company_name']
    category = remote_job['category']
    job_type = remote_job['job_type']
    candidate_required_location = remote_job['candidate_required_location']
    salary = remote_job['salary']
    description = remote_job['description']

    cursor.exexcute('INSERT INTO Jobs(title, company_name, category, job_type, candidate_required_location, salary, description) VALUES(%s, %s, %s, %s, %s, %s, %s)', (title, company_name, category, job_type, candidate_required_location, salary, description))
    return cursor

def check_if_job_exists(cursor, remote_job):
    title = remote_job['title']
    query = f'SELECT * FROM title WHERE name = {title}'
    return query_sql(cursor,query)

def delete_character(cursor, remote_job):
    title = remote_job['title']
    query = f'DELETE FROM title WHERE name = {title}'
    return query_sql(cursor,query)
    return

def add_or_print_character(cursor, fetched_jobs):
    #Loop through characters
    for title in fetched_jobs:
        #Checks if current chracter is in DB
        check_if_job_exists(title)
        #If cursor returns [] then add a new character else print character info
        if not cursor.fetchall():
            add_new_job(cursor, character)
            print(f'New Job added to DB {job["title"]}')
        else:
            print(f'Existing Job found in DB {job["title"]}')



