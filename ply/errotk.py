


class error:
    def __init__(self, linea, value, columna, token):
        self.linea = linea
        self.value = value
        self.columna = columna
        self.token = token

    def get_value(self):
        return self.value

class errores:


    def __init__(self):
        self.errores_sintacticos = []
        self.errores_lexicos = []
        self.errores_semanticos = []


    def addSintactico(self,value,linea,columna,token):
            self.errores_sintacticos.append(error(linea,value,columna,token))

    def addSemantico(self, value, linea,columna,token):
        self.errores_semanticos.append(error(linea,value,columna,token))

    def addLexico(self, value, linea,columna,token):
        self.errores_lexicos.append(error(linea,value,columna,token))