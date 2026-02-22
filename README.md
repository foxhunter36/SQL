# SQL Learning Repository

**Interactive Database User Management Scripts**  
Part of my Python & SQL learning journey (Python for Everybody - Coursera)

---

## 📚 Overview

This repository contains Python scripts for interactive database user management, demonstrating both **MySQL** and **SQLite** implementations with identical functionality but different backend technologies.

---

## 🗂️ Repository Structure

```
SQL/
├── mysql_interactive_insert.py    # MySQL version (requires server)
├── sqlite_interactive_insert.py   # SQLite version (standalone)
├── README.md
└── .gitignore
```

---

## 🎯 Features

### Both Versions Include:
- ✅ **Interactive Loop** - Add multiple users in one session
- ✅ **Case-Insensitive Exit** - Type `done`, `DONE`, or `DoNe` to quit
- ✅ **Input Validation** - Prevents empty name/email entries
- ✅ **User Counter** - Shows total users added at the end

### SQLite Bonus Features:
- ✅ **Auto Table Creation** - Creates `users` table if not exists
- ✅ **Show Command** - Type `show` to list all users during input
- ✅ **End Summary** - Displays all users after completion
- ✅ **No Installation Required** - Uses Python's built-in `sqlite3`

---

## 🚀 Usage

### MySQL Version

**Requirements:**
```bash
pip install mysql-connector-python
```

**Prerequisites:**
- MySQL server running (e.g., XAMPP)
- Database `people` exists
- Table `users` with columns: `user_id`, `name`, `email`

**Run:**
```bash
python mysql_interactive_insert.py
```

---

### SQLite Version

**No Installation Required!** - SQLite is built into Python

**Run:**
```bash
python sqlite_interactive_insert.py
```

The script automatically creates `users.db` in the same directory.

---

## 📊 Database Schema

Both versions use identical table structure:

```sql
users
├── user_id   (INTEGER, PRIMARY KEY, AUTO_INCREMENT)
├── name      (VARCHAR/TEXT, NOT NULL)
└── email     (VARCHAR/TEXT, NOT NULL)
```

---

## 💡 Example Session

```
==================================================
SQLite User Management - Interactive Mode
==================================================
✓ Datenbank bereit: C:\...\users.db

Gib 'done' ein um zu beenden
Gib 'show' ein um alle User anzuzeigen

Name: Max
Email: max@example.com
  ✓ User hinzugefügt: Max (max@example.com) - ID: 1

Name: Anna
Email: anna@test.de
  ✓ User hinzugefügt: Anna (anna@test.de) - ID: 2

Name: show

==================================================
Alle User in der Datenbank:
==================================================
ID 1: Max (max@example.com)
ID 2: Anna (anna@test.de)
Total: 2 User

Name: done

✓ Fertig! 2 User hinzugefügt.
```

---

## 🔧 Key Differences: MySQL vs SQLite

| Feature | MySQL | SQLite |
|---------|-------|--------|
| **Installation** | Requires `mysql-connector-python` | Built-in (`sqlite3`) |
| **Server** | Needs MySQL server (XAMPP/local) | File-based, no server |
| **Credentials** | Username/Password required | No authentication |
| **Placeholder** | `%s` | `?` |
| **Storage** | Server database | `.db` file |
| **Best For** | Production, multi-user apps | Learning, prototyping, single-user |

---

## 🎓 Learning Outcomes

Through building these scripts, I learned:

- ✅ Database connection management (MySQL vs SQLite)
- ✅ SQL INSERT operations with parameterized queries
- ✅ Input validation and error handling
- ✅ Loop control with case-insensitive conditions
- ✅ File path handling for SQLite databases
- ✅ Auto-incrementing primary keys
- ✅ Transaction management (commit/rollback)

---

## 📁 Files

### `mysql_interactive_insert.py`
- Connects to MySQL server (localhost:3306)
- Database: `people`
- Table: `users`
- Requires running MySQL instance

### `sqlite_interactive_insert.py`
- Creates `users.db` in script directory
- Auto-creates table if not exists
- No external dependencies
- Includes `show` command and summary display

---

## 🔗 Related Learning

- **Course:** Python for Everybody (Coursera)
- **Topics:** SQL, Database Design, Python DB-API
- **Skills:** MySQL, SQLite, Python, Git

---

## 📝 License

Educational project - free to use and modify

---

## 👤 Author

**André** | Performance Marketing Manager → Aspiring Quant Trader  
Learning Python, SQL, Machine Learning for Algorithmic Trading

GitHub: [@foxhunter36](https://github.com/foxhunter36)
