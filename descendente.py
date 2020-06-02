#ANALIZADOR SINTACTICO DESCENDIENTE PARA AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

from ply import *
import gramatica
from instrucciones import *
from enumeradores import *

tokens = gramatica.TOKENS
precedence = {
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS')
}

def p_S(p):
    '''S: ESTRUCTURAMAIN'''
    print("S->ESTRUCTURAMAIN")

def p_S_error(p):
    '''S: error'''
    p[0] = None
    p.parser.error += 1

def p_ESTRUCTURAMAIN(p):
    '''ESTRUCTURAMAIN: MAIN DOSPUNTOS PRECUERPO'''
    if len(p) == 3:
        p[0] = principal(TIPO_INSTRUCCION.PRINCIPAL,p[3])

def p_ESTRUCTURAMAIN_error(p):
    '''ESTRUCTURAMAIN: error'''
    p[0] = None
    p.parser.error += 1

def p_PRECUERPO(p):
    '''PRECUERPO: PRECUERPO CUERPO
                 |CUERPO'''
    if len(p) == 2:
        p[0].append(p[2])
    elif len(p) == 1:
        p[0] = list()
        p[0].append(p[1])


def p_CUERPO(p):
    '''CUERPO: LABEL
              |GOTO_LABEL
              |ASIGNACION
              |ARREGLOS
              |ESTRUCTURA_IF'''

    p[0] = p[1]


def p_CUERPO_error(p):
    '''CUERPO: error'''
    p[0] = None
    p.parser.error += 1

def p_LABEL(p):
    '''LABEL: ID DOSPUNTOS PRECUERPO'''
    p[0] = bandera(p[1],TIPO_INSTRUCCION.BANDERA,p[3])

def p_LABEL_error(p):
    '''LABEL: error'''
    p[0] = None
    p.parser.error += 1

def p_GOTO_LABEL(p):
    '''GOTO_LABEL: goto ID PTCOMA'''
    p[0] = salto_bandera(TIPO_INSTRUCCION.SALTO_BANDERA,p[2])

def p_GOTO_LABEL_error(p):
    '''GOTO_LABEL: error'''
    p[0] = None
    p.parser.error += 1

parser = yacc.yacc()

def parse(data,debug=0):
    parser.error = 0
    p = parser.parse(data,debug=debug)
    if parser.error:
        return None
    return p
