# SQLite Learning Project

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Learning-orange?style=for-the-badge)

Welcome to my SQLite learning repository.  
This project contains simple Python scripts to learn how SQLite works with Python.

---

## Features

- Connect to SQLite database
- Create tables
- Insert data into database
- Select and display data
- Beginner-friendly code
- Easy to understand examples

---

## Project Structure

```bash
Learning_sqlite/
│
├── connect.py      # Connects to SQLite database
├── insert.py       # Creates table and inserts records
├── select.py       # Reads data from database
├── sqlite.db       # SQLite database file
└── README.md

---

## Files Explanation

### `connect.py`

This file is used to create a connection with the SQLite database.

```python
import sqlite3

conn = sqlite3.connect('sqlite.db')
print("Database Connected Successfully")
conn.close()
```

### `insert.py`

This file creates a table and inserts data into it.

```python
import sqlite3

conn = sqlite3.connect('sqlite.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS Student(
    std_id INTEGER PRIMARY KEY AUTOINCREMENT,
    std_name TEXT,
    std_class TEXT,
    std_email_id TEXT
)
''')

print("Table Created Successfully")

conn.close()
```

### `select.py`

This file selects and displays data from the database.

```python
import sqlite3

conn = sqlite3.connect('sqlite.db')

cursor = conn.execute("SELECT * FROM Student")

for row in cursor:
    print(row)

conn.close()
```

---

## How To Run

### 1. Clone Repository

```bash
git clone https://github.com/Osaidgit/Learning_sqlite.git
```

### 2. Open Folder

```bash
cd Learning_sqlite
```

### 3. Run Python Files

```bash
python connect.py
python insert.py
python select.py
```

---

## Important Note

SQLite does not support:

```sql
AUTO_INCREMENT
```

Instead, use:

```sql
INTEGER PRIMARY KEY AUTOINCREMENT
```

Example:

```sql
std_id INTEGER PRIMARY KEY AUTOINCREMENT
```

---

## Learning Goals

This repository helps beginners learn:

* SQLite basics
* Database connections in Python
* Creating tables
* Inserting records
* Selecting records
* Understanding SQL queries

---

## Future Improvements

* Update records
* Delete records
* Search functionality
* User input support
* Menu-based SQLite project
* GUI version with Tkinter

---

## Example SQL Queries

```sql
SELECT * FROM Student;

INSERT INTO Student(std_name, std_class, std_email_id)
VALUES('Ali', '10th', 'ali@gmail.com');

DELETE FROM Student WHERE std_id = 1;
```

---

## Author

Made with ❤️ by Osaid Ali

GitHub: [Osaidgit](https://github.com/Osaidgit)

```
```
