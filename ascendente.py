#ANALIZADOR SINTACTICO ASCENDENTE PARA AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

from ply import *
import gramatica
from instrucciones import *
from enumeradores import *
from operaciones import *
from array import *

tokens = gramatica.TOKENS
precedence = {
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'RESIDUO')
}

def p_S(p):
    '''S: ESTRUCTURAMAIN'''
    print("S->ESTRUCTURAMAIN")
    p[0] = p[1]

def p_S_error(p):
    '''S: error'''
    p[0] = None
    p.parser.error += 1

def p_ESTRUCTURAMAIN(p):
    '''ESTRUCTURAMAIN: main DOSPUNTOS PRECUERPO'''
    print('estructuramain.eval = precuerpo.eval')
    p[0] = etiqueta("main",TIPO_INSTRUCCION.PRINCIPAL,p[3],True)

def p_ESTRUCTURAMAIN_error(p):
    '''ESTRUCTURAMAIN: error'''
    p[0] = None
    p.parser.error += 1

def p_PRECUERPO(p):
    '''PRECUERPO: PRECUERPO CUERPO'''
    print('precuerpo.eval = precuerpo.eval + cuerpo.eval')
    p[1].append(p[2])
    p[0] = p[1]

def p_PRECUERPO_CUERPO(p):
    '''PRECUERPO: CUERPO'''
    print('precuerpo.eval = cuerpo.eval')
    p[0] = [p[1]]

def p_CUERPO(p):
    '''CUERPO: ETIQUETA
              |GOTO_LABEL
              |ASIGNACION
              |DESTRUYE_VARIABLE
              |IMPRIME
              |ESTRUCTURA_IF'''
    print('cuerpo.eval = value.eval')
    p[0] = p[1]

def p_CUERPO_error(p):
    '''CUERPO: error'''
    p[0] = None
    p.parser.error += 1

def p_ETIQUETA(p):
    '''ETIQUETA: ID DOSPUNTOS PRECUERPO'''
    print('label.eval = precuerpo.eval')
    p[0] = etiqueta(p[1],TIPO_INSTRUCCION.BANDERA,p[3])

def p_LABEL_error(p):
    '''LABEL: error'''
    p[0] = None
    p.parser.error += 1

def p_GOTO_LABEL(p):
    '''GOTO_LABEL: goto ID PTCOMA'''
    print('goto_label.eval = ID')
    p[0] = salto_bandera(TIPO_INSTRUCCION.SALTO_BANDERA,p[2])

def p_GOTO_LABEL_error(p):
    '''GOTO_LABEL: error'''
    p[0] = None
    p.parser.error += 1

def p_ASIGNACION(p):
    '''ASIGNACION: NORMAL
                  |ARRAY'''
    print('asignacion.eval = value.eval')
    p[0] = p[1]

def p_ASIGNACION_error(p):
    '''ASIGNACION: error'''
    p[0] = None
    p.parser.error +=1

def p_NORMAL(p):
    '''NORMAL: VARIABLE IGUAL EXPRESION'''
    print('normal.eval =  VARIABLE + expresion.eval')
    p[0] = asignacion(TIPO_INSTRUCCION.ASIGNACION,p[1],p[3])

def p_ARRAY(p):
    '''ARRAY: VARIABLE CORA EXPRESION CORB IGUAL EXPRESION'''
    print('array.eval = VARIABLE.eval + EXPRESION.eval + EXPRESION.eval')
    p[0] = asignacion(TIPO_INSTRUCCION.ASIGNACION,p[1],p[6],p[3])

def p_NORMAL_error(p):
    '''NORMAL: error'''
    p[0] = None
    p.parser.error += 1

def p_ARRAY_error(p):
    '''ARRAY: error'''
    p[0] = None
    p.parser.error += 1

def p_EXPRESION(p):
    '''EXPRESION: VALOR'''
    print('expresion.eval = value.eval')
    p[0] = p[1]

def p_VALOR_VARIABLE(p):
    '''VALOR: VARIABLE'''
    print('valor.eval = variable.eval')
    p[0] = valor(p[1],METHOD_VALUE.VARIABLE,None)

def p_VALOR_LLAMADA_ARREGLO(p):
    '''VALOR: LLAMADA_ARREGLO'''
    print('valor.eval = llamada_arreglo.eval')
    p[0] = p[1]

def p_LLAMADA_ARREGLO(p):
    '''LLAMADA_ARREGLO: VARIABLE CORA EXPRESION CORB '''
    print('llamada_arreglo: variable + expresion.eval')
    arreglo = array_s(ARRAY_METHOD.GET,None,variable=p[1],posicion=p[3])
    p[0] = valor(arreglo,METHOD_VALUE.ARREGLO,None)

def p_VALOR_NUMERO(p):
    '''VALOR: INT'''
    print('valor.eval = INT')
    p[0] = valor(p[1],METHOD_VALUE.VALOR_UNICO,TYPE_VALUE.NUMERIC)

def p_VALOR_FLOAT(p):
    '''VALOR: FLOAT'''
    print('valor.eval = FLOAT')
    p[0] = valor(p[1],METHOD_VALUE.VALOR_UNICO,TYPE_VALUE.NUMERIC)

