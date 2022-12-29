class DNI:

    def __init__(self, cadena=""):
        self.dni = cadena
# Función para comprobar que el dni sea de longitud 8

    def comprobar_long_dni(self):
        error = ""
        if len(self.dni) != 8:
            if len(self.dni) > 8:
                error = 'Error: El DNI está por encima de la longitud reglamentaria'
                return error
            elif len(self.dni) < 8:
                error = 'Error: El DNI está por debajo de la longitud reglamentaria'
                return error
        else:
            return True

# Función para comprobar que la sequencia del dni no tenga ningun caracter no aceptado. Para caracter no aceptado se entiende cualquier letra alfabetica que esté entre los números

    def comprobar_car_dni(self):
        error = ""
        lista_cadena = list(self.dni)
        for i in lista_cadena:
            if i.isdigit():
                continue
            else:
                error = 'Error: Caracteres no aceptados encontrados'
                return error
        return True

# Función que combina las funciones que detectan la longitud y los caracteres

    def comprobar_dni(self):
        if DNI.comprobar_long_dni(self) == True and DNI.comprobar_car_dni(self) == True:
            return 'DNI aceptado: Longitud y caracteres correctos'
        else:
            if DNI.comprobar_long_dni(self) == 'Error: El DNI está por debajo de la longitud reglamentaria':
                return 'Error: El DNI está por debajo de la longitud reglamentaria'
            elif DNI.comprobar_long_dni(self) == 'Error: El DNI está por encima de la longitud reglamentaria':
                return 'Error: El DNI está por encima de la longitud reglamentaria'
            else:
                return 'Error: Caracteres no aceptados encontrados'
