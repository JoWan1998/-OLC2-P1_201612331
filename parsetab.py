
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftMULTIPLICACIONDIVIDIRleftRESIDUOANDB ANDL CHAR CORA CORB DIVIDIR DOSPUNTOS FLOAT ID IGUAL IGUALR INT MAS MAYORR MENORR MENOS MULTIPLICACION NEWLINE NOIGUALR NOTB NOTL ORB ORL PARA PARB PTCOMA RESIDUO VARIABLE XORB XORL abs array char exit float goto if int main print read unsetS : ESTRUCTURAMAINS : errorESTRUCTURAMAIN : main DOSPUNTOS PRECUERPOESTRUCTURAMAIN : error DOSPUNTOS PRECUERPOESTRUCTURAMAIN : main error PRECUERPOESTRUCTURAMAIN : main DOSPUNTOS errorPRECUERPO : PRECUERPO CUERPOPRECUERPO : CUERPOCUERPO : ETIQUETA\n              | GOTO_LABEL\n              | ASIGNACION\n              | DESTRUYE_VARIABLE\n              | IMPRIME\n              | ESTRUCTURA_IF\n              | EXITETIQUETA : ID DOSPUNTOS PRECUERPOGOTO_LABEL : goto ID PTCOMAASIGNACION : NORMAL PTCOMA\n                  | ARRAY PTCOMANORMAL : VARIABLE IGUAL EXPRESIONARRAY : VARIABLE LISTA_POS IGUAL EXPRESIONEXPRESION : VALORVALOR : VARIABLEVALOR : LLAMADA_ARREGLOVALOR : INTVALOR : FLOATVALOR : CHARVALOR : array PARA PARBVALOR : read PARA PARBEXPRESION : ARITMETICASARITMETICAS : MENOS VALORARITMETICAS : VALOR MAS VALOR\n                   | VALOR MENOS VALOR\n                   | VALOR MULTIPLICACION VALOR\n                   | VALOR DIVIDIR VALOR\n                   | VALOR RESIDUO VALORARITMETICAS : abs PARA VALOR PARBEXPRESION : LOGICASLOGICAS : NOTL VALORLOGICAS : VALOR ANDL VALOR\n               | VALOR ORL VALOR\n               | VALOR XORL VALOREXPRESION : RELACIONALRELACIONAL : VALOR IGUALR VALOR\n                  | VALOR NOIGUALR VALOR\n                  | VALOR MAYORR IGUALR VALOR\n                  | VALOR MENORR IGUALR VALOR\n                  | VALOR MAYORR VALOR\n                  | VALOR MENORR VALOREXPRESION : BITBIT : NOTB VALORBIT : VALOR ANDB VALOR\n           | VALOR ORB VALOR\n           | VALOR XORB VALOR\n           | VALOR MENORR MENORR VALOR\n           | VALOR MAYORR MAYORR VALORLLAMADA_ARREGLO : VARIABLE LISTA_POSLISTA_POS :  LISTA_POS POSLISTA_POS : POSPOS : CORA EXPRESION CORBEXPRESION : CONVERSIONCONVERSION : PARA TIPO_CONVERSION PARB VALORTIPO_CONVERSION : int\n                       | char\n                       | floatEXPRESION : PUNTEROPUNTERO : ANDB VARIABLEESTRUCTURA_IF : if PARA EXPRESION PARB goto ID PTCOMADESTRUYE_VARIABLE : unset PARA VALOR PARBIMPRIME : print PARA VALOR PARB PTCOMAEXIT : exit PTCOMA'
    
