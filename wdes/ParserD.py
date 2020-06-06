####PARSER, ENGINE PARA PARSEO DE TOKENS
###JOSE WANNAN,2020
###UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

class state:

    def __init__(self):
        self.id = ''
        self.st = 0
        self.productions = []

class Parser:
    def __init__(self):
        self.numlinea = 0
        self.tableProductions = []
