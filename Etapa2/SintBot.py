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

from LexBot import BotLexer
from ArbolExpr import *
from ArbolInst import *

tokens = BotLexer.tokens

# Regla principal para iniciar el programa en lenguaje BOT.
def p_programa(p):
  ''' PROGRAM : DEC_LIST INST_EXE 
              | INST_EXE '''

  if len(p) == 3:
  	p[0] = ArbolProgram(p[1],p[2])
  else: 
  	p[0] = ArbolProgram(None,p[1])

# Regla inicial del programa execute para instrucciones de controlador.
def p_instruccion_execute(p):
  ''' INST_EXE : TkExecute INST_CONT_LIST TkEnd '''

  p[0] = ArbolExecute(p[2])

# Reglas para lista de instrucciones de controlador.
def p_lista_instrucciones_controlador(p):
  ''' INST_CONT_LIST : INST_CONT TkComa INST_CONT_LIST
                     | INST_CONT '''
  if len(p) == 2 :
    p[0] = ArbolContList(p[1],None)
  else :
    p[0] = ArbolContList(p[1],p[3])

# Reglas para instrucciones de controlador.
def p_instrucciones_controlador(p):
  ''' INST_CONT : TkActivate ID_LIST TkPunto
                | TkAdvance ID_LIST TkPunto
                | TkDeactivate ID_LIST TkPunto
                | TkIf EXPR TkDosPuntos INST_CONT TkElse INST_CONT TkEnd
                | TkIf EXPR TkDosPuntos INST_CONT TkEnd
                | TkWhile EXPR TkDosPuntos INST_CONT TkEnd '''
                # | PROGRAM '''

  if p[1] == 'activate' :
    p[0] = ArbolContBot('activate',p[2])
  elif p[1] == 'advance' :
    p[0] = ArbolContBot('advance',p[2])
  elif p[1] == 'deactivate' :
    p[0] = ArbolContBot('deactivate',p[2])
  elif p[1] == 'if' :
    if p[5] == 'else' :
      p[0] = ArbolIf(p[2],p[4],p[6])
    else : 
      p[0] = ArbolIf(p[2],p[4],None)
  elif p[1] == 'while' :
    p[0] = ArbolWhile(p[2],p[4])
  else : # NOTA : Caso program. FALTA
    p[0] = ArbolInst('program') # <-- Placeholder

# Reglas para instrucciones de robots.
def p_inst_bot(p):
  ''' INST_BOT : TkStore EXPR TkPunto 
  			   | TkStore TkMe EXPR TkPunto	       
               | TkCollect TkPunto
               | TkCollect TkAs ID TkPunto
               | TkDrop EXPR TkPunto
               | TkDrop TkMe EXPR TkPunto
               | DIR TkPunto
               | DIR EXPR TkPunto
               | TkRead TkPunto
               | TkRead TkAs ID TkPunto
               | TkSend TkPunto
               | TkRecieve TkPunto
               | TkRecieve EXPR TkPunto '''

  if p[1] == 'store':
  	if p[2] == 'me':
  	  p[0] = ArbolStore(p[2],p[3])
  	else:
  	  p[0] = ArbolStore(None,p[2])
  elif p[1] == 'collect':
    if len(p) == 3: 
      p[0] = ArbolCollect(None)
    else:
      p[0] = ArbolCollect(p[3])
  elif p[1] == 'drop':
  	if p[2] == 'me':
  	  p[0] = ArbolDrop(p[2],p[3])
  	else:
  	  p[0] = ArbolDrop(None,p[2])
  elif p[1] == 'read':
    if len(p) == 3:
      p[0] = ArbolRead()
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
      p[0] = ArbolMove(p[1],None)
    else:
      p[0] = ArbolMove(p[1],p[2])

