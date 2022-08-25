import sqlite3

con = sqlite3.connect('alumnos.db')
cur = con.cursor()

cur.execute("CREATE TABLE alumnos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT)")
cur.execute("INSERT INTO alumnos (nombre,apellido) VALUES ('Alba', 'Gonzalez')")
cur.execute("INSERT INTO alumnos (nombre,apellido) VALUES ('Antonio', 'Perez')")
cur.execute("INSERT INTO alumnos (nombre,apellido) VALUES ('Jose', 'Blanco')")
cur.execute("INSERT INTO alumnos (nombre,apellido) VALUES ('Victor', 'Torres')")
cur.execute("INSERT INTO alumnos (nombre,apellido) VALUES ('Carmen', 'Castillo')")
cur.execute("INSERT INTO alumnos (nombre,apellido) VALUES ('Sofia', 'Reyes')")
cur.execute("INSERT INTO alumnos (nombre,apellido) VALUES ('Manuel', 'Gomez')")
cur.execute("INSERT INTO alumnos (nombre,apellido) VALUES ('Jorge', 'Vázquez')")
con.commit()

cur.execute("SELECT * FROM alumnos WHERE nombre like 'Jo%' ORDER BY nombre")
alumnos = cur.fetchall()
con.close()

print(alumnos)

