"""
MySQL User Insert Script - Interactive Version
Loop-basiertes Hinzufügen von Usern mit Input
Beenden mit 'done' (case-insensitive)
"""

import mysql.connector
from mysql.connector import Error


def add_user_to_database(name, email):
    """
    Fügt einen User zur MySQL-Datenbank hinzu
    
    Args:
        name (str): Name des Users
        email (str): Email-Adresse des Users
        
    Returns:
        bool: True wenn erfolgreich, False bei Fehler
    """
    connection = None
    cursor = None
    
    try:
        # Verbindung zur MySQL-Datenbank herstellen
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='people',
            user='root',
            password=''
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL INSERT Statement
            insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            user_data = (name, email)
            
            # Query ausführen
            cursor.execute(insert_query, user_data)
            connection.commit()
            
            print(f"  ✓ User hinzugefügt: {name} ({email}) - ID: {cursor.lastrowid}")
            return True
            
    except Error as e:
        print(f"  ✗ Fehler: {e}")
        return False
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def main():
    """Hauptprogramm mit Input-Loop"""
    
    print("=" * 50)
    print("MySQL User Management - Interactive Mode")
    print("=" * 50)
    print("Gib 'done' ein um zu beenden\n")
    
    user_count = 0
    
    while True:
        # Name eingeben
        name = input("Name: ").strip()
        
        # Beenden-Check (case-insensitive)
        if name.lower() == 'done':
            print(f"\n✓ Fertig! {user_count} User hinzugefügt.")
            break
        
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
        if add_user_to_database(name, email):
            user_count += 1
        
        print()  # Leerzeile für Übersicht


if __name__ == "__main__":
    main()
