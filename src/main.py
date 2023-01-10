from dni import DNI
from tabla import Tabla

# Funcion que recoge el input del dni desde la terminal


def introducir_dni():
    dni = str(input(
        "Introduce aquí el DNI el cual quiera comprobar su validez y calcular su letra: "))
    mensaje = "El DNI introducido es: {dni}"
    print(mensaje.format(dni=dni))
    return dni


dni = introducir_dni()

# Funcion que comprueba el DNI introducido


def comprobar_dni_introducido():
    error = ""
    if DNI.comprobar_dni(dni) == 'DNI aceptado: Longitud y caracteres correctos':
        return True
    else:
        msg = "El DNI introducido no cumple con los requisitos para poder calcular su letra"

        if DNI.comprobar_long_dni(dni) == 'Error: El DNI está por encima de la longitud reglamentaria':
            error = 'El DNI introducido sobrepasa la longitud reglamentaria'

        elif DNI.comprobar_long_dni(dni) == 'Error: El DNI está por debajo de la longitud reglamentaria':
            error = 'El DNI introducido tiene una longitud por debajo de lo reglamentario'

        elif DNI.comprobar_car_dni(dni) == 'Error: Caracteres no aceptados encontrados':
            error = 'Se ha encontrado caracteres alfabético no aceptados'

        else:
            error = 'Error. Introduzca de nuevo el DNI'

        print(msg)
        print(error)


# Funcion que calcula la letra del DNI


def calcular_letra_dni():
    print('DNI comprobado')
    print('Calculando letra')
    return Tabla.calcular_letra(dni)

# Función para printar en caso de que el DNI introducido sea correcto


def printar_dni_y_letra():
    if comprobar_dni_introducido() == True:
        letra_asignada = calcular_letra_dni()
        mensaje = "El DNI introducido cumple con todos los requisitos. Aquí tiene la letra que le corresponde: {letra}"
        print(mensaje.format(letra=letra_asignada))
        mensaje_dni = "El DNI es: {dni}{letra}"
        print(mensaje_dni.format(dni=dni, letra=letra_asignada))


printar_dni_y_letra()
