
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftMULTIPLICACIONDIVIDIRleftRESIDUOANDB ANDL CHAR CORA CORB DIVIDIR DOSPUNTOS FLOAT ID IGUAL IGUALR INT MAS MAYORR MENORR MENOS MULTIPLICACION NEWLINE NOIGUALR NOTB NOTL ORB ORL PARA PARB PTCOMA RESIDUO VARIABLE XORB XORL abs array char exit float goto if int main print read unsetS : ESTRUCTURAMAINS : errorESTRUCTURAMAIN : main DOSPUNTOS PRECUERPOPRECUERPO : PRECUERPO CUERPOPRECUERPO : CUERPOCUERPO : ETIQUETA\n              | GOTO_LABEL\n              | ASIGNACION\n              | DESTRUYE_VARIABLE\n              | IMPRIME\n              | ESTRUCTURA_IF\n              | EXITETIQUETA : ID DOSPUNTOS PRECUERPOGOTO_LABEL : goto ID PTCOMAASIGNACION : NORMAL PTCOMA\n                  | ARRAY PTCOMANORMAL : VARIABLE IGUAL EXPRESIONARRAY : VARIABLE CORA EXPRESION CORB IGUAL EXPRESIONEXPRESION : VALORVALOR : VARIABLEVALOR : LLAMADA_ARREGLOLLAMADA_ARREGLO : VARIABLE CORA EXPRESION CORBVALOR : INTVALOR : FLOATVALOR : CHARVALOR : array PARA PARBVALOR : read PARA PARBEXPRESION : ARITMETICASARITMETICAS : MENOS VALORARITMETICAS : VALOR MAS VALOR\n                   | VALOR MENOS VALOR\n                   | VALOR MULTIPLICACION VALOR\n                   | VALOR DIVIDIR VALOR\n                   | VALOR RESIDUO VALORARITMETICAS : abs PARA VALOR PARBEXPRESION : LOGICASLOGICAS : NOTL VALORLOGICAS : VALOR ANDL VALOR\n               | VALOR ORL VALOR\n               | VALOR XORL VALOREXPRESION : RELACIONALRELACIONAL : VALOR IGUALR VALOR\n                  | VALOR NOIGUALR VALOR\n                  | VALOR MAYORR IGUALR VALOR\n                  | VALOR MENORR IGUALR VALOR\n                  | VALOR MAYORR VALOR\n                  | VALOR MENORR VALOREXPRESION : BITBIT : NOTB VALORBIT : VALOR ANDB VALOR\n           | VALOR ORB VALOR\n           | VALOR XORB VALOR\n           | VALOR MENORR MENORR VALOR\n           | VALOR MAYORR MAYORR VALOREXPRESION : CONVERSIONCONVERSION : PARA TIPO_CONVERSION PARB VALORTIPO_CONVERSION : int\n                       | char\n                       | floatEXPRESION : PUNTEROPUNTERO : ANDB VARIABLEESTRUCTURA_IF : if PARA EXPRESION PARB goto ID PTCOMADESTRUYE_VARIABLE : unset PARA VARIABLE PARBIMPRIME : print PARA VALOR PARB PTCOMAEXIT : exit PTCOMA'
    
