#ANALIZADOR DESCENDIENTE

####### tlex ##########
#   class -> token
#   definida para la obtencion de los token, los cuales se enviaran al parser para su definicion sintactica

__version__ = '1.0.0'

import re

class wtlex:
    def __init__(self):
        self._token = None
        self._lexema = None         # r'{}' -> definida por la expresion regular
        self._lineapos = None       # posicion en la que se localizo el token
        self._columnstart = None    # posicion inicial del token
        self._columnend = None      # posicion final del token
        self._value = None          # valor obtenido


    @property
    def token(self):
        return self._token

    @property
    def lineapos(self):
        return self._lineapos

    @property
    def columnastart(self):
        return self._columnstart

    @property
    def columnaend(self):
        return self._columnend

    @property
    def value(self):
        return self._value

    @property
    def lexema(self):
        return self._lexema

    @token.setter
    def token(self,value):
        self._token = value

    @token.getter
    def token(self):
        return self._token

    @lexema.setter
    def lexema(self,value):
            self._lexema = value  #pattern


    @lexema.getter
    def lexema(self):
        return self._lexema

    @lineapos.setter
    def lineapos(self,pos):
        if isinstance(pos,int):
            self._lineapos = pos
        else:
            raise ValueError('dont a int')

    @lineapos.getter
    def lineapo(self):
        return self._lineapos

    @columnastart.setter
    def columnastart(self,pos):
        if isinstance(pos,int):
            self._columnstart = pos
        else:
            raise ValueError('dont a int')

    @columnastart.getter
    def columnastart(self):
        return self._columnstart

    @columnaend.setter
    def columnaend(self,pos):
        if isinstance(pos,int):
            self._columnend = pos
        else:
            raise ValueError('dont a int')

    @columnaend.getter
    def columnaend(self):
        return self._columnend

    @value.setter
    def value(self,valor):
        self._value = valor

    @value.getter
    def value(self):
        return self._value

class wSymbols:
    def __init__(self):
        self.columnainicio = 0
        self.columnafin = 0
        self.linea = 0
        self.value = ''

##### lexico ########
# class -> wlex
# definida para la ejecucion de tokenizacion inicial para argumentar

