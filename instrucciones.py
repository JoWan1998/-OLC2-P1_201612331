#definicion de clases para implementacion de AUGUS
#Jose Wannan @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
from AST import Nodo
from TablaSimbolos import *
from enumeradores import *

class instruccion:
    def information(self):

        self.information = "instruccion of augus"

class etiqueta(instruccion):

    def __init__(self,enum,nombre,linea, instrucciones=[],principal=False):
        self.tipo_intruccion = enum
        self.nombre = nombre
        self.linea = linea
        self.instruccionesd = instrucciones
        self.principal = principal

    def implements(self,ts):
        print("bandera")
        for intruccion in self.instruccionesd:
            if isinstance(intruccion,asignacion):
                intruccion.implements(ts)

class salto_bandera(instruccion):

    def __init__(self, enum, bandera,linea):
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

    def implements(self,ts):
        print("asignacion")
        simbol = ts.getSimbolo(self.variable)
        if simbol == None:
            value = self.valor.get_Value(ts)
            if value != None:
                if isinstance(value,simbolo):
                    ts.insertSimbolo(value)
                    print(simbolo)
                else:
                    tipo = self.variable[0:1]
                    registro = None
                    if  tipo == 't':
                        registro = REGISTRO.TEMPORAL
                    elif tipo == 'a':
                        registro = REGISTRO.PARAMETRO
                    elif tipo == 'v':
                        registro = REGISTRO.FUNCION
                    elif tipo == 'r':
                        registro = REGISTRO.RA
                    elif tipo == 's':
                        tipo = self.variable[1:2]
                        if tipo == 'p':
                            registro = REGISTRO.APUNTADORPILA
                        else:
                            registro = REGISTRO.PILA

                    simbolito = simbolo(self.variable,value['valor'],value['tipo'],registro)
                    ts.insertSimbolo(simbolito)
                    print(simbolito)
            else:
                print('Semantic Error, No se puede asignar el valor a la variable, es probable no exista, linea: '+str(self.linea))
        else:
            value = self.valor.get_Value(ts)
            if isinstance(value, simbolo):
                if simbol.tipo != TYPE_VALUE.ARREGLO and simbol.tipo != TYPE_VALUE.APUNTADOR:
                    ts.update(self.variable,value.valor)
                elif simbol.tipo == TYPE_VALUE.ARREGLO:
                    print('arreglo')
                elif simbol.tipo == TYPE_VALUE.APUNTADOR:

                print(simbolo)
            else:
                ts.update(self.variable, value['valor'])

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


