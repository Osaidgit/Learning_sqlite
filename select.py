import sqlite3
conn=sqlite3.connect('sqlite.db')
data=conn.execute('SELECT * FROM student LIMIT 0,1')
print('std_id std_name std_class std_email_id')

for n in data:
    print(n)