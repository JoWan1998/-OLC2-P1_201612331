#definicion de enumeradores necesarios para la implementacion de AUGUS
#José Wannan, @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
from enum import Enum

class TIPO_INSTRUCCION(Enum):
    PRINCIPAL = 0
    BANDERA = 1
    SALTO_BANDERA = 2
    ASIGNACION = 3
    DESTRUCTOR = 4
    IMPRIMIR = 5
    SALIDA = 6

class OPERACION_ARITMETICA(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    RESIDUO = 5
    ABSOLUTO = 6




