# ANALIZADOR SINTACTICO ASCENDENTE PARA AUGUS
# JOSE WANNAN @2020
# UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

from ply import *
import gramatica
from AST import *

caracteres = 0


def format_result(r):
    repr_str = repr(r)
    if ' ' in repr_str:
        repr_str = repr(repr_str)
    if len(repr_str) > 40:
        repr_str = repr_str[:40] + ' ...'
    result = '<%s @ 0x%x> (%s)' % (type(r).__name__, id(r), repr_str)
    return repr_str


def format_results(r):
    repr_str = repr(r)
    if ' ' in repr_str:
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
    # print("S -ESTRUCTURAMAIN")
    raiz = Nodo('S')
    raiz.hijos.append(p[1])
    raiz.produccion('S -ESTRUCTURAMAIN')
    raiz.reglaSemantica('S.val = val[tope]')
    p[0] = raiz



def p_S_error(p):
    'S : error'
    p[0] = None
    p.parser.error += 1


def p_ESTRUCTURAMAIN(p):
    'ESTRUCTURAMAIN : main DOSPUNTOS PRECUERPO1'
    # print('estructuramain.eval = precuerpo.eval')
    estructuramain = Nodo('ESTRUCTURAMAIN')
    estructuramain.hijos.append(Nodo('main'))
    estructuramain.hijos.append(Nodo(':'))
    estructuramain.hijos.append(p[3])
    estructuramain.produccion('ESTRUCTURAMAIN - main : LCUERPO')
    estructuramain.reglaSemantica('ESTRUCTURAMAIN.val = val[tope+3]')
    p[0] = estructuramain



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

def p_PRECUERPO1(p):
    'PRECUERPO1 :  CUERPO PRECUERPO'
    # print('precuerpo.eval = precuerpo.eval + cuerpo.eval')
    if isinstance(p[2], list):
        expresion = Nodo('LCUERPO')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2][0])
        expresion.produccion('LCUERPO  -  CUERPO LCUERPO1')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion
    else:
        expresion = Nodo('LCUERPO')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2])
        expresion.produccion('LCUERPO  -  CUERPO LCUERPO1')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion



def p_PRECUERPO(p):
    'PRECUERPO :  CUERPO PRECUERPO1'
    # print('precuerpo.eval = precuerpo.eval + cuerpo.eval')
    if isinstance(p[2], list):
        expresion = Nodo('LCUERPO\'')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2][0])
        expresion.produccion('LCUERPO1  -  CUERPO LCUERPO')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion
    else:
        expresion = Nodo('LCUERPO\'')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2])
        expresion.produccion('LCUERPO1  -  CUERPO LCUERPO')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion

def p_PRECUERPO_CUERPO(p):
    'PRECUERPO : CUERPO'
    # print('precuerpo.eval = cuerpo.eval')
    p[0] = p[1]


def p_CUERPO(p):
    '''CUERPO : ETIQUETA
              | GOTO_LABEL
              | ASIGNACION
              | DESTRUYE_VARIABLE
              | IMPRIME
              | ESTRUCTURA_IF
              | EXIT
              | '''
    # print('cuerpo.eval = value.eval')
    if len(p)>1:
        expresion = Nodo('CUERPO')
        expresion.hijos.append(p[1])
        expresion.produccion('CUERPO  - E')
        expresion.reglaSemantica('T = new cuerpo(); T.value = val[tope+1]; val[tope] = T;')
        p[0] = expresion
    else:
        p[0] = Nodo('[Empty]')

def p_PRECUERPOE1(p):
    'PRECUERPOE1 : CUERPOE PRECUERPOE'
    # print('precuerpo.eval = precuerpo.eval + cuerpo.eval')
    if isinstance(p[2], list):
        expresion = Nodo('LCUERPOE')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2][0])
        expresion.produccion('LCUERPOE  -  CUERPOE LCUERPOE1')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion
    else:
        expresion = Nodo('LCUERPOE')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2])
        expresion.produccion('LCUERPOE  -  CUERPOE LCUERPOE1')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion


def p_PRECUERPOE(p):
    'PRECUERPOE : CUERPOE PRECUERPOE1'
    # print('precuerpo.eval = precuerpo.eval + cuerpo.eval')
    if isinstance(p[2], list):
        expresion = Nodo('LCUERPOE\'')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2][0])
        expresion.produccion('LCUERPOE1  -  CUERPOE LCUERPOE')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion
    else:
        expresion = Nodo('LCUERPOE\'')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2])
        expresion.produccion('LCUERPOE1  -  CUERPOE LCUERPOE')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion

def p_PRECUERPO_CUERPOE(p):
    'PRECUERPOE : CUERPOE'
    # print('precuerpo.eval = cuerpo.eval')
    p[0] = p[1]


def p_CUERPOE(p):
    '''CUERPOE : GOTO_LABEL
              | ASIGNACION
              | DESTRUYE_VARIABLE
              | IMPRIME
              | ESTRUCTURA_IF
              | EXIT
              | '''
    # print('cuerpo.eval = value.eval')
    if len(p)>1:
        expresion = Nodo('CUERPOE')
        expresion.hijos.append(p[1])
        expresion.produccion('CUERPOE  - E')
        expresion.reglaSemantica('T = new cuerpo(); T.value = val[tope+1]; val[tope] = T;')
        p[0] = expresion
    else:
        p[0] = Nodo('[empty]')

def p_ETIQUETA(p):
    'ETIQUETA : ID DOSPUNTOS PRECUERPOE'
    # print('label.eval = precuerpo.eval')
    expresion = Nodo('ETIQUETA')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(Nodo(':'))
    expresion.hijos.append(p[3])
    expresion.produccion('ETIQUETA  - ID : PRECUERPOE')
    expresion.reglaSemantica('T = new Etiqueta(); id = '+p[1]+'; T.id = id; T.addCuerpo(val[tope+2]); val[tope] = T;')
    p[0] = expresion

def p_ETIQUETA_ERROR(p):
    'ETIQUETA : error DOSPUNTOS PRECUERPO'
    # print('label.eval = precuerpo.eval')

def p_GOTO_LABEL(p):
    'GOTO_LABEL : goto ID PTCOMA'
    # print('goto_label.eval = ID')
    saltobandera = Nodo('GOTO_LABEL')
    saltobandera.hijos.append(Nodo('goto'))
    saltobandera.hijos.append(Nodo(p[2]))
    saltobandera.hijos.append(Nodo(';'))
    saltobandera.produccion('GOTO_LABEL - goto ID ;')
    saltobandera.reglaSemantica('T = new Return(); id = '+p[2]+'; T.val = id.val; val[tope] = T;')
    p[0] = saltobandera


def p_ASIGNACION(p):
    '''ASIGNACION : NORMAL PTCOMA'''
    # print('asignacion.eval = value.eval')
    asignacion = Nodo('ASIGNACION')
    asignacion.hijos.append(p[1])
    asignacion.hijos.append(Nodo(';'))
    asignacion.produccion('ASIGNACION  - NORMAL')
    asignacion.reglaSemantica('T = new asignacion(); T.value = val[tope+1];  val[tope] = T;')
    p[0] = asignacion

def p_ASIGNACION1(p):
    '''ASIGNACION : ARRAY PTCOMA'''
    # print('asignacion.eval = value.eval')
    asignacion = Nodo('ASIGNACION')
    asignacion.hijos.append(p[1])
    asignacion.hijos.append(Nodo(';'))
    asignacion.produccion('ASIGNACION  - ARRAY')
    asignacion.reglaSemantica('T = new asignacion(); T.value = val[tope+1];  val[tope] = T;')
    p[0] = asignacion


