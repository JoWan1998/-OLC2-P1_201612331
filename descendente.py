from wdes import *
import re

#------------------- lexico --------------------
# ' generacion de tokens
# -> tk -> id, value -> value is a pure expression

keywords = [
    {'id': 'IF','value': r'if','tipo': 'reserved_word'},
    {'id': 'GOTO','value': r'goto','tipo': 'reserved_word'},
    {'id': 'READ','value': r'read','tipo': 'reserved_word'},
    {'id': 'PRINT','value': r'print','tipo': 'reserved_word'},
    {'id': 'UNSET','value': r'unset','tipo': 'reserved_word'},
    {'id': 'EXIT','value': r'exit','tipo': 'reserved_word'},
    {'id': 'ABS','value': r'abs','tipo': 'reserved_word'},
    {'id': 'ARRAY','value': r'array','tipo': 'reserved_word'},
    {'id': 'MAIN','value': r'main','tipo': 'reserved_word'},
    {'id': 'INT','value': r'int','tipo': 'reserved_word'},
    {'id': 'FLOAT','value': r'float','tipo': 'reserved_word'},
    {'id': 'CHAR','value': r'char','tipo': 'reserved_word'}
]

simbolos = [ '#','$',':','=','+','-','(',')',';','/','%','*','!','&','|','~','^','=','>','<','[',']','\'' ]

tokens = keywords + [
    {'id':'PARA','value': re.compile(r'\('),'tipo': 'token'},
    {'id':'VARIABLE','value': re.compile(r'(\$)(a|t|v|ra|s|sp)([0-9]+)'),'tipo': 'token'},
    {'id':'CORA','value': re.compile(r'\['),'tipo': 'token'},
    {'id':'CORB','value': re.compile(r'\]'),'tipo': 'token'},
    {'id':'PARB','value': re.compile(r'\)'),'tipo': 'token'},
    {'id':'ID','value': re.compile(r'[a-zA-Z][a-zA-Z0-9]*'),'tipo': 'token'},
    {'id':'IGUAL','value': re.compile(r'='),'tipo': 'token'},
    {'id':'NUMERO','value': re.compile(r'\d+'),'tipo': 'token'},
    {'id':'FLOAT','value': re.compile(r'\d+\.\d+'),'tipo': 'token'},
    {'id':'CARACTERES','value': re.compile(r'\'.*?\''),'tipo': 'token'},
    {'id':'MAS','value': re.compile(r'\+'),'tipo': 'token'},
    {'id':'MENOS','value': re.compile(r'-'),'tipo': 'token'},
    {'id':'PTCOMA','value': re.compile(r';'),'tipo': 'token'},
    {'id':'DIVIDIR','value': re.compile(r'/'),'tipo': 'token'},
    {'id':'RESIDUO','value': re.compile(r'%'),'tipo': 'token'},
    {'id':'MULTIPLICACION','value': re.compile(r'\*'),'tipo': 'token'},
    {'id':'NOTL','value': re.compile(r'!'),'tipo': 'token'},
    {'id':'ANDL','value': re.compile(r'&&'),'tipo': 'token'},
    {'id':'ORL','value': re.compile(r'\|\|'),'tipo': 'token'},
    {'id':'XORL','value': re.compile(r'xor'),'tipo': 'token'},
    {'id':'NOTB','value': re.compile(r'~'),'tipo': 'token'},
    {'id':'ANDB','value': re.compile(r'&'),'tipo': 'token'},
    {'id':'ORB','value': re.compile(r'\|'),'tipo': 'token'},
    {'id':'XORB','value': re.compile(r'\^'),'tipo': 'token'},
    {'id':'IGUALR','value': re.compile(r'=='),'tipo': 'token'},
    {'id':'NOIGUALR','value': re.compile(r'!='),'tipo': 'token'},
    {'id':'MAYORR','value': re.compile(r'>'),'tipo': 'token'},
    {'id':'MENORR','value': re.compile(r'<'),'tipo': 'token'},
    {'id':'DOSPUNTOS','value': re.compile(r':'),'tipo': 'token'},
    {'id':'COMENTARIO','value': re.compile(r'\#\.'),'tipo': 'token'}
]


def parserDes(data):
    lexico = lexicoD.wlex(data)
    lexico.lexems = tokens
    lexico.symbols = simbolos
    lexico.wlexs()