_lr_action_items = {'error':([0,],[3,]),'main':([0,],[4,]),'$end':([1,2,3,6,7,8,9,10,11,12,13,14,24,27,28,34,35,36,62,118,129,],[0,-1,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-4,-15,-16,-65,-13,-14,-63,-64,-62,]),'DOSPUNTOS':([4,15,],[5,25,]),'ID':([5,6,7,8,9,10,11,12,13,14,16,24,25,27,28,34,35,36,62,118,119,129,],[15,15,-5,-6,-7,-8,-9,-10,-11,-12,26,-4,15,-15,-16,-65,15,-14,-63,-64,128,-62,]),'goto':([5,6,7,8,9,10,11,12,13,14,24,25,27,28,34,35,36,62,92,118,129,],[16,16,-5,-6,-7,-8,-9,-10,-11,-12,-4,16,-15,-16,-65,16,-14,-63,119,-64,-62,]),'unset':([5,6,7,8,9,10,11,12,13,14,24,25,27,28,34,35,36,62,118,129,],[19,19,-5,-6,-7,-8,-9,-10,-11,-12,-4,19,-15,-16,-65,19,-14,-63,-64,-62,]),'print':([5,6,7,8,9,10,11,12,13,14,24,25,27,28,34,35,36,62,118,129,],[21,21,-5,-6,-7,-8,-9,-10,-11,-12,-4,21,-15,-16,-65,21,-14,-63,-64,-62,]),'if':([5,6,7,8,9,10,11,12,13,14,24,25,27,28,34,35,36,62,118,129,],[22,22,-5,-6,-7,-8,-9,-10,-11,-12,-4,22,-15,-16,-65,22,-14,-63,-64,-62,]),'exit':([5,6,7,8,9,10,11,12,13,14,24,25,27,28,34,35,36,62,118,129,],[23,23,-5,-6,-7,-8,-9,-10,-11,-12,-4,23,-15,-16,-65,23,-14,-63,-64,-62,]),'VARIABLE':([5,6,7,8,9,10,11,12,13,14,24,25,27,28,29,30,31,32,33,34,35,36,54,56,57,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,86,105,106,108,109,114,117,118,129,],[20,20,-5,-6,-7,-8,-9,-10,-11,-12,-4,20,-15,-16,37,38,38,38,38,-65,20,-14,38,38,38,89,-63,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-64,-62,]),'PTCOMA':([17,18,23,26,38,39,40,41,42,43,44,45,46,47,48,49,50,85,87,88,89,91,94,95,96,97,98,99,100,101,102,103,104,107,110,111,112,113,115,120,121,122,123,124,125,126,127,128,],[27,28,34,36,-20,-17,-19,-28,-36,-41,-48,-55,-60,-21,-23,-24,-25,-29,-37,-49,-61,118,-30,-31,-32,-33,-34,-38,-39,-40,-42,-43,-46,-47,-50,-51,-52,-26,-27,-22,-54,-44,-53,-45,-56,-35,-18,129,]),'PARA':([19,21,22,30,31,33,51,53,55,63,117,],[29,32,33,52,52,52,79,84,86,52,52,]),'IGUAL':([20,90,],[30,117,]),'CORA':([20,38,],[31,63,]),'INT':([30,31,32,33,54,56,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,86,105,106,108,109,114,117,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'FLOAT':([30,31,32,33,54,56,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,86,105,106,108,109,114,117,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'CHAR':([30,31,32,33,54,56,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,86,105,106,108,109,114,117,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'array':([30,31,32,33,54,56,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,86,105,106,108,109,114,117,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'read':([30,31,32,33,54,56,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,86,105,106,108,109,114,117,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'MENOS':([30,31,33,38,40,47,48,49,50,63,113,115,117,120,],[54,54,54,-20,65,-21,-23,-24,-25,54,-26,-27,54,-22,]),'abs':([30,31,33,63,117,],[55,55,55,55,55,]),'NOTL':([30,31,33,63,117,],[56,56,56,56,56,]),'NOTB':([30,31,33,63,117,],[57,57,57,57,57,]),'ANDB':([30,31,33,38,40,47,48,49,50,63,113,115,117,120,],[58,58,58,-20,76,-21,-23,-24,-25,58,-26,-27,58,-22,]),'PARB':([37,38,40,41,42,43,44,45,46,47,48,49,50,60,61,79,80,81,82,83,84,85,87,88,89,94,95,96,97,98,99,100,101,102,103,104,107,110,111,112,113,115,116,120,121,122,123,124,125,126,],[62,-20,-19,-28,-36,-41,-48,-55,-60,-21,-23,-24,-25,91,92,113,114,-57,-58,-59,115,-29,-37,-49,-61,-30,-31,-32,-33,-34,-38,-39,-40,-42,-43,-46,-47,-50,-51,-52,-26,-27,126,-22,-54,-44,-53,-45,-56,-35,]),'MAS':([38,40,47,48,49,50,113,115,120,],[-20,64,-21,-23,-24,-25,-26,-27,-22,]),'MULTIPLICACION':([38,40,47,48,49,50,113,115,120,],[-20,66,-21,-23,-24,-25,-26,-27,-22,]),'DIVIDIR':([38,40,47,48,49,50,113,115,120,],[-20,67,-21,-23,-24,-25,-26,-27,-22,]),'RESIDUO':([38,40,47,48,49,50,113,115,120,],[-20,68,-21,-23,-24,-25,-26,-27,-22,]),'ANDL':([38,40,47,48,49,50,113,115,120,],[-20,69,-21,-23,-24,-25,-26,-27,-22,]),'ORL':([38,40,47,48,49,50,113,115,120,],[-20,70,-21,-23,-24,-25,-26,-27,-22,]),'XORL':([38,40,47,48,49,50,113,115,120,],[-20,71,-21,-23,-24,-25,-26,-27,-22,]),'IGUALR':([38,40,47,48,49,50,74,75,113,115,120,],[-20,72,-21,-23,-24,-25,106,109,-26,-27,-22,]),'NOIGUALR':([38,40,47,48,49,50,113,115,120,],[-20,73,-21,-23,-24,-25,-26,-27,-22,]),'MAYORR':([38,40,47,48,49,50,74,113,115,120,],[-20,74,-21,-23,-24,-25,105,-26,-27,-22,]),'MENORR':([38,40,47,48,49,50,75,113,115,120,],[-20,75,-21,-23,-24,-25,108,-26,-27,-22,]),'ORB':([38,40,47,48,49,50,113,115,120,],[-20,77,-21,-23,-24,-25,-26,-27,-22,]),'XORB':([38,40,47,48,49,50,113,115,120,],[-20,78,-21,-23,-24,-25,-26,-27,-22,]),'CORB':([38,40,41,42,43,44,45,46,47,48,49,50,59,85,87,88,89,93,94,95,96,97,98,99,100,101,102,103,104,107,110,111,112,113,115,120,121,122,123,124,125,126,],[-20,-19,-28,-36,-41,-48,-55,-60,-21,-23,-24,-25,90,-29,-37,-49,-61,120,-30,-31,-32,-33,-34,-38,-39,-40,-42,-43,-46,-47,-50,-51,-52,-26,-27,-22,-54,-44,-53,-45,-56,-35,]),'int':([52,],[81,]),'char':([52,],[82,]),'float':([52,],[83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'ESTRUCTURAMAIN':([0,],[2,]),'PRECUERPO':([5,25,],[6,35,]),'CUERPO':([5,6,25,35,],[7,24,7,24,]),'ETIQUETA':([5,6,25,35,],[8,8,8,8,]),'GOTO_LABEL':([5,6,25,35,],[9,9,9,9,]),'ASIGNACION':([5,6,25,35,],[10,10,10,10,]),'DESTRUYE_VARIABLE':([5,6,25,35,],[11,11,11,11,]),'IMPRIME':([5,6,25,35,],[12,12,12,12,]),'ESTRUCTURA_IF':([5,6,25,35,],[13,13,13,13,]),'EXIT':([5,6,25,35,],[14,14,14,14,]),'NORMAL':([5,6,25,35,],[17,17,17,17,]),'ARRAY':([5,6,25,35,],[18,18,18,18,]),'EXPRESION':([30,31,33,63,117,],[39,59,61,93,127,]),'VALOR':([30,31,32,33,54,56,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,86,105,106,108,109,114,117,],[40,40,60,40,85,87,88,40,94,95,96,97,98,99,100,101,102,103,104,107,110,111,112,116,121,122,123,124,125,40,]),'ARITMETICAS':([30,31,33,63,117,],[41,41,41,41,41,]),'LOGICAS':([30,31,33,63,117,],[42,42,42,42,42,]),'RELACIONAL':([30,31,33,63,117,],[43,43,43,43,43,]),'BIT':([30,31,33,63,117,],[44,44,44,44,44,]),'CONVERSION':([30,31,33,63,117,],[45,45,45,45,45,]),'PUNTERO':([30,31,33,63,117,],[46,46,46,46,46,]),'LLAMADA_ARREGLO':([30,31,32,33,54,56,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,86,105,106,108,109,114,117,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'TIPO_CONVERSION':([52,],[80,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> ESTRUCTURAMAIN','S',1,'p_S','ascendente.py',20),
  ('S -> error','S',1,'p_S_error','ascendente.py',25),
  ('ESTRUCTURAMAIN -> main DOSPUNTOS PRECUERPO','ESTRUCTURAMAIN',3,'p_ESTRUCTURAMAIN','ascendente.py',30),
  ('PRECUERPO -> PRECUERPO CUERPO','PRECUERPO',2,'p_PRECUERPO','ascendente.py',35),
  ('PRECUERPO -> CUERPO','PRECUERPO',1,'p_PRECUERPO_CUERPO','ascendente.py',41),
  ('CUERPO -> ETIQUETA','CUERPO',1,'p_CUERPO','ascendente.py',46),
  ('CUERPO -> GOTO_LABEL','CUERPO',1,'p_CUERPO','ascendente.py',47),
  ('CUERPO -> ASIGNACION','CUERPO',1,'p_CUERPO','ascendente.py',48),
  ('CUERPO -> DESTRUYE_VARIABLE','CUERPO',1,'p_CUERPO','ascendente.py',49),
  ('CUERPO -> IMPRIME','CUERPO',1,'p_CUERPO','ascendente.py',50),
  ('CUERPO -> ESTRUCTURA_IF','CUERPO',1,'p_CUERPO','ascendente.py',51),
  ('CUERPO -> EXIT','CUERPO',1,'p_CUERPO','ascendente.py',52),
  ('ETIQUETA -> ID DOSPUNTOS PRECUERPO','ETIQUETA',3,'p_ETIQUETA','ascendente.py',58),
  ('GOTO_LABEL -> goto ID PTCOMA','GOTO_LABEL',3,'p_GOTO_LABEL','ascendente.py',63),
  ('ASIGNACION -> NORMAL PTCOMA','ASIGNACION',2,'p_ASIGNACION','ascendente.py',69),
  ('ASIGNACION -> ARRAY PTCOMA','ASIGNACION',2,'p_ASIGNACION','ascendente.py',70),
  ('NORMAL -> VARIABLE IGUAL EXPRESION','NORMAL',3,'p_NORMAL','ascendente.py',75),
  ('ARRAY -> VARIABLE CORA EXPRESION CORB IGUAL EXPRESION','ARRAY',6,'p_ARRAY','ascendente.py',80),
  ('EXPRESION -> VALOR','EXPRESION',1,'p_EXPRESION','ascendente.py',85),
  ('VALOR -> VARIABLE','VALOR',1,'p_VALOR_VARIABLE','ascendente.py',90),
  ('VALOR -> LLAMADA_ARREGLO','VALOR',1,'p_VALOR_LLAMADA_ARREGLO','ascendente.py',95),
  ('LLAMADA_ARREGLO -> VARIABLE CORA EXPRESION CORB','LLAMADA_ARREGLO',4,'p_LLAMADA_ARREGLO','ascendente.py',100),
  ('VALOR -> INT','VALOR',1,'p_VALOR_NUMERO','ascendente.py',106),
  ('VALOR -> FLOAT','VALOR',1,'p_VALOR_FLOAT','ascendente.py',111),
  ('VALOR -> CHAR','VALOR',1,'p_VALOR_CARACTER','ascendente.py',116),
  ('VALOR -> array PARA PARB','VALOR',3,'p_VALOR_NUEVO_ARREGLO','ascendente.py',121),
  ('VALOR -> read PARA PARB','VALOR',3,'p_VALOR_LEER','ascendente.py',127),
  ('EXPRESION -> ARITMETICAS','EXPRESION',1,'p_EXPRESION_ARITMETICAS','ascendente.py',131),
  ('ARITMETICAS -> MENOS VALOR','ARITMETICAS',2,'p_ARITMETICAS_NEGATIVO','ascendente.py',135),
  ('ARITMETICAS -> VALOR MAS VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',139),
  ('ARITMETICAS -> VALOR MENOS VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',140),
  ('ARITMETICAS -> VALOR MULTIPLICACION VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',141),
  ('ARITMETICAS -> VALOR DIVIDIR VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',142),
  ('ARITMETICAS -> VALOR RESIDUO VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',143),
  ('ARITMETICAS -> abs PARA VALOR PARB','ARITMETICAS',4,'p_ARITMETICAS_ABS','ascendente.py',157),
  ('EXPRESION -> LOGICAS','EXPRESION',1,'p_EXPRESION_LOGICAS','ascendente.py',161),
  ('LOGICAS -> NOTL VALOR','LOGICAS',2,'p_LOGICAS_NOT','ascendente.py',165),
  ('LOGICAS -> VALOR ANDL VALOR','LOGICAS',3,'p_LOGICAS','ascendente.py',169),
  ('LOGICAS -> VALOR ORL VALOR','LOGICAS',3,'p_LOGICAS','ascendente.py',170),
  ('LOGICAS -> VALOR XORL VALOR','LOGICAS',3,'p_LOGICAS','ascendente.py',171),
  ('EXPRESION -> RELACIONAL','EXPRESION',1,'p_EXPRESION_RELACIONAL','ascendente.py',181),
  ('RELACIONAL -> VALOR IGUALR VALOR','RELACIONAL',3,'p_RELACIONAL','ascendente.py',185),
  ('RELACIONAL -> VALOR NOIGUALR VALOR','RELACIONAL',3,'p_RELACIONAL','ascendente.py',186),
  ('RELACIONAL -> VALOR MAYORR IGUALR VALOR','RELACIONAL',4,'p_RELACIONAL','ascendente.py',187),
  ('RELACIONAL -> VALOR MENORR IGUALR VALOR','RELACIONAL',4,'p_RELACIONAL','ascendente.py',188),
  ('RELACIONAL -> VALOR MAYORR VALOR','RELACIONAL',3,'p_RELACIONAL','ascendente.py',189),
  ('RELACIONAL -> VALOR MENORR VALOR','RELACIONAL',3,'p_RELACIONAL','ascendente.py',190),
  ('EXPRESION -> BIT','EXPRESION',1,'p_EXPRESION_BIT','ascendente.py',206),
  ('BIT -> NOTB VALOR','BIT',2,'p_BIT_NOT','ascendente.py',210),
  ('BIT -> VALOR ANDB VALOR','BIT',3,'p_BIT','ascendente.py',214),
  ('BIT -> VALOR ORB VALOR','BIT',3,'p_BIT','ascendente.py',215),
  ('BIT -> VALOR XORB VALOR','BIT',3,'p_BIT','ascendente.py',216),
  ('BIT -> VALOR MENORR MENORR VALOR','BIT',4,'p_BIT','ascendente.py',217),
  ('BIT -> VALOR MAYORR MAYORR VALOR','BIT',4,'p_BIT','ascendente.py',218),
  ('EXPRESION -> CONVERSION','EXPRESION',1,'p_EXPRESION_CONVERSION','ascendente.py',231),
  ('CONVERSION -> PARA TIPO_CONVERSION PARB VALOR','CONVERSION',4,'p_CONVERSION','ascendente.py',235),
  ('TIPO_CONVERSION -> int','TIPO_CONVERSION',1,'p_TIPO_CONVERSION','ascendente.py',240),
  ('TIPO_CONVERSION -> char','TIPO_CONVERSION',1,'p_TIPO_CONVERSION','ascendente.py',241),
  ('TIPO_CONVERSION -> float','TIPO_CONVERSION',1,'p_TIPO_CONVERSION','ascendente.py',242),
  ('EXPRESION -> PUNTERO','EXPRESION',1,'p_EXPRESION_PUNTERO','ascendente.py',246),
  ('PUNTERO -> ANDB VARIABLE','PUNTERO',2,'p_PUNTERO','ascendente.py',250),
  ('ESTRUCTURA_IF -> if PARA EXPRESION PARB goto ID PTCOMA','ESTRUCTURA_IF',7,'p_ESTRUCTURA_IF','ascendente.py',254),
  ('DESTRUYE_VARIABLE -> unset PARA VARIABLE PARB','DESTRUYE_VARIABLE',4,'p_DESTRUYE_VARIABLE','ascendente.py',258),
  ('IMPRIME -> print PARA VALOR PARB PTCOMA','IMPRIME',5,'p_IMPRIME','ascendente.py',262),
  ('EXIT -> exit PTCOMA','EXIT',2,'p_EXIT','ascendente.py',266),
]