# Reglas de las expresiones aritméticas, booleanas, posibles en el lenguaje BOT.
def p_expr(p):
  ''' EXPR : TkNum
           | TkIdent
           | TkCaracter
           | TkParAbre EXPR TkParCierra
           | TkNegacion EXPR
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

  else :
    if (p[1] != '(') :
      p[0] = ArbolBin(p[2], p[1], p[3])
    else :
      p[0] = p[2] 

# Regla de identificadores de robots.
def p_id(p):
  ''' ID : TkIdent '''

  p[0] = ArbolExpr(p[1])

# Reglas para cuando existen varios identificadores de robots.
def p_id_list(p):
  ''' ID_LIST : ID TkComa ID_LIST
              | ID '''

  if len(p) == 2 :
    p[0] = ArbolIdList(p[1],None)
  else : 
    p[0] = ArbolIdList(p[1],p[3])

# Reglas para lista de instrucciones de robots.
def p_lista_instrucciones_robots(p):
  ''' INST_BOT_LIST : INST_BOT TkComa INST_BOT_LIST
                    | INST_BOT '''

  if len(p) == 2:
  	p[0] = ArbolBotList(p[1],None)
  else:
  	p[0] = ArbolBotList(p[1],p[3])

# Reglas de movimiento en las instrucciones de robots.
def p_direcciones(p):
  ''' DIR : TkLeft 
          | TkRight
          | TkUp
          | TkDown '''

  p[0] = ArbolInst(p[1])

# Reglas de declaraciones o definiciones de robots.
def p_declaraciones(p):
  ''' DEC : TIPO TkBot ID_LIST COMP_LIST TkEnd '''

  p[0] = ArbolDec(p[1],p[3],p[4])

# Reglas para cuando existe una lista de declaraciones o definiciones de robots.
def p_lista_declaraciones(p):
  ''' DEC_LIST : DEC TkComa DEC_LIST
               | TkCreate DEC '''
  if len(p) == 3:
  	p[0] = ArbolDecList(p[2],None)
  else:
  	p[0] = ArbolDecList(p[1],p[3])

# Reglas de comportamientos de robots.
def p_comportamientos(p):
  ''' COMP : TkOn EXPR TkDosPuntos INST_BOT TkEnd 
           | TkOn STATE TkDosPuntos INST_BOT TkEnd '''
  
  p[0] = ArbolComp(p[2],p[4])

# Reglas para cuando existe una lista de comportamientos de robots.
def p_lista_comportamientos(p):
  ''' COMP_LIST : COMP TkComa COMP_LIST
                | COMP 
                | empty '''

  if len(p) == 2:
  	p[0] = ArbolCompList(p[1],None)
  elif len(p) == 4:
  	p[0] = ArbolCompList(p[1],p[3])
  else:
  	p[0] = ArbolCompList(None,None)

# Reglas de estados en los que pueden empezar a estar los robots.
def p_estados(p):
  ''' STATE : TkActivation
            | TkDeactivation
            | TkDefault '''

  p[0] = ArbolInst(p[1])

# Reglas para tipos de robots que pueden crearse.
def p_tipos(p):
  ''' TIPO : TkBool
           | TkChar
           | TkInt '''

  p[0] = ArbolInst(p[1])

# Regla para la palabra vacía.
def p_empty(p):
    'empty :'
    pass

# Regla de error para los errores de sintaxis
def p_error(p):
  print("Syntax error in input!")

# Reglas de precedencia para el parser.
precedence = (
  ('left','TkSuma','TkResta'),
  ('left','TkDiv','TkMult','TkMod'),
  ('left','TkDisyuncion'),
  ('left','TkConjuncion'),
  ('left','TkNegacion'),
  ('nonassoc','TkMayor','TkMayorIgual','TkMenor','TkMenorIgual'), 
  ('left','TkIgual','TkDistinto'),
)

botlex = BotLexer()
botlex.build()
parser = yacc.yacc()

# try:
#     s = raw_input('bot > ')
# except EOFError:
#     break
# if not s: continue

f = open(sys.argv[1],'r') # Abre el archivo pasado como parámetro por línea 
                        # de comando
finput = f.read()
result = parser.parse(finput, lexer=botlex.lexer)

result.printArb()

f.close()
