# -*- encoding: utf-8 -*-

#!/usr/bin/env python3  

# -----------------------------------------------
#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-10566
#           Meggie Sánchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 1
# -----------------------------------------------

import sys
import ply.lex as lex

print(sys.argv[1])
f = open(sys.argv[1],'r') # Abre el archivo escrito en el terminal para
                               # futura lectura
finput = f.read()

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

  'true'          : 'TkTrue',
  'false'         : 'TkFalse',
}

tokens = [
   'TkIdent',     
   'TkNum',          
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
] + list(reservadas.values())

# Reglas de expresiones regulares simples

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

def t_TkComentario(t):
    r'((\$\-([^\-]|(\-)+[^\$])*\-\$)|(\$\$.*))'
    t.lexer.lineno += len(t.value.rsplit('\n')) - 1

def t_TkCaracter(t):
    r'\'.*\''
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

# Compute column. 
#     input is the input text string
#     token is a token instance
def NumColumna(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    # if last_cr < 0:
    #   last_cr = -1
    column = (token.lexpos - last_cr)
    return column

def t_error(t):
    print("Error: Caracter inesperado \"%s\" en la fila %d, columna %d " % (t.value[0], t.lineno, NumColumna(finput, t))) 
    t.lexer.skip(1)

# String que ignora caracteres como los espacios y los tab
t_ignore  = ' \t'

lexer = lex.lex()

lexer.input(finput)

# Este ciclo tokeniza en el lexer
for tok in lexer:
    if (tok.type != 'TkIdent') and (tok.type != 'TkCaracter') and (tok.type != 'TkNum'):
        print(tok.type, tok.value, tok.lineno, NumColumna(finput, tok))
    elif (tok.type == 'TkIdent') and (tok.type != 'TkCaracter'):
        print(tok.type+"(\""+tok.value+"\")", tok.lineno, NumColumna(finput, tok))
    elif (tok.type != 'TkIdent') and ((tok.type == 'TkCaracter') or (tok.type == 'TkNum')):
        print(tok.type+"("+str(tok.value)+")", tok.lineno, NumColumna(finput, tok))
    
f.close()