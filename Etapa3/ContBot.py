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
from SintBot import generarArb

def main():
  # Descripción: Función del programa principal
  global numLines
  numLines = 0

  # Verificación de parámetros de entrada
  if (len(sys.argv) != 2):
    print("Error, faltan argumentos de entrada")
    sys.exit(1)

  arbol = generarArb(sys.argv[1])

  # if (arbol != None):
  #   result.h2.printArb(0,True)

if __name__ == "__main__":
  main()