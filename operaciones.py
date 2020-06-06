#CONSTRUCTORES PARA OPERACIONES, AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

from estructuras import *
from enumeradores import *

class operaciones:
    def descritpion(self):
        print("operaciones aritmeticas, logicas, relacionales para Augus")

    def implements(self):
        print("polimorfismo yeah!")

class valor(operaciones):

    def __init__(self,valor,method,type):
        self.value = valor
        self.metodo = method
        self.tipo = type

    def get_tipo(self):
        return self.tipo

    def get_metodo(self):
        return self.metodo

    def get_Value(self):
        if isinstance(self.value,array_s) and self.metodo == METHOD_VALUE.ARREGLO:
            return self.value.implements
        elif self.metodo == METHOD_VALUE.VARIABLE:
            print('getting value of variable')
        elif self.metodo == METHOD_VALUE.VALOR_UNICO:
            return self.value
        else:
            print('method read has depreceated')


class operacionesAritmeticas(operaciones):

    def __init__(self,tipo_operacion,valorizq,valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("aritmeticas")


class operacionesLogicas(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("Logicas")


class operacionesRelacionales(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("Relacionales")


class operacionesBit(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("Bit a Bit")

