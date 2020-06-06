from wdes import *
import re

#------------------- lexico --------------------
# ' generacion de tokens
# -> tk -> id, value -> value is a pure expression

keywords = [
    {'id': 'if','value': r'if','tk': 1},
    {'id': 'goto','value': r'goto','tk': 2},
    {'id': 'read','value': r'read','tk': 3},
    {'id': 'print','value': r'print','tk': 4},
    {'id': 'unset','value': r'unset','tk': 5},
    {'id': 'exit','value': r'exit','tk': 6},
    {'id': 'abs','value': r'abs','tk': 7},
    {'id': 'array','value': r'array','tk': 8},
    {'id': 'main','value': r'main','tk': 9},
    {'id': 'int','value': r'int','tk': 10},
    {'id': 'float','value': r'float','tk': 11},
    {'id': 'char','value': r'char','tk': 12}
]

simbolos = [ '#','$',':','=','+','-','(',')',';','/','%','*','!','&','|','~','^','=','>','<','[',']','\'' ]

tokens = keywords + [
    {'id': 'para','value': re.compile(r'\('),'tk': 13},
    {'id': 'variable','value': re.compile(r'(\$)(a|t|v|ra|s|sp)([0-9]+)'),'tk': 14},
    {'id': 'cora','value': re.compile(r'\['),'tk': 15},
    {'id': 'corb','value': re.compile(r'\]'),'tk': 16},
    {'id': 'parb','value': re.compile(r'\)'),'tk': 17},
    {'id': 'identificador','value': re.compile(r'[a-zA-Z][a-zA-Z0-9]*'),'tk': 18},
    {'id': 'igual','value': re.compile(r'='),'tk': 19},
    {'id': 'numero','value': re.compile(r'\d+'),'tk': 20},
    {'id': 'decimal','value': re.compile(r'\d+\.\d+'),'tk': 21},
    {'id': 'caracteres','value': re.compile(r'\'.*?\''),'tk': 22},
    {'id': 'mas','value': re.compile(r'\+'),'tk': 23},
    {'id': 'menos','value': re.compile(r'-'),'tk': 24},
    {'id': 'ptcoma','value': re.compile(r';'),'tk': 25},
    {'id': 'dividir','value': re.compile(r'/'),'tk': 26},
    {'id': 'residuo','value': re.compile(r'%'),'tk': 27},
    {'id': 'multiplicacion','value': re.compile(r'\*'),'tk': 28},
    {'id': 'notl','value': re.compile(r'!'),'tk': 29},
    {'id': 'andl','value': re.compile(r'&&'),'tk': 30},
    {'id': 'orl','value': re.compile(r'\|\|'),'tk': 31},
    {'id': 'xorl','value': re.compile(r'xor'),'tk': 32},
    {'id': 'notb','value': re.compile(r'~'),'tk': 33},
    {'id': 'andb','value': re.compile(r'&'),'tk': 34},
    {'id': 'orb','value': re.compile(r'\|'),'tk': 35},
    {'id': 'xorb','value': re.compile(r'\^'),'tk': 36},
    {'id': 'igualr','value': re.compile(r'=='),'tk': 37},
    {'id': 'notigualr','value': re.compile(r'!='),'tk': 38},
    {'id': 'mayorr','value': re.compile(r'>'),'tk': 39},
    {'id': 'menorr','value': re.compile(r'<'),'tk': 40},
    {'id': 'dospuntos','value': re.compile(r':'),'tk': 41},
    {'id': 'comentario','value': re.compile(r'\#\.'),'tk': 'token'}
]

#ESTADOS DEBEN DE POSEER DIFERENTES IDENTIFICADORES QUE LAS PALABRAS RESERVADAS
#PRODUCCIONES -> PALABRAS RESERVADAS Y/O TOKENS DEBEN DE INGRESARSE EN MINISCULA -> S -> inicio dospuntos VALOR
#siendo S y VALOR AMBOS ESTADOS

