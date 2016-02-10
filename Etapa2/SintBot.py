# -*- encoding: utf-8 -*-

#!/usr/bin/env python3  

# -------------------------------------------------
#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-10566
#           Meggie Sánchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 2 - Análisis Sintáctico
# -------------------------------------------------

import sys
import ply.lex as lex
import ply.yacc as yacc

from LexBot import *
from ArbolExpr import *
from ArbolInst import *

tokens = BotLexer.tokens

# Regla principal para iniciar el programa en lenguaje BOT.
def p_programa(p):
  ''' PROGRAM : DEC_LIST_INIT INST_EXE 
              | INST_EXE '''

  if len(p) == 3:
  	p[0] = ArbolProgram(p[1],p[2])
  else: 
  	p[0] = ArbolProgram(None,p[1])

# Regla para el inicio de la lista de declaraciones.
def p_dec_list_init(p):
  ''' DEC_LIST_INIT : TkCreate DEC_LIST '''

  p[0] = ArbolDecListInit(p[2])

# Reglas para cuando existe una lista de declaraciones o definiciones de robots.
def p_dec_list(p):
  ''' DEC_LIST : DEC DEC_LIST
               | DEC '''
  if len(p) == 2:
    p[0] = ArbolDecList(p[1],None)
  else:
    p[0] = ArbolDecList(p[1],p[2])

# Reglas de declaraciones o definiciones de robots.
def p_dec(p):
  ''' DEC : TIPO TkBot ID_LIST COMP_LIST TkEnd '''

  p[0] = ArbolDec(p[1],p[3],p[4])

# Reglas para tipos de robots que pueden crearse.
def p_tipo(p):
  ''' TIPO : TkBool
           | TkChar
           | TkInt '''

  p[0] = ArbolInst(p[1])

# Reglas para cuando existen varios identificadores de robots.
def p_id_list(p):
  ''' ID_LIST : ID TkComa ID_LIST
              | ID '''

  if len(p) == 2:
    p[0] = ArbolIdList(p[1],None)
  else : 
    p[0] = ArbolIdList(p[1],p[3])

# Regla de identificadores de robots.
def p_id(p):
  ''' ID : TkIdent '''

  p[0] = ArbolExpr(p[1])

# Reglas para cuando existe una lista de comportamientos de robots.
def p_comp_list(p):
  ''' COMP_LIST : COMP COMP_LIST 
                | empty '''

  if len(p) == 2:
    p[0] = ArbolCompList(p[1],None)
  elif len(p) == 3:
    p[0] = ArbolCompList(p[1],p[2])
  else:
    p[0] = ArbolCompList(None,None)

# Reglas de comportamientos de robots.
def p_comp(p):
  ''' COMP : TkOn EXPR TkDosPuntos INST_BOT_LIST TkEnd 
           | TkOn STATE TkDosPuntos INST_BOT_LIST TkEnd '''
  
  p[0] = ArbolComp(p[2],p[4])

# Reglas de estados en los que pueden empezar a estar los robots.
def p_state(p):
  ''' STATE : TkActivation
            | TkDeactivation
            | TkDefault '''

  p[0] = ArbolInst(p[1])

# Reglas para lista de instrucciones de robots.
def p_inst_bot_list(p):
  ''' INST_BOT_LIST : INST_BOT INST_BOT_LIST
                    | INST_BOT '''

  if len(p) == 2:
    p[0] = ArbolInstBotList(p[1],None)
  else:
    p[0] = ArbolInstBotList(p[1],p[2])

# Reglas para instrucciones de robots.
def p_inst_bot(p):
  ''' INST_BOT : TkStore EXPR TkPunto        
               | TkCollect TkPunto
               | TkCollect TkAs ID TkPunto
               | TkDrop EXPR TkPunto
               | DIR TkPunto
               | DIR EXPR TkPunto
               | TkRead TkPunto
               | TkRead TkAs ID TkPunto
               | TkSend TkPunto
               | TkRecieve TkPunto
               | TkRecieve EXPR TkPunto '''

  if p[1] == 'store':
     p[0] = ArbolStore(p[2])
  elif p[1] == 'collect':
    if len(p) == 3: 
      p[0] = ArbolCollect(None)
    else:
      p[0] = ArbolCollect(p[3])
  elif p[1] == 'drop':
     p[0] = ArbolDrop(p[2])
  elif p[1] == 'read':
    if len(p) == 3:
      p[0] = ArbolRead(None)
    else:
      p[0] = ArbolRead(p[3])
  elif p[1] == 'send':
    p[0] = ArbolSend()
  elif p[1] == 'recieve':
    if p[2] == '.':
      p[0] = ArbolRecieve(None)
    else:
      p[0] = ArbolRecieve(p[2])
  else:
    if len(p) == 3: 
      p[0] = ArbolDir(p[1],None)
    else:
      p[0] = ArbolDir(p[1],p[2])

# Reglas de movimiento en las instrucciones de robots.
def p_dir(p):
  ''' DIR : TkLeft 
          | TkRight
          | TkUp
          | TkDown '''

  p[0] = ArbolInst(p[1])