class wlex:

    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data
        self.lexems = []                # lexems -> lexemas para adquirir los token lexicos
        self.lineaActual = None
        self.columnaActual = None
        self.columnaFinal = None
        self.tokens = []                # tokens -> para producciones sintacticas
        self.symbols = []
        self.LexSymbols = []
        self.lexicalErrors = []

    def generateSymbols(self):

        data = self.data
        #print(data)
        numline = 1
        symbols = self.symbols
        words = []
        words1 = []

        for linea in data:

            line = list(linea)
            value = ''

            columnainicio= 0
            columnafin = 0


            for ln in line:
                #print(value)
                intro = False
                for nn in symbols:
                    if ln == nn:
                        #print(ln)
                        if ln == '=':
                            if value == '=':
                                value += nn
                                vals = wSymbols()
                                vals.columnafin = columnafin
                                vals.columnainicio = columnainicio
                                vals.linea = numline
                                vals.value = value
                                words.append(vals)
                                value = ''
                                columnainicio = columnafin
                                columnafin += 1
                            else:
                                if value != '':
                                    vals = wSymbols()
                                    vals.columnafin = columnafin
                                    vals.columnainicio = columnainicio
                                    vals.linea = numline
                                    vals.value = value
                                    words.append(vals)
                                    value = ''
                                    columnafin += 1
                                    columnainicio = columnafin



                                else:
                                    value += nn
                                    columnafin += 1

                        elif ln == '!':
                            if value == '=':
                                value += nn
                                vals = wSymbols()
                                vals.columnafin = columnafin
                                vals.columnainicio = columnainicio
                                vals.linea = numline
                                vals.value = value
                                words.append(vals)
                                value = ''
                                columnainicio = columnafin
                                columnafin += 1
                            else:
                                if value != '':
                                    vals = wSymbols()
                                    vals.columnafin = columnafin
                                    vals.columnainicio = columnainicio
                                    vals.linea = numline
                                    vals.value = value
                                    words.append(vals)
                                    value = ''
                                    columnafin += 1
                                    columnainicio = columnafin


                                else:
                                    value += nn
                                    columnafin += 1

                        elif ln == '&':
                            if value == '&':
                                value += nn
                                vals = wSymbols()
                                vals.columnafin = columnafin
                                vals.columnainicio = columnainicio
                                vals.linea = numline
                                vals.value = value
                                words.append(vals)
                                value = ''
                                columnainicio = columnafin
                                columnafin += 1
                            else:
                                if value != '':
                                    vals = wSymbols()
                                    vals.columnafin = columnafin
                                    vals.columnainicio = columnainicio
                                    vals.linea = numline
                                    vals.value = value
                                    words.append(vals)
                                    value = ''
                                    columnafin += 1
                                    columnainicio = columnafin


                                else:
                                    value += nn
                                    columnafin += 1

                        elif ln == '|':
                            if value == '|':
                                value += nn
                                vals = wSymbols()
                                vals.columnafin = columnafin
                                vals.columnainicio = columnainicio
                                vals.linea = numline
                                vals.value = value
                                words.append(vals)
                                value = ''
                                columnainicio = columnafin
                                columnafin += 1
                            else:
                                if value != '':
                                    vals = wSymbols()
                                    vals.columnafin = columnafin
                                    vals.columnainicio = columnainicio
                                    vals.linea = numline
                                    vals.value = value
                                    words.append(vals)
                                    value = ''
                                    columnafin += 1
                                    columnainicio = columnafin


                                else:
                                    value += nn
                                    columnafin += 1

                        elif ln == '$':
                            #print('bb')
                            value += '$'
                            columnafin += 1

                        elif ln == '#':
                            #print('bs')
                            value += '#'
                            columnafin += 1
                        elif ln == '\'':
                            value += '\''
                            columnafin += 1
                        else:
                            #print(ln)
                            if value != '':
                                vals = wSymbols()
                                vals.columnafin = columnafin
                                vals.columnainicio = columnainicio
                                vals.linea = numline
                                vals.value = value
                                words.append(vals)
                                value = ''
                                columnainicio = columnafin
                                columnafin += 1

                                vals = wSymbols()
                                vals.columnafin = columnafin
                                vals.columnainicio = columnainicio
                                vals.linea = numline
                                vals.value = nn
                                words.append(vals)
                                columnainicio = columnafin
                            else:
                                vals = wSymbols()
                                vals.columnafin = columnafin
                                vals.columnainicio = columnainicio
                                vals.linea = numline
                                vals.value = value
                                words.append(vals)
                                value = ''
                                columnafin += 1
                                columnainicio = columnafin
                                vals = wSymbols()
                                vals.columnafin = columnafin
                                vals.columnainicio = columnainicio
                                vals.linea = numline
                                vals.value = nn
                                words.append(vals)
                                value = ''
                                columnafin += 1
                                columnainicio = columnafin


                        intro = True
                        break
                if not intro:

                    if ln == ' ':
                        if value != '':
                            vals = wSymbols()
                            vals.columnafin = columnafin
                            vals.columnainicio = columnainicio
                            vals.linea = numline
                            vals.value = value
                            words.append(vals)
                            value = ''
                            columnafin += 1
                            columnainicio = columnafin
                        else:
                            columnafin += 1
                            columnainicio = columnafin

                    elif re.match(r'[a-zA-Z0-9]',ln):
                        value += ln
                        #print(value)
                        columnafin += 1
                    elif ln != '\n' and ln !='\t':
                        if value != '':
                            vals = wSymbols()
                            vals.columnafin = columnafin
                            vals.columnainicio = columnainicio
                            vals.linea = numline
                            vals.value = value
                            words.append(vals)
                            value = ''
                            columnainicio = columnafin
                            columnafin += 1

                            vals = wSymbols()
                            vals.columnafin = columnafin
                            vals.columnainicio = columnainicio
                            vals.linea = numline
                            vals.value = ln
                            words.append(vals)
                            columnainicio = columnafin
                        else:
                            columnafin +=1
                            vals = wSymbols()
                            vals.columnafin = columnafin
                            vals.columnainicio = columnainicio
                            vals.linea = numline
                            vals.value = value
                            words.append(vals)
                            value = ''
                            columnainicio = columnafin
                    else:
                        #print("salto")
                        vals = wSymbols()
                        vals.columnafin = columnafin
                        vals.columnainicio = columnainicio
                        vals.linea = numline
                        vals.value = value
                        words.append(vals)
                        value = ''


            numline += 1

        for w in words:
           if w.value != ' ' and w.value != '':
               #print(w.value)
               words1.append(w)

        self.LexSymbols =[] + words1

    def generateTokens1(self):
        symbols = self.LexSymbols
        tokens = self.lexems
        tokenization = []
        errors = []
        for symbol in symbols:
            if not re.search(r'#',symbol.value):
                iserror = True
                for token in tokens:
                    #print(symbol)
                    match = re.match(token['value'],symbol.value)
                    if match:
                            tokencito = wtlex()
                            tokencito.token = token['id']
                            tokencito.value = symbol.value
                            tokencito.columnaend = symbol.columnafin
                            tokencito.columnastart = symbol.columnainicio
                            tokencito.lineapos = (symbol.linea)
                            tokencito.lexema = (token['value'])
                            print("token: "+token['id']+", linea: "+str(symbol.linea)+", columna: "+str(symbol.columnainicio))
                            if token['id'] != 'COMENTARIO':
                                tokenization.append(tokencito)
                            iserror = False
                            break

                if iserror:
                    print("Syntax Error  '" + symbol.value + "' in  linea: " + str(symbol.linea) + ", columna: " + str(symbol.columnainicio))
                    errors.append(symbol)

        self.tokens = tokenization
        self.lexicalErrors = errors

    def wlexs(self):
        self.generateSymbols()
        self.generateTokens1()

    def generateTokens(self):
        data = self.data
        numline = 0
        tokens = self.lexems
        tonekinazitation = []
        errors = []
        for linea in data:
            numline += 1
            columnaActual = 1
            ant = False
            now = False
            mg = 0
            gh = list(linea)
            for g in gh:
                if g == ' ':
                    columnaActual +=1
                    mg +=1
                else:
                    break
            linea = linea[mg:]

            while True:

                error = True
                print(linea)
                for token in tokens:
                        #token = tokend[0]
                        pattern = token['value']
                        match =  re.search(pattern,linea)
                        if match:
                            if token['id'] != 'COMENTARIO':
                                tokencito = wtlex()
                                tokencito.token = token['id']
                                tokencito.value = match.group()
                                tokencito.columnaend = match.end()
                                tokencito.columnastart = match.start()
                                tokencito.lineapos = (numline)
                                tokencito.lexema = (token['value'])
                                #print("token: "+token['id']+", linea: "+str(numline)+", columna: "+str(columnaActual))
                                tonekinazitation.append(tokencito)
                                error = False
                                ant = False
                                columnaActual += len(tokencito.value)
                                linea = linea[len(tokencito.value):]
                                columnaActual += len(tokencito.value)
                                mg = 0
                                gh = list(linea)
                                for g in gh:
                                    if g == ' ':
                                        columnaActual += 1
                                        mg +=1
                                    else:
                                        break
                                linea = linea[mg:]
                                break

                if error:
                    if ant:
                        now = True
                    else:
                        ant = True
                if ant and now:
                    break

            linea = re.sub(r'\n', '', linea)
            if linea != '':
                line = list(linea)
                for ln in line:
                    if ln != '' and ln != ' ':
                        msg = "Illegal caracter, token: '" + ln + "', linea: " + str(numline) + ", columna: " + str(columnaActual)
                        columnaActual += 1
                        errors.append(msg)
                    else:
                        columnaActual +=1

        for error in errors:
            print(error)







