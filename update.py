import sqlite3
conn=sqlite3.connect('sqlite.db')
conn.execute('''
             UPDATE student set Std_name = 'mobing1' WHERE std_id ='2'
             ''')
conn.commit()
conn.close()