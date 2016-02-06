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

# Reglas de precedencia para el parser.
precedence = (
  ('left','TkSuma','TkResta'),
  ('left','TkDiv','TkMult','TkMod'),
  ('left','TkDisyuncion'),
  ('left','TkConjuncion'),
  ('left','TkNegacion'),
  ('nonassoc','TkMayor','TkMayorIgual','TkMenor','TkMenorIgual'), 
  ('left','TkIgual','TkDistinto') 
)

# Reglas de las expresiones aritméticas, booleanas, posibles en el lenguaje BOT.
def t_expresiones(t):
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

  if len(t) == 2:
    t[0] = ArbolExpr(t[1])

  elif len(t) == 3:
    t[0] = ArbolUn(t[1], t[2])

  elif len(t) == 4: 
    t[0] = ArbolBin(t[2], t[1], t[3]) 
    if t[2] == '+':
      print("- Operacion: 'Suma'")
    elif t[2] == '-':
      print("- Operacion: 'Resta'")
    elif t[2] == '*':
      print("- Operacion: 'Multiplicacion'")
    elif t[2] == '/':
      print("- Operacion: 'Division'")
    elif t[2] == '%':
      print("- Operacion: 'Modulo'")
    elif t[2] == '/':
      print("- Operacion: 'Conjuncion'")
    elif t[2] == '\/':
      print("- Operacion: 'Disyuncion'")
    elif t[2] == '<':
      print("- Operacion: 'Menor que'")
    elif t[2] == '>':
      print("- Operacion: 'Mayor que'")
    elif t[2] == '<=':
      print("- Operacion: 'Menor o igual que'")
    elif t[2] == '>=':
      print("- Operacion: 'Mayor o igual que'")
    elif t[2] == '/=':
      print("- Operacion: 'Distinto que'")
    elif t[2] == '=':
      print("- Operacion: 'Igual que'")

    print("- Operador izquierdo: " + str(t[1]))
    print("- Operador derecho: " + str(t[3]))

  else: 
    t[0] = ArbolExpr(t[1])

# Regla principal para iniciar el programa en lenguaje BOT.
def t_programa(t):
  ''' PROGRAM : DEC_LIST INST_EXE TkEnd 
              | INST_EXE TkEnd '''

# Regla inicial del programa execute para instrucciones de controlador.
def t_instruccion_execute(t):
  ''' INST_EXE : TkExecute INST_CONT_LIST TkEnd'''

# Reglas para instrucciones de controlador.
def t_instrucciones_controlador(t):
  ''' INST_CONT : TkActivate ID_LIST TkPunto
                | TkAdvance ID_LIST TkPunto
                | TkDeactivate ID_LIST TkPunto
                | TkIf EXPR TkDosPuntos INST_CONT TkElse INST_CONT TkEnd
                | TkIf EXPR TkDosPuntos INST_CONT TkEnd
                | TkWhile EXPR TkDosPuntos INST_CONT TkEnd
                | PROGRAM '''      

# Reglas para instrucciones de robots.
def t_instrucciones_robot(t):
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

# Reglas para lista de instrucciones de controlador.
def t_lista_instrucciones_controlador(t):
  ''' INST_CONT_LIST : INST_CONT_LIST TkComa INST_CONT
                     | INST_CONT '''

# Reglas para lista de instrucciones de robots.
def t_lista_instrucciones_robots(t):
  ''' INST_BOT_LIST : INST_BOT_LIST TkComa INST_BOT
                    | INST_BOT '''

# Reglas de movimiento en las instrucciones de robots.
def t_direcciones(t):
  ''' DIR : TkLeft 
          | TkRight
          | TkUp
          | TkDown '''

  t[0] = t[1]

# Regla de identificadores de robots.
def t_identificadores(t):
  ''' ID : TkIdent '''

  t[0] = t[1]

# Reglas para cuando existen varios identificadores de robots.
def t_lista_identificadores(t):
  ''' ID_LIST : ID_LIST TkComa ID
              | ID '''

# Reglas de declaraciones o definiciones de robots.
def t_declaraciones(t):
  ''' DEC : TIPO TkBot ID_LIST COMP_LIST TkEnd '''

# Reglas para cuando existe una lista de declaraciones o definiciones de robots.
def t_lista_declaraciones(t):
  ''' DEC_LIST : DEC_LIST TkComa DEC
               | TkCreate DEC '''

# Reglas de comportamientos de robots.
def t_comportamientos(t):
  ''' COMP : TkOn EXPR TkDosPuntos INST_BOT TkEnd 
           | TkOn STATE TkDosPuntos INST_BOT TkEnd '''

# Reglas para cuando existe una lista de comportamientos de robots.
def t_lista_comportamientos(t):
  ''' COMP_LIST : COMP_LIST TkComa COMP
                | COMP 
                | LAMBDA '''

# Reglas de estados en los que pueden empezar a estar los robots.
def t_estados(t):
  ''' STATE : TkActivation
            | TkDeactivation
            | TkDefault '''

  t[0] = t[1]

# Reglas para tipos de robots que pueden crearse.
def t_tipos(t):
  ''' TIPO : TkBool
           | TkChar
           | TkInt '''

  t[0] = t[1] 

# Regla para la palabra vacía.
def p_lambda(t):
    ''' LAMBDA : '''
    pass

# Regla de error para los errores de sintaxis
def p_error(t):
  print("Syntax error in input!")

# f = open(sys.argv[1],'r') # Abre el archivo pasado como parámetro por línea 
#                             # de comando
# finput = f.read()

botlex = BotLexer()
botlex.build()
# botlex.lexer.input(finput)
# Build the parser
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

print(result)

f.close()
