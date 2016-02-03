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

# Reglas de las expresiones aritméticas, booleanas, 
# posibles en el lenguaje BOT.
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

  if len(t) == 4 :  
    if t[2] == '+':
      t[0] = t[1] + t[3]
      # print("Operacion : 'Suma'")
    elif t[2] == '-':
      t[0] = t[1] - t[3]
      # print("Operacion : 'Resta'")
    elif t[2] == '*':
      t[0] = t[1] * t[3]
      # print("Operacion : 'Multiplicacion'")
    elif t[2] == '/':
      t[0] = t[1] / t[3]
      # print("Operacion : 'Division'")
    elif t[2] == '%':
      t[0] = t[1] % t[3]
      # print("Operacion : 'Modulo'")
    elif t[1] == '(': 
      t[0] = t[2]

    # if p[1] != '(' :
    #   print("Operador Izquierdo :" + str(p[1]))
    #   print("Operador Derecho :" + str(p[3]))

  else : 
    t[0] = t[1]

def t_programa(t):
  ''' PROGRAM : TkCreate DEC_LIST TkExecute INST TkEnd 
              | TkExecute INST TkEnd '''

# Reglas para instrucciones de controlador e instrucciones de robots.
def t_instrucciones(t):
  ''' INST : TkActivate ID_LIST TkPunto
           | TkAdvance ID_LIST TkPunto
           | TkDeactivate ID_LIST TkPunto
           | INST_LIST
           | TkIf EXPR TkDosPuntos INST TkElse INST TkEnd
           | TkIf EXPR TkDosPuntos INST TkEnd
           | TkWhile EXPR TkDosPuntos INST TkEnd
           | PROGRAM              
           | TkStore EXPR TkPunto        
           | TkCollect TkPunto
           | TkCollect TkAs ID TkPunto
           | TkDrop EXPR TkPunto
           | DIR TkPunto
           | DIR EXPR TkPunto
           | TkRead TkPunto
           | TkRead TkAs ID TkPunto
           | TkSend TkPunto
           | TkRecieve TkPunto '''

# Reglas para cuando existe una lista de instrucciones tanto de controlador 
# como de robots.
def t_lista_instrucciones(t):
  ''' INST_LIST : INST_LIST TkComa INST
                | INST '''

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
  ''' ID_LIST : ID_LIST TkComa TkIdent
              | ID '''

# Reglas de declaraciones o definiciones de robots
def t_declaraciones(t):
  ''' DEC : TIPO TkBot ID_LIST COMP_LIST TkEnd '''

# Reglas para cuando existe una lista de declaraciones o 
# definiciones de robots
def t_lista_declaraciones(t):
  ''' DEC_LIST : DEC_LIST TkComa DEC
               | DEC '''

# Reglas de comportamientos de robots
def t_comportamientos(t):
  ''' COMP : TkOn EXPR TkDosPuntos INST TkEnd 
           | TkOn STATE TkDosPuntos INST TkEnd '''

# Reglas para cuando existe una lista de comportamientos 
# de robots
def t_lista_comportamientos(t):
  ''' COMP_LIST : COMP_LIST TkComa COMP
                | COMP '''

# Reglas de estados en los que pueden empezar a estar los 
# robots
def t_estados(t):
  ''' STATE : TkActivation
            | TkDeactivation
            | TkDefault '''

  t[0] = t[1]

# Reglas para tipos de robots que pueden crearse
def t_tipos(t):
  ''' TIPO : TkBool
           | TkChar
           | TkInt '''

  t[0] = t[1] 

# Regla para la palabra vacía
def p_lambda(t):
    ''' LAMBDA : '''
    pass

# Error rule for syntax errors
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
