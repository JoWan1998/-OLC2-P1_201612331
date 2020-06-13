#definicion de enumeradores necesarios para la implementacion de AUGUS
#José Wannan, @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
from enum import Enum

class TIPO_INSTRUCCION(Enum):
    BANDERA = 1
    SALTO_BANDERA = 2
    ASIGNACION = 3
    DESTRUCTOR = 4
    IMPRIMIR = 5
    SALIDA = 6
    IFCONTROL = 7

class OPERACION_ARITMETICA(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    RESIDUO = 5
    ABSOLUTO = 6
    NEGATIVO = 7

class OPERACION_LOGICA(Enum):
    NOT = 1
    AND = 2
    OR = 3
    XOR = 4

class OPERACION_RELACIONAL(Enum):
    EQUALS = 1
    NOTEQUALS = 2
    MAYOR_EQUALS = 3
    MENOR_EQUALS = 4
    MAYOR = 5
    MENOR = 6

class OPERACION_BIT(Enum):
    NOTB = 1
    ANDB = 2
    ORB = 3
    XORB = 4
    SHIFTA = 5
    SHIFTB = 6

class ARRAY_METHOD(Enum):
    INSTANCIA = 1
    GET = 2
    SET = 3
    
class TYPE_VALUE(Enum):
    NUMERIC = 1
    FLOAT = 5
    CHARACTER = 2
    ARREGLO = 3
    APUNTADOR = 4

class METHOD_VALUE(Enum):
    VARIABLE = 1
    ARREGLO = 2
    VALOR_UNICO = 3
    READ  = 4
    CONVERSION = 5
    APUNTADOR = 6

class REGISTRO(Enum):
    TEMPORAL = 1
    PARAMETRO = 2
    RETORNO = 3
    PILA = 4
    APUNTADORPILA = 5
    RA = 6
    FUNCION = 7
    APUNTADOR = 8

####################################STACK##########################3
##### [direccion, valor]
####### [0x001, valor: { "valor": value}]


##########################TABLA DE SIMBOLOS#########################
##### [direccion, id, valor, tipo, registro] ->
# tipo -> nunerico, caracter, arreglo, apuntador
# direccion -> direccion de memoria de la variable

###variable
##  direccion: 0x000, id: t0, valor: 12, tipo: numerico, registro: temporal
##  direccion: 0x003, id: t3, valor: 'a', tipo: caracter, registro: parametro

###apuntador
## direccion: 0x001, id: t1, valor: 0x000, tipo: apuntador, registro: retorno

###arreglo
## direccion: 0x002, id: t2, valor: 0x001, tipo: arreglo, registro: pila

