import sqlite3
conn=sqlite3.connect('sqlite.db')
st_id=input('Enter the Stident id to delete:')
conn.execute('DELETE FROM student WHERE std_id='+st_id)
conn.comm1it()
conn.close()