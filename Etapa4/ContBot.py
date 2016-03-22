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
# Proyecto BOT - Etapa 3 - Análisis de Contexto
# -------------------------------------------------

import sys
import ply.lex as lex
import ply.yacc as yacc

from LexBot import *
from ArbolExpr import *
from ArbolInst import *
from SimTab import *

tokens = BotLexer.tokens

def p_programa(p):

  # Descripción: Regla principal para iniciar el programa en lenguaje BOT.
  # Parámetros: - p: token

  ''' PROGRAM : DEC_LIST_INIT INST_EXE 
              | INST_EXE '''

  global simTabActual

  if len(p) == 3:
    p[0] = ArbolProgram(p[1],p[2])
    p[0].simTab = simTabActual
    simTabActual = simTabActual.papa
  else: 
    p[0] = ArbolProgram(None,p[1])

def p_dec_list_init(p):

  # Descripción: Regla para el inicio de la lista de declaraciones.
  # Parámetros: - p: token

  ''' DEC_LIST_INIT : TkCreate DEC_LIST '''

  global simTabActual
  # Comienza un nuevo scope, se crea una nueva tabla de simbolos 
  simTabActual = SimTab(simTabActual)
  simTabActual.agregarDecInit(p[2])

  p[0] = ArbolDecListInit(p[2],p.lineno(1)+1-ContBot.numLines)
  p[0].check(simTabActual,p.lineno(1)+1-ContBot.numLines,True)

def p_dec_list(p):

  # Descripción: Reglas para cuando existe una lista de declaraciones o 
  # definiciones de robots.
  # Parámetros: - p: token

  ''' DEC_LIST : DEC DEC_LIST
               | DEC '''

  if len(p) == 2:
    p[0] = ArbolDecList(p[1],None,p.lineno(1)+1-ContBot.numLines)
  else:
    p[0] = ArbolDecList(p[1],p[2],p.lineno(1)+1-ContBot.numLines)

def p_dec(p):

  # Descripción: Reglas de declaraciones o definiciones de robots.
  # Parámetros: - p: token

  ''' DEC : TIPO TkBot ID_LIST COMP_LIST TkEnd '''

  p[0] = ArbolDec(p[1],p[3],p[4],p.lineno(1)+1-ContBot.numLines)

def p_tipo(p):

  # Descripción: Reglas para tipos de robots que pueden crearse.
  # Parámetros: - p: token

  ''' TIPO : TkBool
           | TkChar
           | TkInt '''

  p[0] = ArbolInst(p[1],p.lineno(1)+1-ContBot.numLines)

def p_id_list(p):

  # Descripción: Reglas para cuando existen varios identificadores de robots.
  # Parámetros: - p: token

  ''' ID_LIST : ID TkComa ID_LIST
              | ID '''

  if len(p) == 2:
    p[0] = ArbolIdList(p[1],None,p.lineno(1)+1-ContBot.numLines)
  else : 
    p[0] = ArbolIdList(p[1],p[3],p.lineno(1)+1-ContBot.numLines)


def p_id(p):

  # Descripción: Regla de identificadores de robots.
  # Parámetros: - p: token

  ''' ID : TkIdent '''

  p[0] = ArbolExId(p[1],p.lineno(1)+1-ContBot.numLines)

def p_comp_list(p):

  # Descripción: Reglas para cuando existe una lista de comportamientos de 
  # robots.
  # Parámetros: - p: token

  ''' COMP_LIST : COMP COMP_LIST 
                | empty '''

  if len(p) == 2:
    p[0] = ArbolCompList(p[1],None,p.lineno(1))
  elif len(p) == 3:
    p[0] = ArbolCompList(p[1],p[2],p.lineno(1))
  else:
    p[0] = ArbolCompList(None,None,p.lineno(1))

def p_comp(p):

  # Descripción: Reglas de comportamientos de robots.
  # Parámetros: - p: token

  ''' COMP : TkOn EXPR TkDosPuntos INST_BOT_LIST TkEnd 
           | TkOn STATE TkDosPuntos INST_BOT_LIST TkEnd '''
  
  p[0] = ArbolComp(p[2],p[4],p.lineno(1)+1-ContBot.numLines)

def p_state(p):

  # Descripción: Reglas de estados en los que pueden empezar a estar los robots.
  # Parámetros: - p: token

  ''' STATE : TkActivation
            | TkDeactivation
            | TkDefault '''

  p[0] = ArbolInst(p[1],p.lineno(1)+1-ContBot.numLines)

def p_inst_bot_list(p):

  # Descripción: Reglas para lista de instrucciones de robots.
  # Parámetros: - p: token

  ''' INST_BOT_LIST : INST_BOT INST_BOT_LIST
                    | INST_BOT '''

  if len(p) == 2:
    p[0] = ArbolInstBotList(p[1],None,p.lineno(1)+1-ContBot.numLines)
  else:
    p[0] = ArbolInstBotList(p[1],p[2],p.lineno(1)+1-ContBot.numLines)

