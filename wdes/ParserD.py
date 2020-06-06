####PARSER, ENGINE PARA PARSEO DE TOKENS
###JOSE WANNAN,2020
###UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

from instrucciones import *
from operaciones import *
from estructuras import *

class state:

    def __init__(self):
        self.id = ''
        self.st = 0
        self.productions = []

class Nodo:

    def __init__(self):
        self.value = ''
        self.linea = 0
        self.columna = 0
        self.hijos = []

class Parser:
    def __init__(self):
        self.numlinea = 0
        self.tableProductions = []
        self.estado_incial = None
        self.raiz = None

    def inicio(self,tokens):
        tk = tokens.pop()




    def parse(self,tokens):
        tk = tokens.pop()
        if tk.id == 'main':
            main = tk
            tk = tokens.pop()
            if tk.id == 'dospuntos':
                tk = tokens.pop()
                self.raiz = etiqueta(main.value,TIPO_INSTRUCCION.BANDERA,self.inicio(tokens),True)








