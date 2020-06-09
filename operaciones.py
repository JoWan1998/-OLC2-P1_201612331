#CONSTRUCTORES PARA OPERACIONES, AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

from estructuras import *
from enumeradores import *
from TablaSimbolos import *

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

    def get_Value(self,ts):
        if isinstance(self.value,array_s) and self.metodo == METHOD_VALUE.ARREGLO:
            return self.value.implements
        elif self.metodo == METHOD_VALUE.VARIABLE:
            print('getting value of variable')
            value = ts.getSimbolo(self.value)
            simbolito = simbolo(value.id,value.value,value.tipo,value.registro)
            return simbolito
        elif self.metodo == METHOD_VALUE.VALOR_UNICO:
            value = { 'valor': self.value, 'tipo': self.tipo}
            return value
        elif self.metodo == METHOD_VALUE.APUNTADOR:
            value = ts.getSimbolo(self.value)
            return value
        elif self.metodo == METHOD_VALUE.READ:
            print('reader')
        elif self.metodo == METHOD_VALUE.CONVERSION:
            print('conversion')
        else:
            print('not in')


class operacionesAritmeticas(operaciones):

    def __init__(self,tipo_operacion,valorizq,valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("aritmeticas")

    def get_Value(self,ts):
        print ('aritmeticas')
        valoriz = self.valorizq.get_Value(ts)
        valorder = self.valorder.get_Value(ts)
        if isinstance(valoriz,simbolo):
            tipo = valoriz.tipo
            if isinstance(valorder,simbolo):
                tipo1 = valorder.tipo
                if tipo == TYPE_VALUE.NUMERIC:
                    if tipo1 == TYPE_VALUE.NUMERIC:
                        return valoriz.valor + valorder.valor
                    elif tipo1 == TYPE_VALUE.CHARACTER:
                        return str(valoriz.valor) + valorder.valor



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