def p_inst_bot(p):

  # Descripción: Reglas para instrucciones de robots.
  # Parámetros: - p: token

  ''' INST_BOT : TkStore EXPR TkPunto        
               | TkCollect TkPunto
               | TkCollect TkAs ID TkPunto
               | TkDrop EXPR TkPunto
               | DIR TkPunto
               | DIR EXPR TkPunto
               | TkRead TkPunto
               | TkRead TkAs ID TkPunto
               | TkSend TkPunto '''

  if p[1] == 'store':
     p[0] = ArbolStore(p[2],p.lineno(1)+1-ContBot.numLines)
  elif p[1] == 'collect':
    if len(p) == 3: 
      p[0] = ArbolCollect(None,p.lineno(1)+1-ContBot.numLines)
    else:
      p[0] = ArbolCollect(p[3],p.lineno(1)+1-ContBot.numLines)
  elif p[1] == 'drop':
     p[0] = ArbolDrop(p[2],p.lineno(1)+1-ContBot.numLines)
  elif p[1] == 'read':
    if len(p) == 3:
      p[0] = ArbolRead(None,p.lineno(1)+1-ContBot.numLines)
    else:
      p[0] = ArbolRead(p[3],p.lineno(1)+1-ContBot.numLines)
  elif p[1] == 'send':
    p[0] = ArbolSend(p.lineno(1)+1-ContBot.numLines)
  else:
    if len(p) == 3: 
      p[0] = ArbolDir(p[1],None,p.lineno(2)+1-ContBot.numLines)
    else:
      p[0] = ArbolDir(p[1],p[2],p.lineno(3)+1-ContBot.numLines)

def p_dir(p):

  # Descripción: Reglas de movimiento en las instrucciones de robots.
  # Parámetros: - p: token

  ''' DIR : TkLeft 
          | TkRight
          | TkUp
          | TkDown '''

  p[0] = ArbolInst(p[1],p.lineno(1)+1-ContBot.numLines)

def p_inst_exe(p):

  # Descripción: Regla inicial del programa execute para instrucciones de 
  # controlador.
  # Parámetros: - p: token

  ''' INST_EXE : TkExecute INST_CONT_LIST TkEnd '''

  p[0] = ArbolInstExe(p[2],p.lineno(1)+1-ContBot.numLines)

def p_inst_cont_list(p):

  # Descripción: Reglas para lista de instrucciones de controlador.
  # Parámetros: - p: token

  ''' INST_CONT_LIST : INST_CONT INST_CONT_LIST
                     | INST_CONT '''

  if len(p) == 2 :
    p[0] = ArbolInstContList(p[1],None)
  else :
    p[0] = ArbolInstContList(p[1],p[2])

def p_inst_cont(p):

  # Descripción: Reglas para instrucciones de controlador.
  # Parámetros: - p: token

  ''' INST_CONT : TkActivate ID_LIST TkPunto
                | TkAdvance ID_LIST TkPunto
                | TkDeactivate ID_LIST TkPunto
                | TkIf EXPR TkDosPuntos INST_CONT_LIST TkElse TkDosPuntos INST_CONT_LIST TkEnd
                | TkIf EXPR TkDosPuntos INST_CONT_LIST TkEnd
                | TkWhile EXPR TkDosPuntos INST_CONT_LIST TkEnd
                | PROGRAM '''

  global simTabActual

  if p[1] == 'activate' :
    p[0] = ArbolActivate(p[2],p.lineno(1)+1-ContBot.numLines)
    p[0].check(simTabActual,p.lineno(1)+1-ContBot.numLines,False)
  elif p[1] == 'advance' :
    p[0] = ArbolAdvance(p[2],p.lineno(1)+1-ContBot.numLines)
    p[0].check(simTabActual,p.lineno(1)+1-ContBot.numLines,False)
  elif p[1] == 'deactivate' :
    p[0] = ArbolDeactivate(p[2],p.lineno(1)+1-ContBot.numLines)
    p[0].check(simTabActual,p.lineno(1)+1-ContBot.numLines,False)
  elif p[1] == 'if' :
    if p[5] == 'else' :
      p[0] = ArbolIf(p[2],p[4],p[7],p.lineno(1)+1-ContBot.numLines)
      p[0].check(simTabActual,p.lineno(1)+1-ContBot.numLines,False)
    else: 
      p[0] = ArbolIf(p[2],p[4],None,p.lineno(1)+1-ContBot.numLines)
      p[0].check(simTabActual,p.lineno(1)+1-ContBot.numLines,False)
  elif p[1] == 'while' :
    p[0] = ArbolWhile(p[2],p[4],p.lineno(1)+1-ContBot.numLines)
    p[0].check(simTabActual,p.lineno(1)+1-ContBot.numLines,False)
  else : 
    p[0] = p[1]

