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


def obtainbanderas(instrucciones, lista):
    for inst in instrucciones:
        if isinstance(inst, etiqueta):
            lista.append(inst)
            obtainbanderas(inst.instruccionesd, lista)

    return lista

def semantic(result):
    tablasimbolos = ts()
    pl = pila()
    iniciar = result
    print('-----------------------------[SEMANTICOS]---------------------------------------')
    banderas = obtainbanderas(iniciar.instruccionesd, [])

    m = iniciar.implements(tablasimbolos, pl, banderas)
    if m >0:
        print('--------------------------------------------------------------------')
        simbolos = tablasimbolos.simbolos
        for sm in simbolos:
            print('simbolo: ' + str(sm.id) + '- ' + str(sm.valor) + '- ' + str(sm.registro))

        print('--------------------------------------------------------------------')
        for pls in pl.pila:
            print('pila: ' + str(pls.direccion) + '- ' + str(pls.valor))
    else:
        print("Ah ocurrido un error durante la ejecucion")


file = open("./value.txt", 'r')
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

semantic(result)