def p_NORMAL(p):
    'NORMAL : VARIABLE IGUAL EXPRESION'
    # print('normal.eval =  VARIABLE + expresion.eval')
    aNormal = Nodo('NORMAL')
    aNormal.hijos.append(Nodo(p[1]))
    aNormal.hijos.append(Nodo('='))
    aNormal.hijos.append(p[3])
    aNormal.produccion('NORMAL  - VARIABLE = EXPRESION')
    aNormal.reglaSemantica('T = new Normal(); var = '+p[1]+'; T.var = var; T.val = val[tope+3];  val[tope] = T;')
    p[0] = aNormal


def p_ARRAY(p):
    'ARRAY : VARIABLE LISTA_POS IGUAL EXPRESION'
    # print('array.eval = VARIABLE.eval + EXPRESION.eval + EXPRESION.eval')
    aArray = Nodo('ARRAY')
    aArray.hijos.append(Nodo(p[1]))
    aArray.hijos.append(p[2])
    aArray.hijos.append(Nodo('='))
    aArray.hijos.append(p[4])
    aArray.produccion('ARRAY  - VARIABLE LISTA_POS = EXPRESION')
    aArray.reglaSemantica('T = new Array(); var = '+p[1]+'; T.var = var; T.pos = val[tope+2]; T.val = val[tope+4];  val[tope] = T;')
    p[0] = aArray


def p_EXPRESION(p):
    'EXPRESION : VALOR'
    # print('expresion.eval = value.eval')
    expresion = Nodo('EXPRESION')
    expresion.hijos.append(p[1])
    expresion.produccion('EXPRESION  - VALOR')
    expresion.reglaSemantica('T = new Valor();  T.value = val[tope+1];  val[tope] = T;')
    p[0] = expresion

def p_EXPRESION_ERROR(p):
    'EXPRESION : error'
    # print('expresion.eval = value.eval')
    p[0] = p[1]

def p_EXPRESIONP(p):
    'EXPRESION : PARA EXPRESION PARB'
    # print('expresion.eval = value.eval')
    expresion = Nodo('EXPRESION')
    expresion.hijos.append(Nodo('('))
    expresion.hijos.append(p[2])
    expresion.hijos.append(Nodo(')'))
    expresion.produccion('EXPRESION  - ( EXPRESION )')
    expresion.reglaSemantica('val[tope] = val[tope+1];')
    p[0] = expresion



def p_VALOR_VARIABLE(p):
    'VALOR : VARIABLE'
    # print('valor.eval = variable.eval')
    valor = Nodo('VALOR')
    valor.hijos.append(Nodo(p[1]))
    valor.produccion('VALOR  - VARIABLE')
    valor.reglaSemantica('T = new Variable(); T.var = '+p[1]+'; val[tope] = T;')
    p[0] = valor


def p_VALOR_LLAMADA_ARREGLO(p):
    'VALOR : LLAMADA_ARREGLO'
    # print('valor.eval = llamada_arreglo.eval')
    valor = Nodo('VALOR')
    valor.hijos.append(p[1])
    valor.produccion('VALOR  - LLAMADA_ARREGLO')
    valor.reglaSemantica('val[tope] = val[tope+1]')
    p[0] = valor


def p_VALOR_NUMERO(p):
    'VALOR : INT'
    # print('valor.eval = INT')
    valor = Nodo('VALOR')
    valor.hijos.append(Nodo(str(p[1])))
    valor.produccion('VALOR  - INT')
    valor.reglaSemantica('entero = '+str(p[1])+'; val[tope] = entero;')
    p[0] = valor


def p_VALOR_FLOAT(p):
    'VALOR : FLOAT'
    # print('valor.eval = FLOAT')
    valor = Nodo('VALOR')
    valor.hijos.append(Nodo(str(p[1])))
    valor.produccion('VALOR  - FLOAT')
    valor.reglaSemantica('float = ' + str(p[1]) + '; val[tope] = float;')
    p[0] = valor


