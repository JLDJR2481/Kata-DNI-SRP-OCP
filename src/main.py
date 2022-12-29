from dni import DNI
from letras import Letras

# Funcion que recoge el input del dni desde la terminal


def introducir_dni():
    dni = str(input(
        "Introduce aquí el DNI el cual quieras comprobar su validez y calcular su letra: "))
    mensaje = "El DNI introducido es: {dni}"
    print(mensaje.format(dni=dni))
    return dni


dni = introducir_dni()

# Funcion que comprueba el DNI introducido


def comprobar_dni_introducido():
    if DNI.comprobar_dni(dni) == 'DNI aceptado: Longitud y caracteres correctos':
        return True
    else:
        print(
            'El DNI introducido no cumple con los requisitos para poder calcular su letra')

# Funcion que calcula la letra del DNI


def calcular_letra_dni():
    if comprobar_dni_introducido() == True:
        print('DNI comprobado')
        print('Calculando letra')
        return Letras.calcular_letra(self=dni)

# Función para printar en caso de que el DNI introducido sea correcto


def printar_dni_y_letra():
    if comprobar_dni_introducido() == True:
        letra_asignada = calcular_letra_dni()
        mensaje = "El DNI introducido cumple con todos los requisitos. Aquí tienes la letra que le corresponde es: {letra}"
        print(mensaje.format(letra=letra_asignada))
        mensaje_dni = "El DNI sería: {dni}{letra}"
        print(mensaje_dni.format(dni=dni, letra=letra_asignada))
