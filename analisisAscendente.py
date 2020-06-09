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
from TablaSimbolos import *
from pila import *


file = open("./EJEMPLO_ENTRADA.txt", 'r')
data = file.read()
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
print(result)

tablasimbolos = ts()
iniciar = result
iniciar.implements(tablasimbolos)

simbolos = tablasimbolos.simbolos
for sm in simbolos:
    print(sm.id)
    print(sm.valor)
    print(sm.direccion)