def p_VALOR_CARACTER(p):
    '''VALOR : CHAR'''
    # print('valor.eval = CHAR')
    valor = Nodo('VALOR')
    valor.hijos.append(Nodo(p[1]))
    valor.produccion('VALOR  - CHAR')
    valor.reglaSemantica('caracteres = ' + str(p[1]) + '; val[tope] = caracteres;')
    p[0] = valor


def p_VALOR_NUEVO_ARREGLO(p):
    '''VALOR : array PARA PARB'''
    # print('valor.eval = array')
    valor = Nodo('VALOR')
    valor.hijos.append(Nodo('array'))
    valor.hijos.append(Nodo('('))
    valor.hijos.append(Nodo(')'))
    valor.produccion('VALOR  - array ( )')
    valor.reglaSemantica('array = {} ; val[tope] = array;')
    p[0] = valor


def p_VALOR_LEER(p):
    '''VALOR : read PARA PARB'''
    # print"('valor.eval = read')
    valor = Nodo('VALOR')
    valor.hijos.append(Nodo('read'))
    valor.hijos.append(Nodo('('))
    valor.hijos.append(Nodo(')'))
    valor.produccion('VALOR  - read ( )')
    valor.reglaSemantica('valor = system.interrup_system_call; val[tope] = valor;')
    p[0] = valor


def p_EXPRESION_ARITMETICAS(p):
    '''EXPRESION : ARITMETICAS'''
    expresion = Nodo('EXPRESION')
    expresion.hijos.append(p[1])
    expresion.produccion('EXPRESION  - ARITMETICAS')
    expresion.reglaSemantica('val[tope] = val[tope+1];')
    p[0] = expresion


def p_ARITMETICAS_NEGATIVO(p):
    '''ARITMETICAS : MENOS VALOR'''
    expresion = Nodo('ARITMETICAS')
    expresion.hijos.append(Nodo('-'))
    expresion.hijos.append(p[1])
    expresion.produccion('ARITMETICAS  - - EXPRESION')
    expresion.reglaSemantica('val[tope] = -1 * val[tope+1];')
    p[0] = expresion


def p_ARITMETICAS(p):
    '''ARITMETICAS : EXPRESION MAS EXPRESION
                   | EXPRESION MENOS EXPRESION
                   | EXPRESION MULTIPLICACION EXPRESION
                   | EXPRESION DIVIDIR EXPRESION
                   | EXPRESION RESIDUO EXPRESION'''

    expresion = Nodo('ARITMETICAS')
    expresion.hijos.append(p[1])
    expresion.hijos.append(Nodo(p[2]))
    expresion.hijos.append(p[3])
    expresion.produccion('ARITMETICAS  - EXPRESION '+p[2]+' EXPRESION')
    expresion.reglaSemantica('val[tope] = val[tope+1] '+p[2]+' val[tope+3];')
    p[0] = expresion


def p_ARITMETICAS_ABS(p):
    '''ARITMETICAS : abs PARA EXPRESION PARB'''
    expresion = Nodo('ARITMETICAS')
    expresion.hijos.append(Nodo('abs'))
    expresion.hijos.append(Nodo('('))
    expresion.hijos.append(p[3])
    expresion.hijos.append(Nodo(')'))
    expresion.produccion('ARITMETICAS  - abs ( EXPRESION )')
    expresion.reglaSemantica('val[tope] = val[tope+2];')
    p[0] = expresion


def p_EXPRESION_LOGICAS(p):
    '''EXPRESION : LOGICAS'''
    expresion = Nodo('EXPRESION')
    expresion.hijos.append(p[1])
    p[0] = expresion


def p_LOGICAS_NOT(p):
    '''LOGICAS : NOTL VALOR'''
    expresion = Nodo('LOGICAS')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(p[2])
    expresion.produccion('EXPRESION  - LOGICAS')
    expresion.reglaSemantica('val[tope] = val[tope+1];')
    p[0] = expresion