def p_expr(p):

  # Descripción: Reglas de las expresiones aritméticas, booleanas, posibles en 
  # el lenguaje BOT.
  # Parámetros: - p: token

  ''' EXPR : TkNum
           | TkIdent
           | TkCaracter
           | TkMe
           | TkParAbre EXPR TkParCierra
           | TkNegacion EXPR
           | TkResta EXPR %prec TkRestaUn
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

  if len(p) == 2:
    if type(p[1]) is int :
      p[0] = ArbolExInt(p[1],p.lineno(1)+1-ContBot.numLines)
    elif p[1] == "true" or p[1] == "false" :
      p[0] = ArbolExBool(p[1],p.lineno(1)+1-ContBot.numLines)
    elif p[1] == "me" :
      p[0] = ArbolExMe(p[1],p.lineno(1)+1-ContBot.numLines)
    elif p[1][0] == '\'' :
      p[0] = ArbolExChar(p[1],p.lineno(1)+1-ContBot.numLines)
    elif type(p[1]) is str :
      p[0] = ArbolExId(p[1],p.lineno(1)+1-ContBot.numLines)
  elif len(p) == 3:
    p[0] = ArbolUn(p[1], p[2], p.lineno(1)+1-ContBot.numLines)
  else:
    if (p[1] != '('):
      p[0] = ArbolBin(p[2], p[1], p[3], p.lineno(2)+1-ContBot.numLines)

    else :
      p[0] = p[2] 

def p_empty(p):

  # Descripción: Regla para la palabra vacía.
  # Parámetros: - p: token

  'empty :'
  pass

def p_error(p):

  # Descripción: Regla de error para los errores sintácticos.
  # Cabe destacar que el número de columna cuenta la columna contando
  # cada tab ('\t') como UN solo espacio. Si se quiere ver el 
  # número de columna correctamente, es necesario usar espacios en vez
  # de tabs en el archivo de entrada.
  # Parámetros: - p: token

  if not(p is None):
    last_cr = botlex.lexer.lexdata.rfind('\n',0,p.lexpos)
    column = (p.lexpos - last_cr)
    mensaje = "Existe un error sintáctico: '" + str(p.value) + "' en la línea "
    mensaje += str((p.lineno+1)-numLines) + ", en la columna " + str(column)
    print(mensaje)
    exit(1)
  else : 
    print("Error sintáctico.")
    exit(1)

# Reglas de precedencia para el parser.
precedence = (
  ('nonassoc','TkMayor','TkMayorIgual','TkMenor','TkMenorIgual'),
  ('left','TkSuma','TkResta'),
  ('left','TkDiv','TkMult','TkMod'),
  ('right','TkRestaUn'),
  ('left','TkDisyuncion'),
  ('left','TkConjuncion'),
  ('left','TkNegacion'), 
  ('left','TkIgual','TkDistinto'),
)


def numeroLineas():

  # Descripción: Método para usar en el cálculo del número de líneas para los
  #              errores.

  global numLines
  numLines = 0

  f = open(sys.argv[1],'r') # Abre el archivo pasado como parámetro por línea 
                            # de comando  
  finput = f.read()

  numLines = len(finput.split('\n'))
  return numLines


def main():

  # Descripción: Función del programa principal
  
  print(" ")

  # Variable global para indicar tabla de símbolos actual
  global simTabActual
  simTabActual = SimTab()

  # Verificación de parámetros de entrada
  if (len(sys.argv) != 2):
    print("Error, faltan argumentos de entrada")
    sys.exit(1)

  f = open(sys.argv[1],'r') # Abre el archivo pasado como parámetro por línea 
                            # de comando  
  finput = f.read()

  numLines = numeroLineas()

  # ANALIZADOR LEXICOGRÁFICO

  global botlex
  botlex = BotLexer()
  botlex.build()
  botlex.lexer.input(finput)
  botlex.tokenizar()

  if (botlex.errors == []):
    pass 
  else:
    for err in botlex.errors: 
      print("Error Lexico: Caracter inesperado \"%s\" en la fila %d, columna %d " % (err[0], err[1], err[2])) 
    exit(1)
  
  # ANALIZADOR SINTÁCTICO

  parser = yacc.yacc()
  result = parser.parse(finput, lexer=botlex.lexer)

  print("--------------------- PRINT DEL PROGRAMA   ---------------------------")
  if (result != None):
    result.h2.printArb(0,True)
    
  print("")
  print("--------------------- CORRIDA DEL PROGRAMA ---------------------------")
  # result.simTab.imprimir()
  result.run()
  f.close()

# Programa principal
if __name__ == "__main__":
  main()