# ANALIZADOR SINTACTICO ASCENDENTE PARA AUGUS
# JOSE WANNAN @2020
# UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

from ply import *
import gramatica
from instrucciones import *
from operaciones import *
from estructuras import *

caracteres = 0


def format_result(r):
    repr_str = repr(r)
    if '\n' in repr_str:
        repr_str = repr(repr_str)
    if len(repr_str) > 40:
        repr_str = repr_str[:40] + ' ...'
    result = '<%s @ 0x%x> (%s)' % (type(r).__name__, id(r), repr_str)
    return repr_str


def format_results(r):
    repr_str = repr(r)
    if '\n' in repr_str:
        repr_str = repr(repr_str)
    if len(repr_str) > 40:
        repr_str = repr_str[:40] + ' ...'
    result = '<%s @ 0x%x> (%s)' % (type(r).__name__, id(r), repr_str)
    return result


tokens = gramatica.tokens
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVIDIR'),
    ('left', 'RESIDUO')
)


def p_S(p):
    'S : ESTRUCTURAMAIN'
    # print("S->ESTRUCTURAMAIN")

    p[0] = p[1]


def p_S_error(p):
    'S : error'
    p[0] = None
    p.parser.error += 1


def p_ESTRUCTURAMAIN(p):
    'ESTRUCTURAMAIN : main DOSPUNTOS PRECUERPO'
    # print('estructuramain.eval = precuerpo.eval')
    p[0] = etiqueta(TIPO_INSTRUCCION.BANDERA,"main",p.lexer.lineno , p[3], True)


def p_ESTRUCTURAMAIN_ERROR1(p):
    'ESTRUCTURAMAIN : error DOSPUNTOS PRECUERPO'
    p[0] = None
    p.parser.error += 1


def p_ESTRUCTURAMAIN_ERROR2(p):
    'ESTRUCTURAMAIN : main error PRECUERPO'
    p[0] = None
    p.parser.error += 1


def p_ESTRUCTURAMAIN_ERROR3(p):
    'ESTRUCTURAMAIN : main DOSPUNTOS error'
    p[0] = None
    p.parser.error += 1


def p_PRECUERPO(p):
    'PRECUERPO : PRECUERPO CUERPO'
    # print('precuerpo.eval = precuerpo.eval + cuerpo.eval')
    p[1].append(p[2])
    p[0] = p[1]

def p_PRECUERPO_ERROR(p):
    'PRECUERPO : PRECUERPO error'
    # print('precuerpo.eval = precuerpo.eval + cuerpo.eval')
    p[0] = None
    p.parser.error += 1


def p_PRECUERPO_ERROR1(p):
    'PRECUERPO : error CUERPO'
    # print('precuerpo.eval = precuerpo.eval + cuerpo.eval')
    p[0] = None
    p.parser.error += 1


def p_PRECUERPO_CUERPO(p):
    'PRECUERPO : CUERPO'
    # print('precuerpo.eval = cuerpo.eval')
    p[0] = [p[1]]


def p_CUERPO(p):
    '''CUERPO : ETIQUETA
              | GOTO_LABEL
              | ASIGNACION
              | DESTRUYE_VARIABLE
              | IMPRIME
              | ESTRUCTURA_IF
              | EXIT'''
    # print('cuerpo.eval = value.eval')
    p[0] = p[1]


def p_ETIQUETA(p):
    'ETIQUETA : ID DOSPUNTOS PRECUERPO'
    # print('label.eval = precuerpo.eval')

    p[0] = etiqueta(TIPO_INSTRUCCION.BANDERA,p[1],p.lexer.lineno, p[3])

def p_ETIQUETA_ERROR(p):
    'ETIQUETA : error DOSPUNTOS PRECUERPO'
    # print('label.eval = precuerpo.eval')

def p_GOTO_LABEL(p):
    'GOTO_LABEL : goto ID PTCOMA'
    # print('goto_label.eval = ID')

    p[0] = salto_bandera(TIPO_INSTRUCCION.SALTO_BANDERA, p[2],p.lexer.lineno)


def p_ASIGNACION(p):
    '''ASIGNACION : NORMAL PTCOMA
                  | ARRAY PTCOMA'''
    # print('asignacion.eval = value.eval')
    p[0] = p[1]


def p_NORMAL(p):
    'NORMAL : VARIABLE IGUAL EXPRESION'
    # print('normal.eval =  VARIABLE + expresion.eval')

    p[0] = asignacion(TIPO_INSTRUCCION.ASIGNACION, p.lexer.lineno,p[1], p[3])