def p_LOGICAS(p):
    '''LOGICAS : VALOR ANDL VALOR
               | VALOR ORL VALOR
               | VALOR XORL VALOR'''

    expresion = Nodo('LOGICAS')
    expresion.hijos.append(p[1])
    expresion.hijos.append(Nodo(p[2]))
    expresion.hijos.append(p[3])
    expresion.produccion('LOGICAS  - VALOR ' + p[2] + ' VALOR')
    expresion.reglaSemantica('val[tope] = val[tope+1] ' + p[2] + ' val[tope+3];')
    p[0] = expresion


def p_EXPRESION_RELACIONAL(p):
    '''EXPRESION : RELACIONAL'''
    expresion = Nodo('RELACIONAL')
    expresion.hijos.append(p[1])
    expresion.produccion('EXPRESION  - RELACIONAL')
    expresion.reglaSemantica('val[tope] = val[tope+1];')
    p[0] = expresion


def p_RELACIONAL(p):
    '''RELACIONAL : VALOR IGUALR  VALOR
                  | VALOR NOIGUALR  VALOR
                  | VALOR MAYORR IGUAL VALOR
                  | VALOR MENORR IGUAL VALOR
                  | VALOR MAYORR VALOR
                  | VALOR MENORR VALOR'''

    if p[2] == '>' and p[3] == '=':
        expresion = Nodo('RELACIONAL')
        expresion.hijos.append(p[1])
        expresion.hijos.append(Nodo(p[2] + p[3]))
        expresion.hijos.append(p[4])
        expresion.produccion('RELACIONAL  - VALOR mayorigual VALOR')
        expresion.reglaSemantica('val[tope] = val[tope+1] mayoroigual val[tope+4];')
        p[0] = expresion
    elif p[2] == '<' and p[3] == '=':
        expresion = Nodo('RELACIONAL')
        expresion.hijos.append(p[1])
        expresion.hijos.append(Nodo(p[2] + p[3]))
        expresion.hijos.append(p[4])
        expresion.produccion('RELACIONAL  - VALOR menorigual VALOR')
        expresion.reglaSemantica('val[tope] = val[tope+1] menorigual val[tope+4];')
        p[0] = expresion
    elif p[2] == '<':
        expresion = Nodo('RELACIONAL')
        expresion.hijos.append(p[1])
        expresion.hijos.append(Nodo(p[2] + p[3]))
        expresion.hijos.append(p[4])
        expresion.produccion('RELACIONAL  - VALOR menor VALOR')
        expresion.reglaSemantica('val[tope] = val[tope+1] menor val[tope+4];')
        p[0] = expresion
    elif p[2] == '>':
        expresion = Nodo('RELACIONAL')
        expresion.hijos.append(p[1])
        expresion.hijos.append(Nodo(p[2] + p[3]))
        expresion.hijos.append(p[4])
        expresion.produccion('RELACIONAL  - VALOR mayor VALOR')
        expresion.reglaSemantica('val[tope] = val[tope+1] mayor val[tope+4];')
        p[0] = expresion
    else:
        expresion = Nodo('RELACIONAL')
        expresion.hijos.append(p[1])
        expresion.hijos.append(Nodo(p[2]))
        expresion.hijos.append(p[3])
        expresion.produccion('RELACIONAL  - VALOR ' + p[2] + ' VALOR')
        expresion.reglaSemantica('val[tope] = val[tope+1] ' + p[2] + ' val[tope+3];')
        p[0] = expresion


def p_EXPRESION_BIT(p):
    '''EXPRESION : BIT'''
    expresion = Nodo('EXPRESION')
    expresion.hijos.append(p[1])
    expresion.produccion('EXPRESION  - BIT')
    expresion.reglaSemantica('val[tope] = val[tope+1];')
    p[0] = expresion


def p_BIT_NOT(p):
    '''BIT : NOTB VALOR'''
    expresion = Nodo('BIT')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(p[2])
    expresion.produccion('BIT  - ~ VALOR')
    expresion.reglaSemantica('val[tope] = ~val[tope+1];')
    p[0] = expresion


