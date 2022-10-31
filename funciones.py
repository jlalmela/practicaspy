# Practiquemos con funciones, creamos nuestra propia función descuento de precio

nomProducto = input("Introduce el producto: ")
impProducto = int(input("Introduce el importe: "))
desProducto = int(input("Introduce el descuento a aplicar: "))


def calDescuento(precio, descuento):
    precioFinal = (precio - descuento * precio / 100)
    return precioFinal


calDescuento(impProducto, desProducto)

print("El descuento para " + nomProducto + " es de "+ str(calDescuento(impProducto, desProducto)))
