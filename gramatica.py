#GRAMATICA DESCENDENTE AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA


from ply import *
import re

RESERVED_WORDS =\
{
    'if',
    'goto',
    'read',
    'print',
    'unset',
    'exit',
    'abs',
    'array',
    'main'
}

TOKENS = RESERVED_WORDS + {
    'IGUAL','INT','FLOAT','CHAR'
    'MAS','MENOS','PARENA','PARENB','PTCOMA',
    'NEWLINE','DIVIDIR', 'RESIDUO',
    'MULTIPLICACION','NOTL',
    'ANDL','ORL','XORL','NOTB','ANDB',
    'ORB','XORB','SHIFTA','SHITB',
    'IGUALR','NOIGUALR','MAYORIGUALR',
    'MENORIGUALR','MAYORR','MENORR',
    'CORA','CORB','ID','VARIABLE'
}

t_ignore = ' \t'

def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    if t.value in RESERVED_WORDS:
        t.type = t.value
    return t

def t_VARIABLE(t):
    r'($)(a|t|v|ra|s|sp)([0-9]?)'
    match = re.search('($)(?P<variable>(a|t|v|ra|s|sp) ([0-9]?))',t.value)
    t.value = match.groups('variable')
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Not a Valid %d", t.value)
        t.value = 0
    return t

def t_CHAR(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Not a Valid %d", t.value)
    return 0

def t_comentario(t):
    r'#.*'
    t.lexer.lineno += 1

t_IGUAL = r'='
t_MAS = r'+'
t_MENOS = r'-'
t_PARENA = r'('
t_PARENB = r')'
t_PTCOMA = r';'
t_DIVIDIR = r'/'
t_RESIDUO = r'%'
t_MULTIPLICACION = r'*'
t_NOTL = r'!'
t_ANDL = r'&&'
t_ORL = r'||'
t_XORL = r'^'
t_NOTB = r'~'
t_ANDB = r'&'
t_ORB = r'|'
t_XORB = r'^'
t_SHIFTA = r'<<'
t_SHIFTB = r'>>'
t_IGUALR = r'=='
t_NOIGUALR = r'!='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_MAYORR = r'>'
t_MENORR = r'<'
t_CORA = r'('
t_CORB = r')'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print("Illegal character %s",t.value[0])
    t.lexer.skip(1)

lex.lex(debug=0)

