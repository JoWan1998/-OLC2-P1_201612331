


class error:
    def __init__(self, linea, value):
        self.linea = linea
        self.value = value

class errores:


    def __init__(self):
        self.errores_sintacticos = []
        self.errores_lexicos = []
        self.errores_semanticos = []


    def addSintactico(self,value,linea):
            self.errores_sintacticos.append(error(linea,value))

    def addSemantico(self, value, linea):
        self.errores_semanticos.append(error(linea,value))

    def addLexico(self, value, linea):
        self.errores_lexicos.append(error(linea,value))