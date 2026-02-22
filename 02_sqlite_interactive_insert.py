"""
SQLite User Insert Script - Interactive Version
Loop-basiertes Hinzufügen von Usern mit Input
Beenden mit 'done' (case-insensitive)

VORTEIL: Keine Installation nötig, sqlite3 ist Python built-in!
"""

import sqlite3
import os


def create_database_and_table(db_path):
    """
    Erstellt Datenbank und Tabelle falls nicht vorhanden
    
    Args:
        db_path (str): Pfad zur SQLite-Datenbankdatei
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Tabelle erstellen (falls nicht vorhanden)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    
    connection.commit()
    connection.close()
    print(f"✓ Datenbank bereit: {db_path}\n")


def add_user_to_database(db_path, name, email):
    """
    Fügt einen User zur SQLite-Datenbank hinzu
    
    Args:
        db_path (str): Pfad zur Datenbankdatei
        name (str): Name des Users
        email (str): Email-Adresse des Users
        
    Returns:
        bool: True wenn erfolgreich, False bei Fehler
    """
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        # SQL INSERT Statement
        insert_query = "INSERT INTO users (name, email) VALUES (?, ?)"
        cursor.execute(insert_query, (name, email))
        
        connection.commit()
        user_id = cursor.lastrowid
        
        connection.close()
        
        print(f"  ✓ User hinzugefügt: {name} ({email}) - ID: {user_id}")
        return True
        
    except sqlite3.Error as e:
        print(f"  ✗ Fehler: {e}")
        return False


def show_all_users(db_path):
    """
    Zeigt alle User aus der Datenbank an
    
    Args:
        db_path (str): Pfad zur Datenbankdatei
    """
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM users ORDER BY user_id")
        users = cursor.fetchall()
        
        connection.close()
        
        if users:
            print("\n" + "=" * 50)
            print("Alle User in der Datenbank:")
            print("=" * 50)
            for user in users:
                print(f"ID {user[0]}: {user[1]} ({user[2]})")
            print(f"Total: {len(users)} User")
        else:
            print("\n⚠ Noch keine User in der Datenbank")
            
    except sqlite3.Error as e:
        print(f"✗ Fehler beim Abrufen: {e}")


def main():
    """Hauptprogramm mit Input-Loop"""
    
    # Datenbankpfad festlegen (im gleichen Ordner wie das Script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, 'users.db')
    
    print("=" * 50)
    print("SQLite User Management - Interactive Mode")
    print("=" * 50)
    
    # Datenbank initialisieren
    create_database_and_table(db_path)
    
    print("Gib 'done' ein um zu beenden")
    print("Gib 'show' ein um alle User anzuzeigen\n")
    
    user_count = 0
    
    while True:
        # Name eingeben
        name = input("Name: ").strip()
        
        # Beenden-Check (case-insensitive)
        if name.lower() == 'done':
            print(f"\n✓ Fertig! {user_count} User hinzugefügt.")
            break
        
        # Show all users
        if name.lower() == 'show':
            show_all_users(db_path)
            print()
            continue
        
        # Leere Eingabe abfangen
        if not name:
            print("  ⚠ Name darf nicht leer sein!\n")
            continue
        
        # Email eingeben
        email = input("Email: ").strip()
        
        # Beenden-Check auch bei Email
        if email.lower() == 'done':
            print(f"\n✓ Fertig! {user_count} User hinzugefügt.")
            break
        
        # Leere Email abfangen
        if not email:
            print("  ⚠ Email darf nicht leer sein!\n")
            continue
        
        # User zur DB hinzufügen
        if add_user_to_database(db_path, name, email):
            user_count += 1
        
        print()  # Leerzeile für Übersicht
    
    # Am Ende alle User anzeigen
    show_all_users(db_path)


if __name__ == "__main__":
    main()