def p_BIT(p):
    '''BIT : VALOR ANDB VALOR
           | VALOR ORB VALOR
           | VALOR XORB VALOR
           | VALOR MENORR MENORR VALOR
           | VALOR MAYORR MAYORR VALOR'''

    if p[2] == '<' and p[3] == '<':
        expresion = Nodo('BIT')
        expresion.hijos.append(p[1])
        expresion.hijos.append(Nodo(p[2] + p[3]))
        expresion.hijos.append(p[4])
        expresion.produccion('BIT  - VALOR shifta VALOR')
        expresion.reglaSemantica('val[tope] = val[tope+1] shifta val[tope+4];')
        p[0] = expresion
    elif p[2] == '>' and p[3] == '>':
        expresion = Nodo('BIT')
        expresion.hijos.append(p[1])
        expresion.hijos.append(Nodo(p[2] + p[3]))
        expresion.hijos.append(p[4])
        expresion.produccion('RELACIONAL  - VALOR shiftb VALOR')
        expresion.reglaSemantica('val[tope] = val[tope+1] shiftb val[tope+4];')
        p[0] = expresion
    else:
        expresion = Nodo('BIT')
        expresion.hijos.append(p[1])
        expresion.hijos.append(Nodo(p[2]))
        expresion.hijos.append(p[3])
        expresion.produccion('BIT  - VALOR ' + p[2] + ' VALOR')
        expresion.reglaSemantica('val[tope] = val[tope+1] ' + p[2] + ' val[tope+3];')
        p[0] = expresion


def p_LLAMADA_ARREGLO(p):
    'LLAMADA_ARREGLO : VARIABLE LISTA_POS'

    expresion = Nodo('LLAMADA_ARREGLO')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(p[2])
    expresion.produccion('LLAMADA_ARREGLO  - VARIABLE LISTAPOS')
    expresion.reglaSemantica('T = new LLamadaA(); T.var = '+p[1]+'; T.pos = val[top+2]; val[tope] = T;')
    p[0] = expresion

def p_LISTA_POS_L(p):
    'LISTA_POS :  POS LISTA_POS1'
    if isinstance(p[2],list):
        expresion = Nodo('LISTA_POS')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2][0])
        expresion.produccion('LISTA_POS  - POS LISTA_POS1')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion
    else:
        expresion = Nodo('LISTA_POS')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2])
        expresion.produccion('LISTA_POS  - POS LISTA_POS1')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion



def p_LISTA_POS_L1(p):
    'LISTA_POS1 :  POS LISTA_POS'
    if isinstance(p[2],list):
        expresion = Nodo('LISTA_POS\'')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2][0])
        expresion.produccion('LISTA_POS1  - POS LISTA_POS')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion
    else:
        expresion = Nodo('LISTA_POS\'')
        expresion.hijos.append(p[1])
        expresion.hijos.append(p[2])
        expresion.produccion('LISTA_POS1  - POS LISTA_POS')
        expresion.reglaSemantica('N = []; N.append(val[tope+1]; N.append(val[tope+2]; val[tope] = N;')
        p[0] = expresion



def p_LISTA_POS_P(p):
    '''LISTA_POS : POS
               | '''
    if len(p) >1:
        p[0] = p[1]
    else:
        p[0] = Nodo('[Empty]')


def p_POS(p):
    'POS : CORA VALOR CORB'
    expresion = Nodo('POS')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(p[2])
    expresion.hijos.append(Nodo(p[3]))
    expresion.produccion('POS  - [ VALOR ]')
    expresion.reglaSemantica('val[tope] = val[tope+2];')
    p[0] = expresion


def p_EXPRESION_CONVERSION(p):
    '''EXPRESION : CONVERSION'''
    expresion = Nodo('EXPRESION')
    expresion.hijos.append(p[1])
    expresion.produccion('EXPRESION  - CONVERSION')
    expresion.reglaSemantica('val[tope] = val[tope+1];')
    p[0] = expresion


