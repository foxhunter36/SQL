```python
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# 1. Tabellen löschen/neu erstellen (SQLite)
cur.executescript('''
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Artist;

CREATE TABLE Artist (
  artist_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name       TEXT    UNIQUE
);

CREATE TABLE Genre (
  genre_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name      TEXT    UNIQUE
);

CREATE TABLE Album (
  album_id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title      TEXT    UNIQUE,
  artist_id  INTEGER UNIQUE,
  FOREIGN KEY (artist_id) REFERENCES Artist (artist_id)
);

CREATE TABLE Track (
  track_id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title      TEXT    UNIQUE,
  len        INTEGER,
  rating     INTEGER,
  count      INTEGER DEFAULT 0,
  album_id   INTEGER,
  genre_id   INTEGER,
  FOREIGN KEY(album_id) REFERENCES Album (album_id),
  FOREIGN KEY(genre_id) REFERENCES Genre (genre_id)
);
''')

# 2. Daten einfügen (3 Artists, 5 Alben, 20 Tracks)
cur.executescript('''
-- Artists
INSERT INTO Artist (name) VALUES ('Metallica');
INSERT INTO Artist (name) VALUES ('Lana Del Rey');
INSERT INTO Artist (name) VALUES ('Rihanna');

-- Genres
INSERT INTO Genre (name) VALUES ('Rock');
INSERT INTO Genre (name) VALUES ('Funk');
INSERT INTO Genre (name) VALUES ('House');

-- Alben
INSERT INTO Album (title, artist_id) VALUES ('Master of Puppets', 1);
INSERT INTO Album (title, artist_id) VALUES ('Ultraviolence', 2);
INSERT INTO Album (title, artist_id) VALUES ('Rated R', 3);
INSERT INTO Album (title, artist_id) VALUES ('Ride the Lightning', 1);
INSERT INTO Album (title, artist_id) VALUES ('Born to Die', 2);

-- Tracks (4 pro Album)
INSERT INTO Track (title, len, rating, count, album_id, genre_id) VALUES 
('Master of Puppets', 511, 9, 0, 1, 1),
('Battery', 305, 8, 0, 1, 1),
('Disposable Heroes', 504, 9, 0, 1, 1),
('Welcome Home (Sanitarium)', 389, 8, 0, 1, 1),
('Cruel World', 402, 8, 0, 2, 2),
('Ultraviolence', 290, 9, 0, 2, 2),
('Shades of Cool', 338, 9, 0, 2, 2),
('Brooklyn Baby', 373, 8, 0, 2, 2),
('Rude Boy', 228, 7, 0, 3, 3),
('Russian Roulette', 225, 8, 0, 3, 3),
('Rockstar 101', 211, 7, 0, 3, 3),
('Te Amo', 221, 6, 0, 3, 3),
('Fight Fire with Fire', 289, 9, 0, 4, 1),
('Ride the Lightning', 401, 9, 0, 4, 1),
('For Whom the Bell Tolls', 308, 10, 0, 4, 1),
('Fade to Black', 409, 9, 0, 4, 1),
('Born to Die', 289, 8, 0, 5, 2),
('Blue Jeans', 203, 9, 0, 5, 2),
('Video Games', 294, 10, 0, 5, 2),
('Summertime Sadness', 248, 9, 0, 5, 2);
''')

conn.commit()

# 3. Assignment-Abfragen ausführen
print("=== 1. Track-Tabelle (Screenshot #1) ===")
cur.execute('SELECT * FROM Track')
print(cur.fetchall())

print("\n=== 2. Voll-Join sortiert nach Album-Titel (Screenshot #2) ===")
cur.execute('''
SELECT Track.title, Artist.name AS artist, Album.title AS album, Genre.name AS genre
FROM Track 
JOIN Album ON Track.album_id = Album.album_id
JOIN Artist ON Album.artist_id = Artist.artist_id
JOIN Genre ON Track.genre_id = Genre.genre_id
ORDER BY Album.title ASC
''')
print(cur.fetchall())

print("\n=== 3. Genres für Lana Del Rey (Screenshot #3) ===")
cur.execute('''
SELECT DISTINCT Artist.name, Genre.name AS genre
FROM Artist
JOIN Album ON Artist.artist_id = Album.artist_id
JOIN Track ON Album.album_id = Track.album_id
JOIN Genre ON Track.genre_id = Genre.genre_id
WHERE Artist.name = 'Lana Del Rey'
''')
print(cur.fetchall())

print("\n=== Bonus: Tracks nach Titel DESC ===")
cur.execute('SELECT title FROM Track ORDER BY title DESC')
print(cur.fetchall())

conn.close()
print("\n'music.sqlite' erstellt! Öffne mit DB Browser for SQLite für Screenshots.")
```

**Py4e-ready:** Speichere als `music_db.py`, führe aus → `music.sqlite` wird erstellt. Perfekt für dein letztes Modul!