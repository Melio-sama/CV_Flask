import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('DUPONT', 'Emilie', 'Je suis Nathan'))
cur.execute("INSERT INTO clients (nom, prenom, message) VALUES (?, ?, ?)",('LEROUX', 'Lucas', 'Je suis Amadou'))



connection.commit()
connection.close()