def p_CONVERSION(p):
    '''CONVERSION : PARA TIPO_CONVERSION PARB VALOR'''

    expresion = Nodo('CONVERSION')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(p[2])
    expresion.hijos.append(Nodo(p[3]))
    expresion.hijos.append(p[4])
    expresion.produccion('CONVERSION  - ( TIPO ) VALOR')
    expresion.reglaSemantica('T = new Convertion(); T.tipo = val[tope+2]; T.value = val[tope+4]; val[tope] = T;')
    p[0] = expresion


def p_TIPO_CONVERSION(p):
    '''TIPO_CONVERSION : int
                       | char
                       | float'''

    expresion = Nodo('TIPO')
    expresion.hijos.append(Nodo(p[1]))
    expresion.produccion('TIPO  - '+p[1])
    expresion.reglaSemantica('val[tope] = val[tope+1];')
    p[0] = expresion


def p_EXPRESION_PUNTERO(p):
    '''EXPRESION : PUNTERO'''
    expresion = Nodo('EXPRESION')
    expresion.hijos.append(p[1])
    expresion.produccion('EXPRESION  - PRODUCCION')
    expresion.reglaSemantica('val[tope] = val[tope+1];')
    p[0] = expresion


def p_PUNTERO(p):
    '''PUNTERO : ANDB VARIABLE'''
    expresion = Nodo('PUNTERO')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(Nodo(p[2]))
    expresion.produccion('PUNTERO  - & VARIABLE')
    expresion.produccion('var = '+p[2]+';  val[tope] = var;')
    p[0] = expresion


def p_ESTRUCTURA_IF(p):
    '''ESTRUCTURA_IF : if PARA EXPRESION PARB goto ID PTCOMA'''

    expresion = Nodo('IF')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(Nodo(p[2]))
    expresion.hijos.append(p[3])
    expresion.hijos.append(Nodo(p[4]))
    expresion.hijos.append(Nodo(p[5]))
    expresion.hijos.append(Nodo(p[6]))
    expresion.hijos.append(Nodo(p[7]))
    expresion.produccion('IF  - if ( EXPRESION ) goto ID ;')
    expresion.reglaSemantica('T = new conditional(); T.condicion = val[tope+3]; T.salto = '+p[6]+';  val[tope] = T;')
    p[0] = expresion


def p_DESTRUYE_VARIABLE(p):
    '''DESTRUYE_VARIABLE : unset PARA VALOR PARB PTCOMA'''
    expresion = Nodo('DESTRUYE_VARIABLE')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(Nodo(p[2]))
    expresion.hijos.append(p[3])
    expresion.hijos.append(Nodo(p[4]))
    expresion.hijos.append(Nodo(p[5]))
    expresion.produccion('DESTRUYE_VARIABLE  - unset ( VALOR ) ;')
    expresion.reglaSemantica('T = new destruct(); T.var = val[tope+3]; val[tope] = T;')
    p[0] = expresion


def p_IMPRIME(p):
    '''IMPRIME : print PARA EXPRESION PARB PTCOMA'''

    expresion = Nodo('IMPRIME')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(Nodo(p[2]))
    expresion.hijos.append(p[3])
    expresion.hijos.append(Nodo(p[4]))
    expresion.hijos.append(Nodo(p[5]))
    expresion.produccion('IMPRIME  - print ( EXPRESION ) ;')
    expresion.reglaSemantica('T = new print(); T.exp = val[tope+3]; val[tope] = T;')
    p[0] = expresion


def p_EXIT(p):
    '''EXIT : exit PTCOMA'''
    expresion = Nodo('EXIT')
    expresion.hijos.append(Nodo(p[1]))
    expresion.hijos.append(Nodo(p[2]))
    expresion.produccion('EXIT - exit ;')
    expresion.reglaSemantica('T = new Exit(); T.defined = 1 val[tope] = T;')
    p[0] = expresion



parser = yacc.yacc()


def arparsedes(data):

        parser.error = 0
        p = parser.parse(data)
        if parser.error:
            return None
        return p
