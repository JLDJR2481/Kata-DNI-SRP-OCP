class Letras:
    tabla = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
             'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    length = [*range(0, len(tabla))]
    diccionarioLetras = dict(zip(length, tabla))

    def __init__(self, cadena):
        self.cadena = str(cadena)

    def calcularLetra(self):
        if len(self.cadena) == 8:
            self.cadena = int(self.cadena)
            try:
                return Letras.diccionarioLetras[self.cadena % len(Letras.tabla)]
            except:
                'Error calculando la letra'
        else:
            return 'El DNI no cumple la longitud obligatoria de 8 digitos'
