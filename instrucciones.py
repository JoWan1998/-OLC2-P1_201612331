#definicion de clases para implementacion de AUGUS
#Jose Wannan @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
from enumeradores import *

class instruccion:
    def information(self):
        self.information = "instruccion of augus"

class principal(instruccion):

    def __init__(self, enum, instrucciones = []):
        self.tipo_instruccion = enum
        self.instrucciones = instrucciones

    def implements(self):
        print("menu principal")

class bandera(instruccion):

    def __init__(self, nombre,enum, instrucciones=[]):
        self.tipo_intruccion = enum
        self.nombre = nombre
        self.instrucciones = instrucciones

    def implements(self):
        print("bandera")

class salto_bandera(instruccion):

    def __init__(self, enum, bandera):
        self.tipo_instruccion = enum
        self.bandera = bandera

    def implements(self):
        print("salto_bandera")

class asignacion(instruccion):

    def __init__(self,enum,variable,valor):
        self.tipo_instruccion = enum
        self.variable = variable
        self.valor = valor

    def implements(self):
        print("asignacion")

class destructor(instruccion):

    def __init__(self,enum,variable):
        self.tipo_instruccion = enum
        self.variable = variable

    def implements(self):
        print("destructor")

class imprimir(instruccion):

    def __init__(self,enum,valor):
        self.tipo_instruccion = enum
        self.valor = valor

    def implements(self):
        print("imprimir")

class salida(instruccion):

    def __init__(self,enum):
        self.tipo_instruccion = enum

    def implements(self):
        print("Adios")


