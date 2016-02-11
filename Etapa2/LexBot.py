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

    # Tipos
    'int'           : 'TkInt',
    'bool'          : 'TkBool',
    'char'          : 'TkChar',

    # Palabras reservadas para controlador
    'create'        : 'TkCreate',
    'execute'       : 'TkExecute',
    'end'           : 'TkEnd',

    # Condiciones para controlador
    'if'            : 'TkIf',
    'else'          : 'TkElse',
    'while'         : 'TkWhile',

    # Instrucciones de controlador
    'advance'       : 'TkAdvance',
    'deactivate'    : 'TkDeactivate',
    'activate'      : 'TkActivate',

    # Palabras reservadas para robots
    'bot'           : 'TkBot',
    'on'            : 'TkOn',

    # Movimientos para robots
    'left'          : 'TkLeft',
    'right'         : 'TkRight',
    'up'            : 'TkUp',
    'down'          : 'TkDown',

    'true'          : 'TkTrue',
    'false'         : 'TkFalse',

    # Condiciones en instrucciones para robots
    'deactivation'  : 'TkDeactivation',
    'activation'    : 'TkActivation',
    'default'       : 'TkDefault',

    # Instrucciones para robots
    'store'         : 'TkStore',
    'recieve'       : 'TkRecieve',
    'collect'       : 'TkCollect',
    'drop'          : 'TkDrop',
    'read'          : 'TkRead',
    'send'          : 'TkSend',
    'as'            : 'TkAs',
    'me'			      : 'TkMe',
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