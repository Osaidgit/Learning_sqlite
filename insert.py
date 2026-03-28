import sqlite3
conn=sqlite3.connect('sqlite.db')
ins=('''
    INSERT INTO student (std_name, std_class, std_email_id) VALUES
    ('kufu', '7th', 'bablu13@gmail.com')
    
    ''')
conn.execute(ins)
conn.commit()
conn.close()
