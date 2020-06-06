from ply import *
import gramatica
from instrucciones import *
from enumeradores import *
from operaciones import *
from estructuras import *
from ascendente import *
from ply import *
from descendente1 import *
from wdes import *

file = open("./EJEMPLO_ENTRADA.txt",'r')
data = file.read()

errores = errotk.errores()
result = parsedes(errores,data,1)
print("------------[LEXICOS]-----------------")
lexicos = errores.errores_lexicos
for errorsito in lexicos:
     print(errorsito.get_value())
print("----------[SINTACTICO]-----------------")
sintatico = errores.errores_sintacticos
for errorsito in sintatico:
     print(errorsito.get_value())

def analisis_ascendente(data):
    errores = errotk.errores()

    result = parseas(errores,data,1)
    print("------------[LEXICOS]-----------------")
    lexicos = errores.errores_lexicos
    for errorsito in lexicos:
        print(errorsito.get_value())
    print("----------[SINTACTICO]-----------------")
    sintatico = errores.errores_sintacticos
    for errorsito in sintatico:
        print(errorsito.get_value())






