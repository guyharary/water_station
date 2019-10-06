#IMPORTS
import sqlite3 as sql

#DATA
db_file = "student.sqlite"


sql_create_table_students ="""
CREATE TABLE IF NOT EXISTS student (
    fname TEXT,
    lname TEXT,
    score INT    
);
"""


#MAIN

#check if database exists, if not create it
with sql.connect(db_file) as conn:

    conn.execute(sql_create_table_students)