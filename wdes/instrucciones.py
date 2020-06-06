#definicion de clases para implementacion de AUGUS
#Jose Wannan @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
from AST import Nodo

class instruccion:
    def information(self):

        self.information = "instruccion of augus"

class etiqueta(instruccion):

    def __init__(self,enum,nombre,linea, instrucciones=list,principal=False):
        self.tipo_intruccion = enum
        self.nombre = nombre
        self.linea = linea
        self.instruccionesd = instrucciones
        self.principal = principal

    def implements(self):
        print("bandera")

class salto_bandera(instruccion):

    def __init__(self, enum, linea,bandera):
        self.tipo_instruccion = enum
        self.bandera = bandera
        self.linea = linea

    def implements(self):
        print("salto_bandera")

class asignacion(instruccion):

    def __init__(self,enum,linea,variable,valor,pos=-1):
        self.tipo_instruccion = enum
        self.linea = linea
        self.variable = variable
        self.valor = valor
        self.pos = pos

    def implements(self):
        print("asignacion")

class sentencia_control(instruccion):

    def __init__(self,enum,linea,condicion,bandera):
        self.tipo_instruccion = enum
        self.condicion = condicion
        self.bandera = bandera
        self.linea = linea

    def implements(self):
        print("sentencia de control")

class destructor(instruccion):

    def __init__(self,enum,linea,variable):
        self.tipo_instruccion = enum
        self.variable = variable
        self.linea = linea

    def implements(self):
        print("destructor")

class imprimir(instruccion):

    def __init__(self,enum,linea,valor):
        self.tipo_instruccion = enum
        self.valor = valor
        self.linea = linea

    def implements(self):
        print("imprimir")

class salida(instruccion):

    def __init__(self,enum,linea):
        self.tipo_instruccion = enum
        self.linea = linea

    def implements(self):
        print("Adios")


