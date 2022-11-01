# Ejemplo calculadora de indice de masa corporal
# IMC = Peso / (Altura x Altura)
# < 19: demasiado delgado
# entre 20 y 25: peso normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad

peso = int(input('Inserte su kg: '))
alturaEnCM = int(input('Ingrese su altura en cm: '))
alturaEnMetros = alturaEnCM / 100
imc = peso / (alturaEnMetros * alturaEnMetros)

print('Su IMC es de ' + str(imc))

if imc < 20:
    print('Demasiado delgado')
if imc >= 20 and imc < 26:
    print('Peso normal')
if imc >= 26 and imc < 30:
    print('Sobrepeso')
if imc >= 30:
    print('Tiene obesidad')