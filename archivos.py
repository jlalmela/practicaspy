#Trabajamos con lectura y escritura de archivos, ejemplo de encriptar y desencriptar un texto y guardarlo en un archivo

def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra) # convierte la letra en código ASCII
        ascii += 1
        textoFinal += chr(ascii) # hace lo inverso y convierte en letra el número
    return textoFinal

def desencriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra) # convierte la letra en código ASCII
        ascii -= 1
        textoFinal += chr(ascii) # hace lo inverso y convierte en letra el número
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto =archivo.read()
    archivo.close()
    textoEncriptado= encriptar(texto)

    archivo = open(rutaArchivo, 'w') 
    archivo.write(textoEncriptado)
    archivo.close()
    print('El archivo se encriptó correctamente')

def desencriptarArchivo(rutaArchivo):
    archivo= open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado= desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print('El archivo se desencripto correctamente')

respuestaEoD = input('Presione "E" para enciptar o "D" para desencriptar: ')

if respuestaEoD == "E" or respuestaEoD == "e":
    rutaArchivo = input('Ingrese la ruta del archivo: ')
    encriptarArchivo(rutaArchivo)
elif respuestaEoD == "D" or respuestaEoD == "d":
    rutaArchivo = input('Ingrese la ruta del archivo: ')
    desencriptarArchivo(rutaArchivo)
else:
    print('No ha escrito E o D correctamente vuelva a intentarlo')