_lr_action_items = {'error':([0,4,6,],[3,7,27,]),'main':([0,],[4,]),'$end':([1,2,3,8,9,10,11,12,13,14,15,16,26,27,28,29,32,33,37,42,43,71,105,135,],[0,-1,-2,-4,-8,-9,-10,-11,-12,-13,-14,-15,-3,-6,-5,-7,-18,-19,-71,-16,-17,-69,-70,-68,]),'DOSPUNTOS':([3,4,17,],[5,6,30,]),'ID':([5,6,7,8,9,10,11,12,13,14,15,16,18,26,28,29,30,32,33,37,42,43,71,105,107,135,],[17,17,17,17,-8,-9,-10,-11,-12,-13,-14,-15,31,17,17,-7,17,-18,-19,-71,17,-17,-69,-70,129,-68,]),'goto':([5,6,7,8,9,10,11,12,13,14,15,16,26,28,29,30,32,33,37,42,43,71,80,105,135,],[18,18,18,18,-8,-9,-10,-11,-12,-13,-14,-15,18,18,-7,18,-18,-19,-71,18,-17,-69,107,-70,-68,]),'unset':([5,6,7,8,9,10,11,12,13,14,15,16,26,28,29,30,32,33,37,42,43,71,105,135,],[21,21,21,21,-8,-9,-10,-11,-12,-13,-14,-15,21,21,-7,21,-18,-19,-71,21,-17,-69,-70,-68,]),'print':([5,6,7,8,9,10,11,12,13,14,15,16,26,28,29,30,32,33,37,42,43,71,105,135,],[22,22,22,22,-8,-9,-10,-11,-12,-13,-14,-15,22,22,-7,22,-18,-19,-71,22,-17,-69,-70,-68,]),'if':([5,6,7,8,9,10,11,12,13,14,15,16,26,28,29,30,32,33,37,42,43,71,105,135,],[23,23,23,23,-8,-9,-10,-11,-12,-13,-14,-15,23,23,-7,23,-18,-19,-71,23,-17,-69,-70,-68,]),'exit':([5,6,7,8,9,10,11,12,13,14,15,16,26,28,29,30,32,33,37,42,43,71,105,135,],[24,24,24,24,-8,-9,-10,-11,-12,-13,-14,-15,24,24,-7,24,-18,-19,-71,24,-17,-69,-70,-68,]),'VARIABLE':([5,6,7,8,9,10,11,12,13,14,15,16,26,28,29,30,32,33,34,35,36,37,38,41,42,43,62,64,65,66,68,71,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,105,106,119,120,122,123,135,],[25,25,25,25,-8,-9,-10,-11,-12,-13,-14,-15,25,25,-7,25,-18,-19,45,45,45,-71,45,45,25,-17,45,45,45,100,45,-69,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-70,45,45,45,45,45,-68,]),'PTCOMA':([19,20,24,31,40,45,46,47,48,49,55,56,57,58,59,60,61,67,69,72,75,96,98,99,100,101,102,103,104,108,109,110,111,112,113,114,115,116,117,118,121,124,125,126,128,129,130,131,132,133,134,],[32,33,37,43,-59,-23,-24,-25,-26,-27,-22,-30,-38,-43,-50,-61,-66,-20,-58,-57,105,-31,-39,-51,-67,-21,-60,-28,-29,-32,-33,-34,-35,-36,-40,-41,-42,-44,-45,-48,-49,-52,-53,-54,-62,135,-56,-46,-55,-47,-37,]),'PARA':([21,22,23,36,38,41,50,51,63,68,],[34,35,36,53,53,53,73,74,97,53,]),'IGUAL':([25,39,40,69,102,],[38,68,-59,-58,-60,]),'CORA':([25,39,40,45,69,72,102,],[41,41,-59,41,-58,41,-60,]),'INT':([34,35,36,38,41,62,64,65,68,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,106,119,120,122,123,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'FLOAT':([34,35,36,38,41,62,64,65,68,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,106,119,120,122,123,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'CHAR':([34,35,36,38,41,62,64,65,68,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,106,119,120,122,123,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'array':([34,35,36,38,41,62,64,65,68,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,106,119,120,122,123,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'read':([34,35,36,38,41,62,64,65,68,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,106,119,120,122,123,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'MENOS':([36,38,40,41,45,46,47,48,49,55,68,69,72,102,103,104,],[62,62,-59,62,-23,-24,-25,-26,-27,82,62,-58,-57,-60,-28,-29,]),'abs':([36,38,41,68,],[63,63,63,63,]),'NOTL':([36,38,41,68,],[64,64,64,64,]),'NOTB':([36,38,41,68,],[65,65,65,65,]),'ANDB':([36,38,40,41,45,46,47,48,49,55,68,69,72,102,103,104,],[66,66,-59,66,-23,-24,-25,-26,-27,93,66,-58,-57,-60,-28,-29,]),'PARB':([40,44,45,46,47,48,49,52,54,55,56,57,58,59,60,61,69,72,73,74,76,77,78,79,96,98,99,100,102,103,104,108,109,110,111,112,113,114,115,116,117,118,121,124,125,126,127,128,130,131,132,133,134,],[-59,71,-23,-24,-25,-26,-27,75,80,-22,-30,-38,-43,-50,-61,-66,-58,-57,103,104,106,-63,-64,-65,-31,-39,-51,-67,-60,-28,-29,-32,-33,-34,-35,-36,-40,-41,-42,-44,-45,-48,-49,-52,-53,-54,134,-62,-56,-46,-55,-47,-37,]),'MAS':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,81,-58,-57,-60,-28,-29,]),'MULTIPLICACION':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,83,-58,-57,-60,-28,-29,]),'DIVIDIR':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,84,-58,-57,-60,-28,-29,]),'RESIDUO':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,85,-58,-57,-60,-28,-29,]),'ANDL':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,86,-58,-57,-60,-28,-29,]),'ORL':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,87,-58,-57,-60,-28,-29,]),'XORL':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,88,-58,-57,-60,-28,-29,]),'IGUALR':([40,45,46,47,48,49,55,69,72,91,92,102,103,104,],[-59,-23,-24,-25,-26,-27,89,-58,-57,120,123,-60,-28,-29,]),'NOIGUALR':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,90,-58,-57,-60,-28,-29,]),'MAYORR':([40,45,46,47,48,49,55,69,72,91,102,103,104,],[-59,-23,-24,-25,-26,-27,91,-58,-57,119,-60,-28,-29,]),'MENORR':([40,45,46,47,48,49,55,69,72,92,102,103,104,],[-59,-23,-24,-25,-26,-27,92,-58,-57,122,-60,-28,-29,]),'ORB':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,94,-58,-57,-60,-28,-29,]),'XORB':([40,45,46,47,48,49,55,69,72,102,103,104,],[-59,-23,-24,-25,-26,-27,95,-58,-57,-60,-28,-29,]),'CORB':([40,45,46,47,48,49,55,56,57,58,59,60,61,69,70,72,96,98,99,100,102,103,104,108,109,110,111,112,113,114,115,116,117,118,121,124,125,126,128,130,131,132,133,134,],[-59,-23,-24,-25,-26,-27,-22,-30,-38,-43,-50,-61,-66,-58,102,-57,-31,-39,-51,-67,-60,-28,-29,-32,-33,-34,-35,-36,-40,-41,-42,-44,-45,-48,-49,-52,-53,-54,-62,-56,-46,-55,-47,-37,]),'int':([53,],[77,]),'char':([53,],[78,]),'float':([53,],[79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'ESTRUCTURAMAIN':([0,],[2,]),'PRECUERPO':([5,6,7,30,],[8,26,28,42,]),'CUERPO':([5,6,7,8,26,28,30,42,],[9,9,9,29,29,29,9,29,]),'ETIQUETA':([5,6,7,8,26,28,30,42,],[10,10,10,10,10,10,10,10,]),'GOTO_LABEL':([5,6,7,8,26,28,30,42,],[11,11,11,11,11,11,11,11,]),'ASIGNACION':([5,6,7,8,26,28,30,42,],[12,12,12,12,12,12,12,12,]),'DESTRUYE_VARIABLE':([5,6,7,8,26,28,30,42,],[13,13,13,13,13,13,13,13,]),'IMPRIME':([5,6,7,8,26,28,30,42,],[14,14,14,14,14,14,14,14,]),'ESTRUCTURA_IF':([5,6,7,8,26,28,30,42,],[15,15,15,15,15,15,15,15,]),'EXIT':([5,6,7,8,26,28,30,42,],[16,16,16,16,16,16,16,16,]),'NORMAL':([5,6,7,8,26,28,30,42,],[19,19,19,19,19,19,19,19,]),'ARRAY':([5,6,7,8,26,28,30,42,],[20,20,20,20,20,20,20,20,]),'LISTA_POS':([25,45,],[39,72,]),'POS':([25,39,45,72,],[40,69,40,69,]),'VALOR':([34,35,36,38,41,62,64,65,68,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,106,119,120,122,123,],[44,52,55,55,55,96,98,99,55,108,109,110,111,112,113,114,115,116,117,118,121,124,125,126,127,128,130,131,132,133,]),'LLAMADA_ARREGLO':([34,35,36,38,41,62,64,65,68,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,106,119,120,122,123,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'EXPRESION':([36,38,41,68,],[54,67,70,101,]),'ARITMETICAS':([36,38,41,68,],[56,56,56,56,]),'LOGICAS':([36,38,41,68,],[57,57,57,57,]),'RELACIONAL':([36,38,41,68,],[58,58,58,58,]),'BIT':([36,38,41,68,],[59,59,59,59,]),'CONVERSION':([36,38,41,68,],[60,60,60,60,]),'PUNTERO':([36,38,41,68,],[61,61,61,61,]),'TIPO_CONVERSION':([53,],[76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> ESTRUCTURAMAIN','S',1,'p_S','ascendente.py',41),
  ('S -> error','S',1,'p_S_error','ascendente.py',47),
  ('ESTRUCTURAMAIN -> main DOSPUNTOS PRECUERPO','ESTRUCTURAMAIN',3,'p_ESTRUCTURAMAIN','ascendente.py',52),
  ('ESTRUCTURAMAIN -> error DOSPUNTOS PRECUERPO','ESTRUCTURAMAIN',3,'p_ESTRUCTURAMAIN_ERROR1','ascendente.py',57),
  ('ESTRUCTURAMAIN -> main error PRECUERPO','ESTRUCTURAMAIN',3,'p_ESTRUCTURAMAIN_ERROR2','ascendente.py',62),
  ('ESTRUCTURAMAIN -> main DOSPUNTOS error','ESTRUCTURAMAIN',3,'p_ESTRUCTURAMAIN_ERROR3','ascendente.py',66),
  ('PRECUERPO -> PRECUERPO CUERPO','PRECUERPO',2,'p_PRECUERPO','ascendente.py',70),
  ('PRECUERPO -> CUERPO','PRECUERPO',1,'p_PRECUERPO_CUERPO','ascendente.py',76),
  ('CUERPO -> ETIQUETA','CUERPO',1,'p_CUERPO','ascendente.py',81),
  ('CUERPO -> GOTO_LABEL','CUERPO',1,'p_CUERPO','ascendente.py',82),
  ('CUERPO -> ASIGNACION','CUERPO',1,'p_CUERPO','ascendente.py',83),
  ('CUERPO -> DESTRUYE_VARIABLE','CUERPO',1,'p_CUERPO','ascendente.py',84),
  ('CUERPO -> IMPRIME','CUERPO',1,'p_CUERPO','ascendente.py',85),
  ('CUERPO -> ESTRUCTURA_IF','CUERPO',1,'p_CUERPO','ascendente.py',86),
  ('CUERPO -> EXIT','CUERPO',1,'p_CUERPO','ascendente.py',87),
  ('ETIQUETA -> ID DOSPUNTOS PRECUERPO','ETIQUETA',3,'p_ETIQUETA','ascendente.py',93),
  ('GOTO_LABEL -> goto ID PTCOMA','GOTO_LABEL',3,'p_GOTO_LABEL','ascendente.py',99),
  ('ASIGNACION -> NORMAL PTCOMA','ASIGNACION',2,'p_ASIGNACION','ascendente.py',106),
  ('ASIGNACION -> ARRAY PTCOMA','ASIGNACION',2,'p_ASIGNACION','ascendente.py',107),
  ('NORMAL -> VARIABLE IGUAL EXPRESION','NORMAL',3,'p_NORMAL','ascendente.py',112),
  ('ARRAY -> VARIABLE LISTA_POS IGUAL EXPRESION','ARRAY',4,'p_ARRAY','ascendente.py',118),
  ('EXPRESION -> VALOR','EXPRESION',1,'p_EXPRESION','ascendente.py',124),
  ('VALOR -> VARIABLE','VALOR',1,'p_VALOR_VARIABLE','ascendente.py',129),
  ('VALOR -> LLAMADA_ARREGLO','VALOR',1,'p_VALOR_LLAMADA_ARREGLO','ascendente.py',135),
  ('VALOR -> INT','VALOR',1,'p_VALOR_NUMERO','ascendente.py',140),
  ('VALOR -> FLOAT','VALOR',1,'p_VALOR_FLOAT','ascendente.py',146),
  ('VALOR -> CHAR','VALOR',1,'p_VALOR_CARACTER','ascendente.py',152),
  ('VALOR -> array PARA PARB','VALOR',3,'p_VALOR_NUEVO_ARREGLO','ascendente.py',158),
  ('VALOR -> read PARA PARB','VALOR',3,'p_VALOR_LEER','ascendente.py',165),
  ('EXPRESION -> ARITMETICAS','EXPRESION',1,'p_EXPRESION_ARITMETICAS','ascendente.py',170),
  ('ARITMETICAS -> MENOS VALOR','ARITMETICAS',2,'p_ARITMETICAS_NEGATIVO','ascendente.py',174),
  ('ARITMETICAS -> VALOR MAS VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',179),
  ('ARITMETICAS -> VALOR MENOS VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',180),
  ('ARITMETICAS -> VALOR MULTIPLICACION VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',181),
  ('ARITMETICAS -> VALOR DIVIDIR VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',182),
  ('ARITMETICAS -> VALOR RESIDUO VALOR','ARITMETICAS',3,'p_ARITMETICAS','ascendente.py',183),
  ('ARITMETICAS -> abs PARA VALOR PARB','ARITMETICAS',4,'p_ARITMETICAS_ABS','ascendente.py',198),
  ('EXPRESION -> LOGICAS','EXPRESION',1,'p_EXPRESION_LOGICAS','ascendente.py',203),
  ('LOGICAS -> NOTL VALOR','LOGICAS',2,'p_LOGICAS_NOT','ascendente.py',207),
  ('LOGICAS -> VALOR ANDL VALOR','LOGICAS',3,'p_LOGICAS','ascendente.py',212),
  ('LOGICAS -> VALOR ORL VALOR','LOGICAS',3,'p_LOGICAS','ascendente.py',213),
  ('LOGICAS -> VALOR XORL VALOR','LOGICAS',3,'p_LOGICAS','ascendente.py',214),
  ('EXPRESION -> RELACIONAL','EXPRESION',1,'p_EXPRESION_RELACIONAL','ascendente.py',225),
  ('RELACIONAL -> VALOR IGUALR VALOR','RELACIONAL',3,'p_RELACIONAL','ascendente.py',229),
  ('RELACIONAL -> VALOR NOIGUALR VALOR','RELACIONAL',3,'p_RELACIONAL','ascendente.py',230),
  ('RELACIONAL -> VALOR MAYORR IGUALR VALOR','RELACIONAL',4,'p_RELACIONAL','ascendente.py',231),
  ('RELACIONAL -> VALOR MENORR IGUALR VALOR','RELACIONAL',4,'p_RELACIONAL','ascendente.py',232),
  ('RELACIONAL -> VALOR MAYORR VALOR','RELACIONAL',3,'p_RELACIONAL','ascendente.py',233),
  ('RELACIONAL -> VALOR MENORR VALOR','RELACIONAL',3,'p_RELACIONAL','ascendente.py',234),
  ('EXPRESION -> BIT','EXPRESION',1,'p_EXPRESION_BIT','ascendente.py',251),
  ('BIT -> NOTB VALOR','BIT',2,'p_BIT_NOT','ascendente.py',255),
  ('BIT -> VALOR ANDB VALOR','BIT',3,'p_BIT','ascendente.py',260),
  ('BIT -> VALOR ORB VALOR','BIT',3,'p_BIT','ascendente.py',261),
  ('BIT -> VALOR XORB VALOR','BIT',3,'p_BIT','ascendente.py',262),
  ('BIT -> VALOR MENORR MENORR VALOR','BIT',4,'p_BIT','ascendente.py',263),
  ('BIT -> VALOR MAYORR MAYORR VALOR','BIT',4,'p_BIT','ascendente.py',264),
  ('LLAMADA_ARREGLO -> VARIABLE LISTA_POS','LLAMADA_ARREGLO',2,'p_LLAMADA_ARREGLO','ascendente.py',279),
  ('LISTA_POS -> LISTA_POS POS','LISTA_POS',2,'p_LISTA_POS_L','ascendente.py',285),
  ('LISTA_POS -> POS','LISTA_POS',1,'p_LISTA_POS_P','ascendente.py',290),
  ('POS -> CORA EXPRESION CORB','POS',3,'p_POS','ascendente.py',294),
  ('EXPRESION -> CONVERSION','EXPRESION',1,'p_EXPRESION_CONVERSION','ascendente.py',299),
  ('CONVERSION -> PARA TIPO_CONVERSION PARB VALOR','CONVERSION',4,'p_CONVERSION','ascendente.py',303),
  ('TIPO_CONVERSION -> int','TIPO_CONVERSION',1,'p_TIPO_CONVERSION','ascendente.py',309),
  ('TIPO_CONVERSION -> char','TIPO_CONVERSION',1,'p_TIPO_CONVERSION','ascendente.py',310),
  ('TIPO_CONVERSION -> float','TIPO_CONVERSION',1,'p_TIPO_CONVERSION','ascendente.py',311),
  ('EXPRESION -> PUNTERO','EXPRESION',1,'p_EXPRESION_PUNTERO','ascendente.py',316),
  ('PUNTERO -> ANDB VARIABLE','PUNTERO',2,'p_PUNTERO','ascendente.py',320),
  ('ESTRUCTURA_IF -> if PARA EXPRESION PARB goto ID PTCOMA','ESTRUCTURA_IF',7,'p_ESTRUCTURA_IF','ascendente.py',325),
  ('DESTRUYE_VARIABLE -> unset PARA VALOR PARB','DESTRUYE_VARIABLE',4,'p_DESTRUYE_VARIABLE','ascendente.py',330),
  ('IMPRIME -> print PARA VALOR PARB PTCOMA','IMPRIME',5,'p_IMPRIME','ascendente.py',335),
  ('EXIT -> exit PTCOMA','EXIT',2,'p_EXIT','ascendente.py',340),
]
