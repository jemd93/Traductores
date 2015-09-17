# -*- encoding: utf-8 -*-

#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-10566
#           Meggie Sanchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 1

import sys
import ply.lex as lex

finput = open(sys.argv[1],'r') # Abre el archivo escrito en el terminal para
                               # futura lectura

# Nombres de los tokens
reservadas = {
  'create'        : 'TkCreate',
  'int'           : 'TkInt',
  'bool'          : 'TkBool',
  'char'          : 'TkChar',
  'bot'           : 'TkBot',
  'on'            : 'TkOn',
  'activation'    : 'TkActivation',
  'store'         : 'TkStore',
  'end'           : 'TkEnd',
  'execute'       : 'TkExecute',
  'activate'      : 'TkActivate',
  'recieve'       : 'TkRecieve',
  'avance'        : 'TkAvance',
  'deactivate'    : 'TkDeactivate',
  'deactivation'  : 'TkDeactivation',
  'collect'       : 'TkCollect',
  'drop'          : 'TkDrop',
  'default'       : 'TkDefault',
  'send'          : 'TkSend',

  'left'          : 'TkLeft',
  'right'         : 'TkRight',
  'up'            : 'TkUp',
  'down'          : 'TkDown',
}

tokens = [
   'TkIdent',     
   'TkNum',          
   'TkCaracter', 

   'TkTrue',    
   'TkFalse',
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
] + list(reservadas.values())

# Reglas de expresiones regulares simples

t_TkTrue         = r'\#t'  # Consegui esto en internet no estoy clara o:
t_TkFalse        = r'\#f' 
t_TkComa         = r'\,'
t_TkPunto        = r'\.'
t_TkDosPuntos    = r'\:'
t_TkParAbre      = r'\('
t_TkParCierra    = r'\)'
t_TkSuma         = r'\+'
t_TkResta        = r'\-'   # ***
t_TkMult         = r'\*'
t_TkDiv          = r'/'
t_TkMod          = r'\%'
t_TkConjuncion   = r'\/\\' # ***
t_TkDisyuncion   = r'\\\/' # ***
t_TkNegacion     = r'\~'
t_TkMenor        = r'\<'
t_TkMenorIgual   = r'\<\=' # ***
t_TkMayor        = r'\>'
t_TkMayorIgual   = r'\>\=' # ***
t_TkIgual        = r'\='

# '''def t_COMMENT(t):
#     r'\#.*'
#     pass
#     # No return value. Token discarded
# Alternatively, you can include the prefix "ignore_" in the token declaration to force a token to be ignored. For example:
# t_ignore_COMMENT = r'\#.*'

def t_TkCaracter(t):
  #hola
  return t

def t_TkIdent(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reservadas.get(t.value,'TkIdent')
  return t

def t_TkNum(t):
  r'\d+'
  t.value = int(t.value)    
  return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0]) # Esto manda error para caracteres no soportados
  t.lexer.skip(1)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

lexer = lex.lex()

data = '''create
            int bot contador
              on activation:
                store 35.
              end
            end
          execute
            activate contador.
          end'''

lexer.input(data)

# if __name__ == '__main__':
#      lex.runmain()

# Tokenizar
for tok in lexer:
    print(tok.type, tok.value, tok.lineno, tok.lexpos)