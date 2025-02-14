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
        self.tokens = []
        self.estado_incial = None
        self.raiz = None
        self.errores = []

    def inicio(self):
        tk = self.tokens.pop()
        if tk.id == 'variable':
            valor = tk
            tk = self.tokens.pop()




    def parse(self):
        tk = self.tokens.pop()
        if tk.id == 'main':
            main = tk
            tk = self.tokens.pop()
            if tk.id == 'dospuntos':
                tk = self.tokens.pop()
                self.raiz = etiqueta(main.value,TIPO_INSTRUCCION.BANDERA,self.inicio(),True)
            