def p_ARRAY(p):
    'ARRAY : VARIABLE LISTA_POS IGUAL EXPRESION'
    # print('array.eval = VARIABLE.eval + EXPRESION.eval + EXPRESION.eval')

    p[0] = asignacion(TIPO_INSTRUCCION.ASIGNACION, p.lexer.lineno,p[1], p[4], p[2])


def p_EXPRESION(p):
    'EXPRESION : VALOR'
    # print('expresion.eval = value.eval')
    p[0] = p[1]

def p_EXPRESION_ERROR(p):
    'EXPRESION : error'
    # print('expresion.eval = value.eval')
    p[0] = p[1]

def p_EXPRESIONP(p):
    'EXPRESION : PARA EXPRESION PARB'
    # print('expresion.eval = value.eval')
    p[0] = p[2]



def p_VALOR_VARIABLE(p):
    'VALOR : VARIABLE'
    # print('valor.eval = variable.eval')

    p[0] = valor(p[1], METHOD_VALUE.VARIABLE, None)


def p_VALOR_LLAMADA_ARREGLO(p):
    'VALOR : LLAMADA_ARREGLO'
    # print('valor.eval = llamada_arreglo.eval')
    p[0] = p[1]


def p_VALOR_NUMERO(p):
    'VALOR : INT'
    # print('valor.eval = INT')

    p[0] = valor(p[1], METHOD_VALUE.VALOR_UNICO, TYPE_VALUE.NUMERIC)


def p_VALOR_FLOAT(p):
    'VALOR : FLOAT'
    # print('valor.eval = FLOAT')

    p[0] = valor(p[1], METHOD_VALUE.VALOR_UNICO, TYPE_VALUE.NUMERIC)


def p_VALOR_CARACTER(p):
    '''VALOR : CHAR'''
    # print('valor.eval = CHAR')

    p[0] = valor(p[1], METHOD_VALUE.VALOR_UNICO, TYPE_VALUE.CHARACTER)


def p_VALOR_NUEVO_ARREGLO(p):
    '''VALOR : array PARA PARB'''
    # print('valor.eval = array')

    arreglo = array_s(ARRAY_METHOD.INSTANCIA, list)
    p[0] = valor(arreglo, METHOD_VALUE.ARREGLO, TYPE_VALUE.ARREGLO)


def p_VALOR_LEER(p):
    '''VALOR : read PARA PARB'''
    # print"('valor.eval = read')


def p_EXPRESION_ARITMETICAS(p):
    '''EXPRESION : ARITMETICAS'''
    p[0] = p[1]


def p_ARITMETICAS_NEGATIVO(p):
    '''ARITMETICAS : MENOS VALOR'''

    p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.NEGATIVO, p[2], None)


def p_ARITMETICAS(p):
    '''ARITMETICAS : EXPRESION MAS EXPRESION
                   | EXPRESION MENOS EXPRESION
                   | EXPRESION MULTIPLICACION EXPRESION
                   | EXPRESION DIVIDIR EXPRESION
                   | EXPRESION RESIDUO EXPRESION'''

    if p[2] == '+':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.SUMA, p[1], p[3])
    elif p[2] == '-':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.RESTA, p[1], p[3])
    elif p[2] == '*':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.MULTIPLICACION, p[1], p[3])
    elif p[2] == '/':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.DIVISION, p[1], p[3])
    elif p[2] == '%':
        p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.RESIDUO, p[1], p[3])


def p_ARITMETICAS_ABS(p):
    '''ARITMETICAS : abs PARA EXPRESION PARB'''

    p[0] = operacionesAritmeticas(OPERACION_ARITMETICA.ABSOLUTO, p[3], None)


def p_EXPRESION_LOGICAS(p):
    '''EXPRESION : LOGICAS'''
    p[0] = p[1]


def p_LOGICAS_NOT(p):
    '''LOGICAS : NOTL VALOR'''

    p[0] = operacionesLogicas(OPERACION_LOGICA.NOT, p[2], None)


def p_LOGICAS(p):
    '''LOGICAS : VALOR ANDL VALOR
               | VALOR ORL VALOR
               | VALOR XORL VALOR'''

    if p[2] == '&&':
        p[0] = operacionesLogicas(OPERACION_LOGICA.AND, p[1], p[3])
    elif p[2] == '||':
        p[0] = operacionesLogicas(OPERACION_LOGICA.OR, p[1], p[3])
    elif p[2] == 'xor':
        p[0] = operacionesLogicas(OPERACION_LOGICA.XOR, p[1], p[3])


def p_EXPRESION_RELACIONAL(p):
    '''EXPRESION : RELACIONAL'''
    p[0] = p[1]


