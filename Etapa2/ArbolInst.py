# -------------------------------------------------
#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-10566
#           Meggie Sánchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 2 - Arbol de Instrucciones
# -------------------------------------------------

from ArbolExpr import *

# OJO NO ESTOY SEGURO SI EN EL ARBOL DEBEN APARECER
# LOS PARENTESIS Y LOS PUNTOS. CREO QUE NO.

# ArbolInst inicial. Como todas las hojas
# son o instrucciones (palabras reservadas) o 
# variables, aqui entran todos esos casos.
class ArbolInst(object):
	def __init__(self,inst):
		self.inst = inst

	def printArb(self):
		print(self.inst)

# Arbol para la instruccion Store
class ArbolStore(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('store')
		self.h2 = h2

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()

# Arbol para la instruccion Collect
# con caso Collect y caso Collect as ID
class ArbolCollect(ArbolInst):
	def __init__(self,id):
		self.h1 = ArbolInst('collect')
		if not(id is None):
			self.h2 = ArbolInst('as')
			self.h3 = ArbolInst(id)
		else :
			self.h2 = None
			self.h3 = None

	def printArb(self):
		if self.h2 is None :
			self.h1.printArb()
		else :
			self.h1.printArb()
			self.h2.printArb()
			self.h3.printArb()

if __name__  == "__main__":
   # x = ArbolBin(1,None,None)
   # y = ArbolBin(3,None,None)
   # z = ArbolBin('+',x,y)

   # k = ArbolStore(z)

   # k.printArb()

   # m = ArbolCollect('variable')
   # m.printArb()

   # n = ArbolCollect()
   # n.printArb()