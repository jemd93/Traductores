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


# f = open(sys.argv[1],'r') # Abre el archivo pasado como parametro por linea de comando
# finput = f.read()


class MyLexer(object):

  # Palabras reservadas
  reservadas = {
    'int'           : 'TkInt',
    'bool'          : 'TkBool',
    'char'          : 'TkChar',

    'create'        : 'TkCreate',
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

  # Nombres de los demas tokens
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

  # Funcion para detectar comentarios
  def t_TkComentario(self,t):
    r'((\$\-([^\-]|(\-)+[^\$])*\-\$)|(\$\$.*))'
    t.lexer.lineno += len(t.value.rsplit('\n')) - 1

  # Funcion para deteccion de caracteres
  def t_TkCaracter(self,t):
    r'\'.*\''
    return t

  # Funcion para deteccion de identificadores de variables
  def t_TkIdent(self,t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = self.reservadas.get(t.value,'TkIdent')
    return t

  # Funcion para deteccion de numeros
  def t_TkNum(self,t):
    r'\d+'
    t.value = int(t.value)    
    return t

  # Funcion para deteccion de saltos de linea
  def t_newline(self,t):
    r'\n+'
    t.lexer.lineno += len(t.value)

  # Funcion para calcular el numero de columna de cada token
  def NumColumna(self,token):
    last_cr = self.lexer.lexdata.rfind('\n',0,token.lexpos)
    column = (token.lexpos - last_cr)
    return column

  # Funcion para deteccion de caracteres ilegales
  def t_error(self,t):
    print("Error: Caracter inesperado \"%s\" en la fila %d, columna %d " % (t.value[0], t.lineno, self.NumColumna(t))) 
    t.lexer.skip(1)

  # String que ignora caracteres como los espacios y los tab
  t_ignore  = ' \t'

  # Build the lexer
  def build(self,**kwargs):
    self.lexer = lex.lex(module=self, **kwargs)

# Funcion principal
def main() :

  f = open(sys.argv[1],'r') # Abre el archivo pasado como parametro por linea de comando
  finput = f.read()

  lex = MyLexer()
  lex.build()
  lex.lexer.input(finput)
  # lexer = lex.lex()
  # lexer.input(finput)

  # lista = []
  # for tok in lex.lexer:
  #   lista.append(tok)

  # # for x in lista:
  # #   print(x)


  # Este ciclo tokeniza en el lexer 
  for tok in lex.lexer:
    if (tok.type != 'TkIdent') and (tok.type != 'TkCaracter') and (tok.type != 'TkNum'):
      print(tok.type, tok.value, tok.lineno, lex.NumColumna(tok))
    elif (tok.type == 'TkIdent') :
      print(tok.type+"(\""+tok.value+"\")", tok.lineno, lex.NumColumna(tok))
    elif (tok.type == 'TkCaracter') or (tok.type == 'TkNum'):
      print(tok.type+"("+str(tok.value)+")", tok.lineno, lex.NumColumna(tok))
      
  f.close()

# Programa principal
if __name__ == "__main__":
  main()