from ascendente import *
from descendente1 import *
from TablaSimbolos import *
from stack import *
from ArbolAscendente import *
from ArbolDescendente import *
from graphviz import Digraph,render
import tempfile

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
    val = "C:\\Windows\\Temp\\salida.txt"
    file = open(val,'w+')
    file.write('')
    print('-----------------------------[SEMANTICOS]---------------------------------------')
    banderas = obtainbanderas(iniciar.instruccionesd, [])

    m = iniciar.implements(tablasimbolos, pl, banderas,file)

    vali = tempfile.mktemp('.txt')
    fil = open(vali,'w+')
    if m >0:
        fil.write('<\n<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n')
        fil.write('<TR><TD COLSPAN=\"5\">TABLA SIMBOLOS</TD></TR>\n')
        fil.write('<TR>')
        fil.write('<TD>DIRECCION</TD>')
        fil.write('<TD>IDENTIFICADOR</TD>')
        fil.write('<TD>VALOR</TD>')
        fil.write('<TD>REGISTRO</TD>')
        fil.write('<TD>TIPO</TD>')
        fil.write('</TR>\n')
        print('--------------------------------------------------------------------')
        simbolos = tablasimbolos.simbolos
        for sm in simbolos:
            print('simbolo: ' + str(sm.id) + '- ' + str(sm.valor) + '- ' + str(sm.registro))
            fil.write('<TR>')
            fil.write('<TD>' + str(sm.direccion) + '</TD>')
            fil.write('<TD>' + str(sm.id) + '</TD>')
            fil.write('<TD>' + str(sm.valor) + '</TD>')
            fil.write('<TD>' + str(sm.registro) + '</TD>')
            fil.write('<TD>' + str(sm.tipo) + '</TD>')
            fil.write('</TR>\n')

        fil.write('</TABLE>\n>')
        fil.close()
        f = open(vali, 'r')
        da = f.read()
        f.close()
        dot = Digraph("TABLA SIMBOLOS", node_attr={'shape': 'plaintext'})
        dot.attr(size='1000,1000')
        dot.node('struct', da)
        dot.render(tempfile.mktemp('.dot'), view=True)

        print('--------------------------------------------------------------------')
        #for pls in pl.pila:
        #    print('pila: ' + str(pls.direccion) + '- ' + str(pls.valor))
        file.write("Executed Finished"+"\n")
    else:
        file.write("Ah ocurrido un error durante la ejecucion, retorno :"+str(m)+"\n")
    file.close()
    del tablasimbolos
    del result

def getDot(padre,cont,contpadre,dot):
        if contpadre == cont:
            father = 'Nodo_' + str(cont)
            dot.node(father, padre.value)
            cont = getDot(padre,cont+1,cont,dot)
        else:
            for p in padre.hijos:
                father = 'Nodo_' + str(contpadre)
                son = 'Nodo_'+str(cont)
                print(p)
                print(p.value)
                dot.node(son,p.value)
                dot.edge(father,son,arrowhead='none')
                cont = getDot(p,cont+1,cont,dot)
                cont += 1
        return cont

def getInfoASCE1(data):
    resul = arparseas(data)
    if resul != None:
        dot = Digraph("ARBOL_ASCENDENTE", "ARBOL_ASCENDENTE")
        dot.attr(size='1000,1000')
        getDot(resul, 0, 0, dot)
        dot.render(tempfile.mktemp('.dot'), view=True)

        val = tempfile.mktemp('.txt')
        #val = './table.txt'
        f = open(val, "w+")
        f.write('<\n<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n')
        resul.createReglaS(resul, f, 0)
        f.write('</TABLE>\n>')
        f.close()

        filetable = open(val, 'r')
        datatable = filetable.read()

        dot = Digraph("DEFINICION_DIRIGIDA_SINTAXIS_ASCENDENTE", "DEFINICION_DIRIGIDA_SINTAXIS_ASCENDENTE",
                      node_attr={'shape': 'plaintext'})
        dot.attr(size='1000,1000')
        dot.node('struct', datatable)
        vv= tempfile.mktemp('.dot')
        dot.render(vv, view=True)

def getInfoDES1(data):
    res = arparsedes(data)

    if res != None:
        dot1 = Digraph("ARBOL_DESCENDENTE")
        dot1.attr(size='1000,1000')
        getDot(res, 0, 0, dot1)
        dot1.render(tempfile.mktemp('.dot'), view=True)

        val = tempfile.mktemp('.txt')
        f = open(val, "w+")
        f.write('<\n<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n')
        res.createReglaS(res, f, 0)
        f.write('</TABLE>\n>')
        f.close()

        filetable = open(val, 'r')
        datatable = filetable.read()

        dot = Digraph("DEFINICION_DIRIGIDA_SINTAXIS_DESCENDENTE", "DEFINICION_DIRIGIDA_SINTAXIS_DESCENDENTE",
                      node_attr={'shape': 'plaintext'})
        dot.attr(size='1000,1000')
        dot.node('struct', datatable)
        dot.render(tempfile.mktemp('.dot'), view=True)

def reportes1(errores):
    print('-----------------------------[LEXICOS]---------------------------------------')
    val = tempfile.mktemp('.txt')
    f = open(val, "w+")
    f.write('<\n<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n')
    lexicos = errores.errores_lexicos
    f.write('<TR><TD COLSPAN=\"4\">ERRORES LEXICOS</TD></TR>\n')
    f.write('<TR>')
    f.write('<TD>LINEA</TD>')
    f.write('<TD>COLUMNA</TD>')
    f.write('<TD>TOKEN</TD>')
    f.write('<TD>VALUE</TD>')
    f.write('</TR>\n')
    for errorsito in lexicos:
        f.write('<TR>')
        f.write('<TD>' + str(errorsito.linea) + '</TD>')
        f.write('<TD>' + str(errorsito.columna) + '</TD>')
        f.write('<TD>' + str(errorsito.token) + '</TD>')
        f.write('<TD>' + errorsito.value + '</TD>')
        f.write('</TR>\n')
        print(errorsito.get_value())
    print('-----------------------------[SINTACTICOS]---------------------------------------')
    f.write('<TR><TD COLSPAN=\"4\">ERRORES SINTACTICOS</TD></TR>\n')
    f.write('<TR>')
    f.write('<TD>LINEA</TD>')
    f.write('<TD>COLUMNA</TD>')
    f.write('<TD>TOKEN</TD>')
    f.write('<TD>VALUE</TD>')
    f.write('</TR>\n')
    sintatico = errores.errores_sintacticos
    for errorsito in sintatico:
        f.write('<TR>')
        f.write('<TD>' + str(errorsito.linea) + '</TD>')
        f.write('<TD>' + str(errorsito.columna) + '</TD>')
        f.write('<TD>' + str(errorsito.token) + '</TD>')
        f.write('<TD>' + errorsito.value + '</TD>')
        f.write('</TR>\n')
        print(errorsito.get_value())
    f.write('</TABLE>\n>')
    f.close()
    f = open(val, 'r')
    da = f.read()

    dot = Digraph("ERRORES", node_attr={'shape': 'plaintext'})
    dot.attr(size='1000,1000')
    dot.node('struct', da)
    dot.render(tempfile.mktemp('.dot'), view=True)

def analisisas(data):
    try:
        errores = errotk.errores()
        result = parseas(errores,data,1)
        reportes1(errores)
        semantic(result)
    except Exception as e:
        val = "C:\\Windows\\Temp\\salida.txt"
        file = open(val, 'w+')
        file.write('Excepcion encontrada de retorno -5, Existen errores no definidos como sintacticos o semanticos.\n')
        file.close()





