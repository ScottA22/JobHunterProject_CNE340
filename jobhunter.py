import mysql.connector
import json
import requests

# https://remotive.com/api/remote-jobs

def connect_to_sql():
    connection = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='jobhunter_db')
    return connection

def fetch_jobs():
    response = requests.get('https://remotive.com/api/remote-jobs')
    data = json.loads(response.text)
    return data['jobs']

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Jobs (id INT PRIMARY KEY auto_increment, title TEXT, company_name TEXT, category TEXT, job_type TEXT, candidate_required_location TEXT, salary TEXT, description TEXT)''')

def add_new_remote_job(cursor, remote_job):
    title = remote_job['title']
    company_name = remote_job['company_name']
    category = remote_job['category']
    job_type = remote_job['job_type']
    candidate_required_location = remote_job['candidate_required_location']
    salary = remote_job['salary']
    description = remote_job['description']

    cursor.execute('INSERT INTO Jobs(title, company_name, category, job_type, candidate_required_location, salary, description) VALUES(%s, %s, %s, %s, %s, %s, %s)', (title, company_name, category, job_type, candidate_required_location, salary, description))
    return cursor

def check_if_job_exists(cursor, remote_job):
    title = remote_job['title']
    query = f"SELECT * FROM Jobs WHERE title = '{title}'"
    cursor.execute(query)
    return cursor.fetchall()

def delete_job(cursor, remote_job):
    title = remote_job['title']
    query = f"DELETE FROM Jobs WHERE title = '{title}'"
    cursor.execute(query)

def add_or_print_job(cursor, fetched_jobs):
    for job in fetched_jobs:
        if not check_if_job_exists(cursor, job):
            add_new_remote_job(cursor, job)
            print(f'New Job added to DB {job["title"]}')
        else:
            print(f'Existing Job found in DB {job["title"]}')

def main():
    connection = connect_to_sql()
    cursor = connection.cursor()
    create_table(cursor)
    data = fetch_jobs()
    add_or_print_job(cursor, data)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()