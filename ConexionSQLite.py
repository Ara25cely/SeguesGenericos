import sqlite3
con = sqlite3.connect("MydataBase.db")
cur = con.cursor()
cur.execute("CREATE TABLE usuarios(nombre, edad)")

cur.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Ejemplo", 30))
con.commit()


