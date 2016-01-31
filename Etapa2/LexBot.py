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
# Proyecto BOT - Etapa 1 - Análisis Lexicográfico
# -------------------------------------------------

# Librerías utilizadas
import sys
import ply.lex as lex

class BotLexer(object):

  # Clase MyLexer para el análisis lexicográfico del lenguaje BOT
  
  toks = []
  errors = []

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

  # Nombres de los demás tokens
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
     'TkDistinto',
  ] + list(reservadas.values())

  # Reglas de expresiones regulares simples
  t_TkComa         = r'\,'
  t_TkPunto        = r'\.'
  t_TkDosPuntos    = r'\:'
  t_TkParAbre      = r'\('
  t_TkParCierra    = r'\)'
  t_TkSuma         = r'\+'
  t_TkResta        = r'\-'   
  t_TkMult         = r'\*'
  t_TkDiv          = r'/'
  t_TkMod          = r'\%'
  t_TkConjuncion   = r'\/\\' 
  t_TkDisyuncion   = r'\\\/' 
  t_TkNegacion     = r'\~'
  t_TkMenor        = r'\<'
  t_TkMenorIgual   = r'\<\=' 
  t_TkMayor        = r'\>'
  t_TkMayorIgual   = r'\>\=' 
  t_TkIgual        = r'\='
  t_TkDistinto     = r'\/\='

  def t_TkComentario(self,t):

    # Descripción: Función para detectar comentarios 
    # Parámetros: - t: token

    r'((\$\-([^\-]|(\-)+[^\$])*\-\$)|(\$\$.*))'
    t.lexer.lineno += len(t.value.rsplit('\n')) - 1

  def t_TkCaracter(self,t):

    # Descripción: Función para detección de caracteres
    # Parámetros: - t: token

    r'\'.\''
    return t

  def t_TkIdent(self,t):

    # Descripción: Función para detección de identificadores de variables
    # Parámetros: - t: token

    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = self.reservadas.get(t.value,'TkIdent')
    return t

  def t_ignoreTkNumTkIdent(self,t):

    # Descripción: Función para agregar a errores si un ident comienza en 
    #              números seguido de letras minúsculas o mayúsculas 
    # Parámetros: - t: token

    r'\d+[a-z_A-Z]+'
    self.errors.append([t.value[0],t.lineno,self.NumColumna(t)])
    t.lexer.skip(1)

  def t_TkNum(self,t):

    # Descripción: Función para detección de números
    # Parámetros: - t: token

    r'\d+'
    t.value = int(t.value)    
    return t

  def t_newline(self,t):

    # Descripción: Función para detección de saltos de línea
    # Parámetros: - t: token

    r'\n+'
    t.lexer.lineno += len(t.value)

  def NumColumna(self,token):

    # Descripción: Función para calcular el número de columna de cada token
    # Parámetros: - token: token

    last_cr = self.lexer.lexdata.rfind('\n',0,token.lexpos)
    column = (token.lexpos - last_cr)
    return column

  def t_error(self,t):

    # Descripción: Función para detección de caracteres ilegales
    # Parámetros: - t: token

    self.errors.append([t.value[0],t.lineno,self.NumColumna(t)])
    t.lexer.skip(1)

  # String que ignora caracteres como los espacios y los tab
  t_ignore  = ' \t'

  def build(self,**kwargs):

    # Descripción: Función para construir el lexer

    self.lexer = lex.lex(module=self, **kwargs)

  def tokenizar(self):

    # Descripción: Función para tokenizar todos los tokens existentes

    for t in self.lexer:
      self.toks.append([t.value,t.type,t.lineno,self.NumColumna(t)])

def main():

  # Función principal

  f = open(sys.argv[1],'r') # Abre el archivo pasado como parámetro por línea 
                            # de comando
  finput = f.read()

  botlex = BotLexer()
  botlex.build()
  botlex.lexer.input(finput)

  botlex.tokenizar()

  if (botlex.errors == []): 
    for tok in botlex.toks:
      if (tok[1] != 'TkIdent') and (tok[1] != 'TkCaracter') and (tok[1] != 'TkNum'):
        print(tok[1], tok[2], tok[3])
      elif (tok[1] == 'TkIdent') :
        print(tok[1]+"(\""+tok[0]+"\")", tok[2], tok[3])
      elif (tok[1] == 'TkCaracter') or (tok[1] == 'TkNum'):
        print(tok[1]+"("+str(tok[0])+")", tok[2], tok[3])
  else:
    for err in botlex.errors: 
      print("Error: Caracter inesperado \"%s\" en la fila %d, columna %d " % (err[0], err[1], err[2])) 
  
  f.close()

# Programa principal
if __name__ == "__main__":
  main()