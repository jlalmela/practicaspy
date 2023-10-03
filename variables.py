
""" 
    Varibales y constantes
    ----------------------

    Las variables son contenedores con datos que puede variar, las constantes son contenedores que se mantienen fijos. ejemlo: velocidad_luz = 300000

    Nomenclatura de las variables
    -----------------------------
    No pueden tener espacios. Ejemplo: fecha de nacimiento
    No pueden empezar por un número. Ejemplo: 2email_cliente
    No pueden usar palabras reservadas. Ejemplo: if, while, for, else

    Convenciones de nombres para varibles
    -------------------------------------
    camelCase - ejemplo: fechaDeNacimiento - (primera palabra en minúsculas y el resto de las palabras la primera letra en mayúscula, se utiliza para declarar variables)
    snake_case - ejemplo: fecha_de_nacimiento - (separamos las palabras en minúsculas con un subguión bajo, se utiliza en las bases de datos)
    SCREAMING_SNAKE_CASE - ejemplo: FECHA_DE_NACIMIENTO - (se utiliza a la hora de nombrar constantes)
    kebab-case - ejemplo: fecha-de-nacimiento - (se utiliza bastante en URLs)

    Tipos de variables
    ------------------
    enteros (int) - se utilizan para almacenar números enteros - 
    flotantes (float) - se utilizan para almacenar números con coma flotante o con decimales - pi = 3.1416
    primitivos booleanos  (bool) - se utilizan para almacenar datos binarios - esta_frio = True , es_bajo = False
    string (str) o pueden contener caracteres o cadenas de caracteres de texto o números como texto y se crean entre comillas simpres o dobles - nombre = "Pepe"

    Operadores de comparación
    -------------------------
    == Igual 
    > Mayor 
    < Menor
    >= Mayor igual
    <= Menor igual
    != Distinto  5!= 6f

    Operadores lógicos
    ------------------
    NOT combierte en opuesto cualquier valor de una variable o cadena
    AND compara entre dos datos 
    OR necesita un sólo valor verdadero para funcionar

    Operadores aridméticos
    ----------------------
    Sumar +
    Restar -
    Multiplicar *
    Dividir /
    Resto % - 11 % 3 (calcula el resto de una operación, si por ejemplo dividimos 11 entre 3 hay un resto de 2)


"""

# Variable string
nombre = 'Jose Luis'
print ('mi nombre es ' + nombre)

# La variable edad contiene un número y para mostrarla tenemos que convertirla en texto con str()
edad = 53
print ("mi edad es " + str(edad))

if edad > 18:
    print(nombre + " es mayor de edad")

else:
    print(nombre + " es menor de edad")

#Probamos ahora pidiendo un dato por el teclado

tuedad = int(input('Dime tu edad '))

if tuedad > 18:
    print("eres mayor de edad")

else:
    print("eres menor de edad")

#Probamos el operador resto

num = int(input('introduce un número '))

if num % 2 == 0:
    print("has introducido un número entero")

else:
    print("no has introducido un número entero")
