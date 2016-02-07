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
# def t_programa(t):
#   ''' PROGRAM : DEC_LIST INST_EXE 
#               | INST_EXE '''

# # Reglas para lista de instrucciones de controlador.
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
               | TkCollect TkPunto
               | TkCollect TkAs ID TkPunto
               | TkDrop EXPR TkPunto
               | DIR TkPunto
               | DIR EXPR TkPunto
               | TkRead TkPunto
               | TkRead TkAs ID TkPunto
               | TkSend TkPunto
               | TkRecieve EXPR TkPunto '''

  if p[1] == 'store' :
    p[0] = ArbolStore(p[2])
  elif p[1] == 'collect' :
    if len(p) == 3 : 
      p[0] = ArbolCollect(None)
    else :
      p[0] = ArbolCollect(p[3])
  elif p[1] == 'drop' :
    p[0] = ArbolDrop(p[2])
  elif p[1] == 'read' :
    if len(p) == 3 :
      p[0] = ArbolRead()
    else :
      p[0] = ArbolRead(p[3])
  elif p[1] == 'send' :
    p[0] = ArbolSend()
  elif p[1] == 'recieve' :
    p[0] = ArbolRecieve(p[2])
  else :
    if len(p) == 3 : 
      p[0] = ArbolMove(p[1],None)
    else :
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
           | EXPR TkDistinto EXPR'''

  if len(p) == 2:
    p[0] = ArbolExpr(p[1])

  elif len(p) == 3:
    p[0] = ArbolUn(p[1], p[2])

  else :
    if (p[1] != '(') :
      p[0] = ArbolBin(p[2], p[1], p[3])
    else :
      p[0] = p[2] 

# Regla inicial del programa execute para instrucciones de controlador.
# def t_instruccion_execute(t):
#   ''' INST_EXE : TkExecute INST_CONT_LIST TkEnd'''

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
# def t_lista_instrucciones_robots(t):
#   ''' INST_BOT_LIST : INST_BOT_LIST TkComa INST_BOT
#                     | INST_BOT '''

# Reglas de movimiento en las instrucciones de robots.
def p_direcciones(p):
  ''' DIR : TkLeft 
          | TkRight
          | TkUp
          | TkDown '''

  p[0] = ArbolInst(p[1])

# Reglas de declaraciones o definiciones de robots.
# def t_declaraciones(t):
#   ''' DEC : TIPO TkBot ID_LIST COMP_LIST TkEnd '''

# # Reglas para cuando existe una lista de declaraciones o definiciones de robots.
# def t_lista_declaraciones(t):
#   ''' DEC_LIST : DEC_LIST TkComa DEC
#                | TkCreate DEC '''

# Reglas de comportamientos de robots.
# def t_comportamientos(t):
#   ''' COMP : TkOn EXPR TkDosPuntos INST_BOT TkEnd 
#            | TkOn STATE TkDosPuntos INST_BOT TkEnd '''

# Reglas para cuando existe una lista de comportamientos de robots.
# def t_lista_comportamientos(t):
#   ''' COMP_LIST : COMP_LIST TkComa COMP
#                 | COMP 
#                 | empty '''

# Reglas de estados en los que pueden empezar a estar los robots.
# def t_estados(t):
#   ''' STATE : TkActivation
#             | TkDeactivation
#             | TkDefault '''

#   t[0] = t[1]

# # Reglas para tipos de robots que pueden crearse.
# def t_tipos(t):
#   ''' TIPO : TkBool
#            | TkChar
#            | TkInt '''

#   t[0] = t[1] 

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
