import mysql.connector

def conectar_a_db():
    """
    Esta función establece una conexión a la base de datos local sin contraseña.

    Args:
        None

    Returns:
        mysql.connector.connect: Un objeto de conexión a la base de datos, o None si ocurre un error.
    """

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="basedatos",
            charset='utf8'
        )
        return mydb
    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None

def mostrar_listado():
    """
    Muestra el listado de la tabla 'tabla1' en formato tabular.
    """
    mydb = conectar_a_db()
    if mydb is None:
        return

    cursor = mydb.cursor()
    cursor.execute("SELECT nombre, apellidos, DNI FROM tabla1")
    resultados = cursor.fetchall()

    # Encabezados de la tabla
    print("{:<20} {:<20} {:<10}".format("Nombre", "Apellidos", "DNI"))
    print("-" * 50)

    # Datos de la tabla
    for nombre, apellidos, dni in resultados:
        print("{:<20} {:<20} {:<10}".format(nombre, apellidos, dni))

def agregar_registro():
    """
    Agrega un nuevo registro a la tabla 'tabla1'.
    """
    mydb = conectar_a_db()
    if mydb is None:
        return

    cursor = mydb.cursor()

    nombre = input("Ingrese el nombre: ")
    apellidos = input("Ingrese los apellidos: ")
    dni = input("Ingrese el DNI: ")

    sql = "INSERT INTO tabla1 (nombre, apellidos, DNI) VALUES (%s, %s, %s)"
    valores = (nombre, apellidos, dni)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Registro agregado exitosamente")

# Bucle principal del programa
while True:
    print("\nMenú:")
    print("1. Mostrar listado")
    print("2. Agregar registro")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        mostrar_listado()
    elif opcion == '2':
        agregar_registro()
    elif opcion == '3':
        break
    else:
        print("Opción inválida")

print("¡Hasta luego!")