# Regla inicial del programa execute para instrucciones de controlador.
def p_inst_exe(p):
  ''' INST_EXE : TkExecute INST_CONT_LIST TkEnd '''

  p[0] = ArbolInstExe(p[2])

# Reglas para lista de instrucciones de controlador.
def p_inst_cont_list(p):
  ''' INST_CONT_LIST : INST_CONT INST_CONT_LIST
                     | INST_CONT '''
  if len(p) == 2 :
    p[0] = ArbolInstContList(p[1],None)
  else :
    p[0] = ArbolInstContList(p[1],p[2])

# Reglas para instrucciones de controlador.
def p_inst_cont(p):
  ''' INST_CONT : TkActivate ID_LIST TkPunto
                | TkAdvance ID_LIST TkPunto
                | TkDeactivate ID_LIST TkPunto
                | TkIf EXPR TkDosPuntos INST_CONT_LIST TkElse TkDosPuntos INST_CONT_LIST TkEnd
                | TkIf EXPR TkDosPuntos INST_CONT_LIST TkEnd
                | TkWhile EXPR TkDosPuntos INST_CONT_LIST TkEnd
                | PROGRAM '''

  if p[1] == 'activate' :
    p[0] = ArbolActivate(p[2])
  elif p[1] == 'advance' :
    p[0] = ArbolAdvance(p[2])
  elif p[1] == 'deactivate' :
    p[0] = ArbolDeactivate(p[2])
  elif p[1] == 'if' :
    if p[5] == 'else' :
      p[0] = ArbolIf(p[2],p[4],p[7])
    else : 
      p[0] = ArbolIf(p[2],p[4],None)
  elif p[1] == 'while' :
    p[0] = ArbolWhile(p[2],p[4])
  else : 
    p[0] = p[1]

# Reglas de las expresiones aritméticas, booleanas, posibles en el lenguaje BOT.
def p_expr(p):
  ''' EXPR : TkNum
           | TkIdent
           | TkCaracter
           | TkMe
           | TkParAbre EXPR TkParCierra
           | TkNegacion EXPR
           | TkResta EXPR %prec TkRestaUn
           | EXPR TkSuma EXPR
           | EXPR TkResta EXPR
           | EXPR TkMult EXPR
           | EXPR TkDiv EXPR
           | EXPR TkMod EXPR
           | TkTrue
           | TkFalse 
           | EXPR TkConjuncion EXPR 
           | EXPR TkDisyuncion EXPR
           | EXPR TkIgual EXPR
           | EXPR TkMayor EXPR
           | EXPR TkMayorIgual EXPR
           | EXPR TkMenor EXPR
           | EXPR TkMenorIgual EXPR
           | EXPR TkDistinto EXPR '''

  if len(p) == 2:
    p[0] = ArbolExpr(p[1])

  elif len(p) == 3:
    p[0] = ArbolUn(p[1], p[2])

  else:
    if (p[1] != '('):
      p[0] = ArbolBin(p[2], p[1], p[3])
    else :
      p[0] = p[2] 

# Regla para la palabra vacía.
def p_empty(p):
  'empty :'
  pass

# Regla de error para los errores sintácticos
# Cabe destacar que el numero de columna cuenta la columna contando
# cada tab ('\t') como UN solo espacio. Si se quiere ver el 
# numero de columna correctamente, es necesario usar espacios en vez
# de tabs en el archivo de entrada.
def p_error(p):
  if not(p is None):
    last_cr = botlex.lexer.lexdata.rfind('\n',0,p.lexpos)
    column = (p.lexpos - last_cr)
    mensaje = "Existe un error sintáctico: '" + str(p.value) + "' en la línea "
    mensaje += str((p.lineno+1)-numLines) + ", en la columna " + str(column)
    print(mensaje)
    exit(1)

# Reglas de precedencia para el parser.
precedence = (
  ('nonassoc','TkMayor','TkMayorIgual','TkMenor','TkMenorIgual'),
  ('left','TkSuma','TkResta'),
  ('left','TkDiv','TkMult','TkMod'),
  ('right','TkRestaUn'),
  ('left','TkDisyuncion'),
  ('left','TkConjuncion'),
  ('left','TkNegacion'), 
  ('left','TkIgual','TkDistinto'),
)
  
def main():
  global numLines
  numLines = 0

  if (len(sys.argv) != 2):
    print("Error, faltan argumentos de entrada")
    sys.exit(1)

  f = open(sys.argv[1],'r') # Abre el archivo pasado como parámetro por línea 
                            # de comando  
  finput = f.read()
  
  numLines = len(finput.split('\n'))

  # ANALIZADOR LEXICOGRÁFICO

  global botlex
  botlex = BotLexer()
  botlex.build()
  botlex.lexer.input(finput)
  botlex.tokenizar()

  if (botlex.errors == []):
    pass 
  else:
    for err in botlex.errors: 
      print("Error Lexico: Caracter inesperado \"%s\" en la fila %d, columna %d " % (err[0], err[1], err[2])) 
  
  # ANALIZADOR SINTÁCTICO

  parser = yacc.yacc()
  result = parser.parse(finput, lexer=botlex.lexer)

  if (result != None):
    result.h2.printArb(0,True)

  f.close()

# Programa principal
if __name__ == "__main__":
  main()