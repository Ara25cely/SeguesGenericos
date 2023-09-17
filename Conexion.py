import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '25enero2001', host = 'localhost', database = 'ejemplo', port=3306 )

print(conexion)

cursor = conexion.cursor()

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

consulta = "INSERT INTO personas (nombre, edad) VALUES (%s, %s)"
valores = (nombre, edad)

# Ejecuta la consulta para insertar los datos
cursor.execute(consulta, valores)

# Guarda los cambios en la base de datos
conexion.commit()

# Cierra el cursor y la conexión
cursor.close()
conexion.close()







