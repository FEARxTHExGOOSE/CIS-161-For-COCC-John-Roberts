import sqlite3

con = sqlite3.connect('Music.db')

cursorObj = con.cursor()

cursorObj.execute('create table if not exists Music_Artists(artist text, genre text, number_recordings int)')

music_data = [("Miley", "Rock", 14), ("Dolly", "Country", 123), ("Eminem", "HipHop", 98), ("Brittany", "Rock", 37)]

cursorObj.executemany("INSERT INTO Music_Artists VALUES(?, ?, ?)", music_data)
con.commit()

cursorObj.execute("SELECT * FROM Music_Artists")
rows = cursorObj.fetchall()
for row in rows:
    print(row)

print("")

cursorObj.execute('SELECT artist, genre, number_recordings FROM Music_Artists WHERE genre == "Rock"')
rows2 = cursorObj.fetchall()
for Rock_and_Rows in rows2:
    print(Rock_and_Rows)