def p_VALOR_CARACTER(p):
    '''VALOR: CHAR'''
    print('valor.eval = CHAR')
    p[0] = valor(p[1],METHOD_VALUE.VALOR_UNICO,TYPE_VALUE.CHARACTER)

def p_VALOR_NUEVO_ARREGLO(p):
    '''VALOR: array PARA PARB'''
    print('valor.eval = array')
    arreglo = array_s(ARRAY_METHOD.INSTANCIA,list)
    p[0] = valor(arreglo,METHOD_VALUE.ARREGLO,TYPE_VALUE.ARREGLO)

def p_VALOR_LEER(p):
    '''VALOR: read PARA PARB'''
    print('valor.eval = read')

def p_EXPRESION_ARITMETICAS(p):
    '''EXPRESION: ARITMETICAS'''
    p[0] = p[1]

def p_ARITMETICAS_NEGATIVO(p):
    '''ARITMETICAS: MENOS VALOR'''
    p[0]= operacionesAritmeticas(OPERACION_ARITMETICA.NEGATIVO,p[2],None)

def p_ARITMETICAS(p):
    '''ARITMETICAS: VALOR MAS VALOR
                   |VALOR MENOS VALOR
                   |VALOR MULTIPLICACION VALOR
                   |VALOR DIVIDIR VALOR
                   |VALOR RESIDUO VALOR'''

    if p[2] == '+':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.SUMA,p[1],p[3])
    elif p[2] == '-':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.RESTA,p[1],p[3])
    elif p[2] == '*':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.MULTIPLICACION, p[1], p[3])
    elif p[2] == '/':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.DIVISION, p[1], p[3])
    elif p[2] == '%':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.RESIDUO, p[1], p[3])

def p_ARITMETICAS_ABS(p):
    '''ARITMETICAS: abs PARA VALOR PARB'''
    p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.ABSOLUTO,p[3],None)

def p_EXPRESION_LOGICAS(p):
    '''EXPRESION: LOGICAS'''
    p[0] = p[1]

def p_LOGICAS_NOT(p):
    '''LOGICAS: NOTL VALOR'''
    p[0] = operacionesLogicas(OPERACION_LOGICA.NOT,p[2],None)

def p_LOGICAS(p):
    '''LOGICAS: VALOR ANDL VALOR
               |VALOR ORL VALOR
               |VALOR XORL VALOR'''

    if p[2] == '&&':
        p[0] = operacionesLogicas(OPERACION_LOGICA.AND, p[1], p[3])
    elif p[2] == '||':
        p[0] = operacionesLogicas(OPERACION_LOGICA.OR, p[1], p[3])
    elif p[2] == 'xor':
        p[0] = operacionesLogicas(OPERACION_LOGICA.XOR, p[1], p[3])

def p_EXPRESION_RELACIONAL(p):
    '''EXPRESION: RELACIONAL'''
    p[0] = p[1]

def p_RELACIONAL(p):
    '''RELACIONAL: VALOR IGUALR VALOR
                  |VALOR NOIGUALR VALOR
                  |VALOR MAYORIGUAL VALOR
                  |VALOR MENORIGUAL VALOR
                  |VALOR MAYORR VALOR
                  |VALOR MENORR VALOR'''

    if p[2] == '==':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.EQUALS, p[1], p[3])
    elif p[2] == '!=':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.NOTEQUALS, p[1], p[3])
    elif p[2] == '>=':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.MAYOR_EQUALS, p[1], p[3])
    elif p[2] == '<=':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.MENOR_EQUALS, p[1], p[3])
    elif p[2] == '>':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.MAYOR, p[1], p[3])
    elif p[2] == '<':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.MENOR, p[1], p[3])

def p_EXPRESION_BIT(p):
    '''EXPRESION: BIT'''
    p[0] = p[1]

def p_BIT_NOT(p):
    '''BIT: NOTB VALOR'''
    p[0] = operacionesBit(OPERACION_BIT.NOTB,p[2],None)

def p_BIT(p):
    '''BIT: VALOR ANDB VALOR
           |VALOR ORB VALOR
           |VALOR XORB VALOR
           |VALOR SHIFTA VALOR
           |VALOR SHIFTB VALOR'''
    if p[2] == '&':
        p[0] = operacionesBit(OPERACION_BIT.ANDB, p[1], p[3])
    elif p[2] == '|':
        p[0] = operacionesBit(OPERACION_BIT.ORB, p[1], p[3])
    elif p[2] == '^':
        p[0] = operacionesBit(OPERACION_BIT.XORB, p[1], p[3])
    elif p[2] == '<<':
        p[0] = operacionesBit(OPERACION_BIT.SHIFTA, p[1], p[3])
    elif p[2] == '>>':
        p[0] = operacionesBit(OPERACION_BIT.SHIFTB, p[1], p[3])



parser = yacc.yacc()

def parse(data,debug=0):
    parser.error = 0
    p = parser.parse(data,debug=debug)
    if parser.error:
        return None
    return p
