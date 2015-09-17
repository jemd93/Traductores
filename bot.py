# -*- encoding: utf-8 -*-

#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-
#           Meggie Sanchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 1

import ply.lex as lex

# Nombres de los tokens

tokens = (
   'TkCreate',
   'TkIdent', 		
   'TkNum', 		
   'TkTrue', 		
   'TkFalse', 		
   'TkCaracter',	
   'TkComa',		
   'TkPunto',
   'TkDosPuntos',
   'TkParAbre',
   'TkParCierra',
   'TkSuma',
   'TkResta',
   'TkMult',
   'TkDiv',
   'TkMod',
   'TkConjuncion',
   'TkDisyuncion',
   'TkNegacion',
   'TkMenor',
   'TkMenorIgual',
   'TkMayor',
   'TkMayorIgual',
   'TkIgual',
)

'''

t_TkCreate
t_TkIdent
t_TkNum
t_TkCaracter

'''

# Reglas de expresiones regulares simples

t_TkTrue 		= r'\#t'  # Consegui esto en internet no estoy clara o:
t_TkFalse 		= r'\#f'	
t_TkComa 		= r'\,'
t_TkPunto 		= r'\.'
t_TkDosPuntos	= r'\:'
t_TkParAbre		= r'\('
t_TkParCierra	= r'\)'
t_TkSuma		= r'\+'
t_TkResta		= r'\-'   # ***
t_TkMult		= r'\*'
t_TkDiv			= r'/'
t_TkMod			= r'\%'
t_TkConjuncion  = r'\/\\' # ***
t_TkDisyuncion  = r'\\\/' # ***
t_TkNegacion	= r'\~'
t_TkMenor 		= r'\<'
t_TkMenorIgual	= r'\<\=' # ***
t_TkMayor 		= r'\>'
t_TkMayorIgual 	= r'\>\=' # ***
t_TkIgual 		= r'\='

'''def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded
Alternatively, you can include the prefix "ignore_" in the token declaration to force a token to be ignored. For example:
t_ignore_COMMENT = r'\#.*'

'''

'''reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   ...
}

tokens = ['LPAREN','RPAREN',...,'ID'] + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
'''
# A string containing ignored characters (spaces and tabs)
# t_ignore  = ' \t'
