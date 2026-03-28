import os
import sqlite3
conn =sqlite3.connect('sqlite.db')
conn.execute('''
             create table student (
             std_id INTEGER PRIMARY KEY AUTOINCREMENT,
             std_name VARCHAR(10),
             std_class VARCHAR(10),
             std_email_id VARCHAR(30)
             )
        ''')
conn.close()