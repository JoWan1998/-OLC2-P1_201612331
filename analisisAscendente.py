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
from ArbolAscendente import *
from ArbolDescendente import *
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


def obtainbanderas(instrucciones, lista):
    for inst in instrucciones:
        if isinstance(inst, etiqueta):
            lista.append(inst)
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
        #simbolos = tablasimbolos.simbolos
        #for sm in simbolos:
        #    print('simbolo: ' + str(sm.id) + '- ' + str(sm.valor) + '- ' + str(sm.registro))

        print('--------------------------------------------------------------------')
        #for pls in pl.pila:
        #    print('pila: ' + str(pls.direccion) + '- ' + str(pls.valor))
        print("Executed Finished")
    else:
        print("Ah ocurrido un error durante la ejecucion")

def getDot(padre,cont,contpadre,dot):
        if contpadre == cont:
            father = 'Nodo_' + str(cont)
            dot.node(father, padre.value)
            cont = getDot(padre,cont+1,cont,dot)
        else:
            for p in padre.hijos:
                father = 'Nodo_' + str(contpadre)
                son = 'Nodo_'+str(cont)
                dot.node(son,p.value)
                dot.edge(father,son,arrowhead='none')
                cont = getDot(p,cont+1,cont,dot)
                cont += 1
        return cont

file = open("./value1.txt", 'r')
data = file.read()
errores = errotk.errores()
#result = parseas(errores,data,1)
resul = arparseas(data)
res = arparsedes(data)
if resul != None:
    dot = Digraph("ARBOL_ASCENDENTE","ARBOL_ASCENDENTE")
    dot.attr(size='1000,1000')
    #f= open("./arbolascendente.txt","w+")
    #f.write('digraph G {\n')
    #f.write('size="100,100";\n')
    #resul.getData(resul,0,f)
    #f.write('}')
    #f.close()
    getDot(resul,0,0,dot)
    dot.render('test-output/ARBOL_ASCENDENTE.dot',view=True)
if res != None:

    dot1 = Digraph("ARBOL_DESCENDENTE")
    dot1.attr(size='1000,1000')
    #f= open("./arbolascendente.txt","w+")
    #f.write('digraph G {\n')
    #f.write('size="100,100";\n')
    #resul.getData(resul,0,f)
    #f.write('}')
    #f.close()
    getDot(res,0,0,dot1)
    dot1.render('test-output/ARBOL_DESCENDENTE.dot',view=True)

print('-----------------------------[LEXICOS]---------------------------------------')
lexicos = errores.errores_lexicos
for errorsito in lexicos:
    print(errorsito.get_value())
print('-----------------------------[SINTACTICOS]---------------------------------------')
sintatico = errores.errores_sintacticos
for errorsito in sintatico:
    print(errorsito.get_value())
#semantic(result)