estados = [
    {'id':'S','producciones': [
        ['INICIO']
    ],
     'st': 1},
    {'id':'INICIO', 'producciones': [
        ['main','dospuntos','PRECUERPO']
    ],
     'st': 2},
    {'id': 'PRECUERPO', 'producciones': [
        ['CUERPO','PRECUERPO_F']
    ],
     'st': 3},
    {'id': 'PRECUERPO_F', 'producciones': [
        ['CUERPO','PRECUERPO_F'],
        ['EMPTY']
    ],
     'st': 4},
    {'id': 'CUERPO', 'producciones': [
        ['ETIQUETA'],
        ['ASIGNACION'],
        ['SALTO'],
        ['ESTRUCTURA_IF'],
        ['DESTRUYE_VARIABLE'],
        ['IMPRIME'],
        ['EXIT']
    ],
     'st': 5},
    {'id': 'ETIQUETA', 'producciones': [
        ['identificador','dospuntos','PRECUERPO']
    ],
     'st': 6},
    {'id': 'ASIGNACION', 'producciones': [
        ['NORMAL'],
        ['ARREGLO']
    ],
     'st': 7},
    {'id': 'NORMAL', 'producciones': [
        ['variable','dospuntos','EXPRESION','ptcoma']
    ],
     'st': 8},
    {'id': 'ARREGLO', 'producciones': [
        ['variable','LISTA_POS','dospuntos','EXPRESION','ptcoma']
    ],
     'st': 9},
    {'id': 'LISTA_POS', 'producciones':[
        ['POS','LISTAPOS_F']
    ],
     'st': 10},
    {'id': 'LISTA_POS_F', 'producciones':[
        ['POS','LISTAPOS_F'],
        ['EMPTY']
    ],
     'st': 11},
    {'id': 'POS', 'producciones': [
        ['cora','EXPRESION','corb']
    ],
     'st': 12},
    {'id': 'EXPRESION', 'producciones': [
        ['ARITMETICAS'],
        ['LOGICAS'],
        ['RELACIONALES'],
        ['BIT'],
        ['CONVERSION'],
        ['PUNTERO'],
        ['VALOR']
    ],
     'st': 13},
    {'id': 'ARITMETICAS', 'producciones': [
        ['menos','VALOR'],
        ['VALOR','mas','VALOR'],
        ['VALOR','menos','VALOR'],
        ['VALOR','dividir','VALOR'],
        ['VALOR','multiplicacion','VALOR'],
        ['VALOR','residuo','VALOR'],
        ['abs','para','VALOR','parb']
    ],
     'st': 14},
    {'id': 'LOGICAS', 'producciones': [
        ['not','VALOR'],
        ['VALOR','and','VALOR'],
        ['VALOR','or','VALOR'],
        ['VALOR','xor','VALOR']
    ],
     'st': 15},
    {'id': 'RELACIONALES', 'producciones': [
        ['VALOR','igualr','VALOR'],
        ['VALOR','notigualr','VALOR'],
        ['VALOR','mayorr','VALOR'],
        ['VALOR','menorr','VALOR'],
        ['VALOR','mayorr','igual','VALOR'],
        ['VALOR','menorr','igual','VALOR']
    ],
     'st': 16},
    {'id': 'BIT', 'producciones': [
        ['notb','VALOR'],
        ['VALOR','andb','VALOR'],
        ['VALOR','orb','VALOR'],
        ['VALOR','xorb','VALOR'],
        ['VALOR','mayorr','mayorr','VALOR'],
        ['VALOR','menorr','menorr','VALOR']
    ],
     'st': 17},
    {'id': 'CONVERSION', 'producciones': [
        ['para','TIPOCONV','parb','VALOR']
    ],
     'st': 18},
    {'id': 'PUNTERO', 'producciones': [
        ['andb','variable']
    ],
     'st': 19},
    {'id': 'VALOR', 'producciones': [
        ['variable'],
        ['LLAMADA_ARREGLO'],
        ['numero'],
        ['decimal'],
        ['caracteres'],
        ['NUEVO_ARREGLO'],
        ['LEER']
    ],
     'st': 20},
    {'id': 'LLAMADA_ARREGLO', 'producciones': [
        ['variable','LISTA_POS']
    ],
     'st': 21},
    {'id': 'NUEVO_ARREGLO', 'producciones': [
        ['array','para','parb']
    ],
     'st': 22},
    {'id': 'ESTRUCTURA_IF', 'producciones': [
        ['if','para','EXPRESION','parb','goto','identificador','ptcoma']
    ],
     'st': 23},
    {'id': 'TIPOCONV', 'producciones': [
        ['int'],
        ['char'],
        ['float']
    ],
     'st': 24},
    {'id': 'EXIT', 'producciones': [
        ['exit','ptcoma']
    ],
     'st': 25},
    {'id': 'LEER', 'producciones': [
        ['read','para','parb']
    ],
     'st': 26},
    {'id': 'SALTO', 'producciones':
     [
         ['goto','identificador']
     ],
     'st': 27},
    {'id': 'IMPRIME', 'producciones': [
        ['print','para','EXPRESION','parb']
    ],
     'st': 28},
    {'id': 'DESTRUYE_VARIABLE', 'producciones': [
        ['unset','para','EXPRESION','parb']
    ],
     'st': 29}
]

def parserDes(data):
    lexico = lexicoD.wlex(data)
    lexico.lexems = tokens
    lexico.symbols = simbolos
    lexico.wlexs()
    
