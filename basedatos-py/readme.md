# Gestión de una base de datos de contactos en Python

## Descripción
Este script en Python permite interactuar con una base de datos de contactos de forma sencilla. Las principales funcionalidades son:

* **Conexión a la base de datos:** Se establece una conexión con una base de datos MySQL local.
* **Mostrar listado de contactos:** Presenta los contactos almacenados en la base de datos en un formato tabular, facilitando su visualización.
* **Agregar nuevos contactos:** Permite introducir nuevos contactos a la base de datos.

## Requisitos
* **Python:** Asegúrate de tener instalado Python en tu sistema.
* **MySQL:** Necesitarás tener un servidor MySQL configurado y una base de datos creada.
* **Conector Python para MySQL:** Instala este paquete utilizando `pip install mysql-connector-python`.

## Estructura del proyecto
* **`script.py`:** Contiene el código principal del programa.
* **`README.md`:** Este archivo.

## Uso
1. **Clona el repositorio** (si estás utilizando un sistema de control de versiones como Git).
2. **Instala las dependencias:** Ejecuta `pip install -r requirements.txt` (si tienes un archivo `requirements.txt` con las dependencias).
3. **Edita la conexión a la base de datos:** Modifica la función `conectar_a_db()` para que coincida con los datos de tu base de datos.
4. **Ejecuta el script:** Ejecuta el script desde la línea de comandos: `python script.py`.
5. **Sigue las instrucciones:** El programa te presentará un menú con las opciones disponibles.

## Funcionalidades
* **Mostrar listado:** Muestra todos los contactos almacenados en la base de datos en un formato tabular.
* **Agregar contacto:** Permite añadir nuevos contactos a la base de datos solicitando los datos necesarios (nombre, apellidos, DNI).

## Ampliaciones posibles
* **Buscar contactos:** Implementar una función para buscar contactos por nombre, apellidos o DNI.
* **Editar contactos:** Permitir modificar los datos de un contacto existente.
* **Eliminar contactos:** Eliminar un contacto de la base de datos.
* **Exportar a CSV:** Exportar los datos a un archivo CSV para su análisis en hojas de cálculo.
* **Interfaz gráfica:** Crear una interfaz gráfica más amigable utilizando bibliotecas como Tkinter o PyQt.

## Consideraciones
* **Seguridad:** Evita almacenar contraseñas en claro en el código. Utiliza variables de entorno o archivos de configuración para gestionar las credenciales de la base de datos.
* **Validación de datos:** Implementa validaciones para asegurar que los datos ingresados por el usuario sean correctos y consistentes.
* **Escalabilidad:** Si esperas una gran cantidad de datos, considera optimizar las consultas SQL y utilizar índices para mejorar el rendimiento.

## Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request en el repositorio.

**¡Gracias por usar este script!**

### **Personalización**

* **Reemplaza** "script.py" con el nombre real de tu archivo Python.
* **Adapta** la descripción y las funcionalidades a tu proyecto específico.
* **Agrega** secciones sobre la estructura de la base de datos, ejemplos de uso, etc.
* **Utiliza** Markdown para darle formato al texto (negrita, cursiva, listas, encabezados, etc.).
* **Incorpora** capturas de pantalla o diagramas para ilustrar el funcionamiento del programa.

**Este README.md te servirá como punto de partida para documentar tu proyecto y facilitar su comprensión tanto para ti como para otros desarrolladores.**

**¿Quieres que te ayude a personalizar este README.md aún más?**
