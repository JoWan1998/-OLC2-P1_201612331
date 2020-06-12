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
from stack import *


file = open("./value1.txt", 'r')
data = file.read()
errores = errotk.errores()
result = parseas(errores,data,1)
print('-----------------------------[LEXICOS]---------------------------------------')
lexicos = errores.errores_lexicos
for errorsito in lexicos:
    print(errorsito.get_value())
print('-----------------------------[SINTACTICOS]---------------------------------------')
sintatico = errores.errores_sintacticos
for errorsito in sintatico:
    print(errorsito.get_value())

tablasimbolos = ts()
pl = pila()
iniciar = result
print('-----------------------------[SEMANTICOS]---------------------------------------')
iniciar.implements(tablasimbolos,pl)

print('--------------------------------------------------------------------')
simbolos = tablasimbolos.simbolos
for sm in simbolos:
    print('simbolo: '+str(sm.id) + '- ' + str(sm.valor) + '- ' +str(sm.registro))

print('--------------------------------------------------------------------')
for pls in pl.pila:
    print('pila: '+str(pls.direccion) + '- ' + str(pls.valor) )






