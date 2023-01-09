class Letras:
    tabla = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
             'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    length = [*range(0, len(tabla))]
    diccionarioLetras = dict(zip(length, tabla))

    def __init__(self, cadena):
        self.dni = str(cadena)

    @staticmethod
    def calcular_letra(self):
        if len(str(self)) == 8:
            cadena = int(self)
            try:
                return Letras.diccionarioLetras[cadena % len(Letras.tabla)]
            except:
                'Error calculando la letra'
        else:
            return 'El DNI no cumple la longitud obligatoria de 8 digitos'
