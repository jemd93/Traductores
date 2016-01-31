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

def p_binary_operators(p):
    '''expression : expression TkSuma term
                  | expression TkResta term
       term       : term TkMult factor
                  | term TkDiv factor
                  | term TkMod factor'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]

def p_expression_term(p):
  'expression : term'
  p[0] = p[1]

def p_term_factor(p):
  'term : factor'
  p[0] = p[1]

def p_factor_num(p):
  'factor : TkNum'
  p[0] = p[1]

def p_factor_expr(p):
  'factor : TkParAbre expression TkParCierra'
  p[0] = p[2]

# def p_comparador_bin(p):
#     '''comp_bin   : factor TkMenor factor
#                   | factor TkMenorIgual factor
#                   | factor TkMayor factor
#                   | factor TkMayorIgual factor''' 
                  
#     if p[2] == '<':
#         p[0] = p[1] < p[3]
#     elif p[2] == '<=':
#         p[0] = p[1] <= p[3]
#     elif p[2] == '>':
#         p[0] = p[1] > p[3]
#     elif p[2] == '>=':
#         p[0] = p[1] >= p[3]

# def p_comparador_bool(p):
#     '''expression : expression TkIgual expression
#                   | expression TkDistinto expression'''
#     if p[2] == '=':
#         p[0] = p[1] = p[3]
#     elif p[2] == '/=':
#         p[0] = p[1] /= p[3] 

# def p_expression_bool(p):
#     '''bool : bool TkDisyuncion bool     
#             | bool TkConjuncion bool'''
#     if p[2] == '\/':
#         p[0] = p[1] = p[3]
#     elif p[2] == '/\':
#         p[0] = p[1] /\ p[3]                


# tokens = [
#      'TkIdent',     
#      'TkNum',          
#      'TkCaracter', 

#      'TkComa',    
#      'TkPunto',
#      'TkDosPuntos',
#      'TkParAbre',
#      'TkParCierra',

#      'TkConjuncion',
#      'TkDisyuncion',
#      'TkNegacion',

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