def p_RELACIONAL(p):
    '''RELACIONAL : VALOR IGUALR  VALOR
                  | VALOR NOIGUALR  VALOR
                  | VALOR MAYORR IGUAL VALOR
                  | VALOR MENORR IGUAL VALOR
                  | VALOR MAYORR VALOR
                  | VALOR MENORR VALOR'''

    if p[2] == '==':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.EQUALS, p[1], p[3])
    elif p[2] == '!=':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.NOTEQUALS, p[1], p[3])
    elif p[2] == '>' and p[3] == '=':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.MAYOR_EQUALS, p[1], p[4])
    elif p[2] == '<' and p[3] == '=':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.MENOR_EQUALS, p[1], p[4])
    elif p[2] == '>':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.MAYOR, p[1], p[3])
    elif p[2] == '<':
        p[0] = operacionesRelacionales(OPERACION_RELACIONAL.MENOR, p[1], p[3])


def p_EXPRESION_BIT(p):
    '''EXPRESION : BIT'''
    p[0] = p[1]


def p_BIT_NOT(p):
    '''BIT : NOTB VALOR'''

    p[0] = operacionesBit(OPERACION_BIT.NOTB, p[2], None)


def p_BIT(p):
    '''BIT : VALOR ANDB VALOR
           | VALOR ORB VALOR
           | VALOR XORB VALOR
           | VALOR MENORR MENORR VALOR
           | VALOR MAYORR MAYORR VALOR'''

    if p[2] == '&':
        p[0] = operacionesBit(OPERACION_BIT.ANDB, p[1], p[3])
    elif p[2] == '|':
        p[0] = operacionesBit(OPERACION_BIT.ORB, p[1], p[3])
    elif p[2] == '^':
        p[0] = operacionesBit(OPERACION_BIT.XORB, p[1], p[3])
    elif p[2] == '<' and p[3] == '<':
        p[0] = operacionesBit(OPERACION_BIT.SHIFTA, p[1], p[4])
    elif p[2] == '>' and p[3] == '>':
        p[0] = operacionesBit(OPERACION_BIT.SHIFTB, p[1], p[4])


def p_LLAMADA_ARREGLO(p):
    'LLAMADA_ARREGLO : VARIABLE LISTA_POS'

    arreglo = array_s(ARRAY_METHOD.GET, list, p[1], p[2])
    p[0] = valor(arreglo, METHOD_VALUE.ARREGLO, None)


def p_LISTA_POS_L(p):
    'LISTA_POS :  LISTA_POS POS'
    p[1].append(p[2])
    p[0] = p[1]


def p_LISTA_POS_P(p):
    'LISTA_POS : POS'
    p[0] = [p[1]]


def p_POS(p):
    'POS : CORA EXPRESION CORB'

    p[0] = p[2]


def p_EXPRESION_CONVERSION(p):
    '''EXPRESION : CONVERSION'''
    p[0] = p[1]


def p_CONVERSION(p):
    '''CONVERSION : PARA TIPO_CONVERSION PARB VALOR'''

    value = {"tipo": p[2], "value": p[4]}
    p[0] = valor(value, METHOD_VALUE.CONVERSION, None)


def p_TIPO_CONVERSION(p):
    '''TIPO_CONVERSION : int
                       | char
                       | float'''

    p[0] = p[1]


def p_EXPRESION_PUNTERO(p):
    '''EXPRESION : PUNTERO'''
    p[0] = p[1]


def p_PUNTERO(p):
    '''PUNTERO : ANDB VARIABLE'''

    p[0] = valor('&'+p[2], METHOD_VALUE.APUNTADOR, TYPE_VALUE.APUNTADOR)


def p_ESTRUCTURA_IF(p):
    '''ESTRUCTURA_IF : if PARA EXPRESION PARB goto ID PTCOMA'''

    p[0] = sentencia_control(TIPO_INSTRUCCION.IFCONTROL,p.lexer.lineno, p[3], p[6])


def p_DESTRUYE_VARIABLE(p):
    '''DESTRUYE_VARIABLE : unset PARA VALOR PARB PTCOMA'''

    p[0] = destructor(TIPO_INSTRUCCION.DESTRUCTOR,p.lexer.lineno, p[3])


def p_IMPRIME(p):
    '''IMPRIME : print PARA EXPRESION PARB PTCOMA'''

    p[0] = imprimir(TIPO_INSTRUCCION.IMPRIMIR, p.lexer.lineno,p[3])


def p_EXIT(p):
    '''EXIT : exit PTCOMA'''

    p[0] = salida(TIPO_INSTRUCCION.SALIDA,p.lexer.lineno)


parser = yacc.yacc()


def parsedes(errors, data, debug=0):
    parser.error = 0
    p = parser.parse(data)
    errors.errores_sintacticos = parser.getErrores()
    errors.errores_lexicos = gramatica.lexicos
    if parser.error:
        return None
    return p
