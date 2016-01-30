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
# Proyecto BOT - Etapa 2 - Análisis Sintactico
# -------------------------------------------------

import sys
import ply.lex as lex
import ply.yacc as yacc

from LexBot import BotLexer
tokens = BotLexer.tokens

def p_expression_t_TkSuma(p):
  'expression : expression TkSuma term'
  p[0] = p[1] + p[3]

def p_expression_minus(p):
  'expression : expression TkResta term'
  p[0] = p[1] - p[3]

def p_expression_term(p):
  'expression : term'
  p[0] = p[1]

def p_term_times(p):
  'term : term TkMult factor'
  p[0] = p[1] * p[3]

def p_term_div(p):
  'term : term TkDiv factor'
  p[0] = p[1] / p[3]

def p_term_factor(p):
  'term : factor'
  p[0] = p[1]

def p_factor_num(p):
  'factor : TkNum'
  p[0] = p[1]

def p_factor_expr(p):
  'factor : TkParAbre expression TkParCierra'
  p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
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
