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



