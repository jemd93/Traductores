# -------------------------------------------------
#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-10566
#           Meggie Sánchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 2 - Árbol de Instrucciones
# -------------------------------------------------

from ArbolExpr import *

# OJO NO ESTOY SEGURO SI EN EL ARBOL DEBEN APARECER
# LOS PARENTESIS Y LOS PUNTOS. CREO QUE NO.

# ArbolInst inicial. Como todas las hojas
# son o instrucciones (palabras reservadas) o 
# variables, aquí entran todos esos casos.
class ArbolInst(object):
	def __init__(self,inst):
		self.inst = inst

	def printArb(self):
		print(self.inst)

# Árbol para la instrucción Store
class ArbolStore(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('store')
		self.h2 = h2

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()

# Árbol para la instrucción Collect
# con caso Collect y caso Collect as ID
class ArbolCollect(ArbolInst):
	def __init__(self,id):
		self.h1 = ArbolInst('collect')
		if not(id is None):
			self.h2 = ArbolInst('as')
			self.h3 = ArbolInst(id)
		else:
			self.h2 = None
			self.h3 = None

	def printArb(self):
		if self.h2 is None:
			self.h1.printArb()
		else:
			self.h1.printArb()
			self.h2.printArb()
			self.h3.printArb()

# Árbol para la instrucción Drop
class ArbolDrop(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('drop')
		self.h2 = h2

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()

# Árbol para la instrucción Recieve
class ArbolRecieve(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('recieve')
		self.h2 = h2

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()

# Árboles para las instrucciones de Movimiento
# con caso Movimiento y caso Movimiento expresión

# Árbol para la instrucción de movimiento Left
# con caso left y caso left expresión
class ArbolLeft(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('left')
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None

	def printArb(self):
		if self.h2 is None:
			self.h1.printArb()
		else:
			self.h1.printArb()
			self.h2.printArb()

# Árbol para la instrucción de movimiento Right
# con caso right y caso right expresión
class ArbolRight(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('right')
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None

	def printArb(self):
		if self.h2 is None:
			self.h1.printArb()
		else:
			self.h1.printArb()
			self.h2.printArb()

# Árbol para la instrucción de movimiento Up
# con caso up y caso up expresión
class ArbolUp(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('up')
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None

	def printArb(self):
		if self.h2 is None:
			self.h1.printArb()
		else:
			self.h1.printArb()
			self.h2.printArb()

# Árbol para la instrucción de movimiento Down
# con caso down y caso down expresión
class ArbolDown(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('down')
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None

	def printArb(self):
		if self.h2 is None:
			self.h1.printArb()
		else:
			self.h1.printArb()
			self.h2.printArb()

# Árbol para la instrucción Entrada y Salida
# con caso Read y caso Read as ID
class ArbolRead(ArbolInst):
	def __init__(self,id):
		self.h1 = ArbolInst('read')
		if not(id is None):
			self.h2 = ArbolInst('as')
			self.h3 = ArbolInst(id)
		else:
			self.h2 = None
			self.h3 = None

	def printArb(self):
		if self.h2 is None:
			self.h1.printArb()
		else:
			self.h1.printArb()
			self.h2.printArb()
			self.h3.printArb()

# Árbol para la instrucción Send
class ArbolSend(ArbolInst):
	def __init__(self):
		self.h1 = ArbolInst('send')

	def printArb(self):
		self.h1.printArb()

if __name__  == "__main__":
   x = ArbolBin(1,None,None)
   y = ArbolBin(3,None,None)
   z = ArbolBin('+',x,y)

   r = ArbolBin('-',x,y)
   t = ArbolBin('*',x,y)
   w = ArbolBin('/',x,y)
   g = ArbolBin('%',x,y)

   k = ArbolStore(z)

   k.printArb()

   m = ArbolCollect('variable')
   m.printArb()

   n = ArbolCollect(None)
   n.printArb()

   o = ArbolDrop(z)

   o.printArb()

   ñ = ArbolRecieve(z)

   ñ.printArb()

   up = ArbolUp(None)
   up2 = ArbolUp(r)
   up.printArb()
   up2.printArb()

   left = ArbolLeft(None)
   left2 = ArbolLeft(t)
   left.printArb()
   left2.printArb()

   down = ArbolDown(None)
   down2 = ArbolDown(w)
   down.printArb()
   down2.printArb()

   right = ArbolRight(None)
   right2 = ArbolRight(g)
   right.printArb()
   right2.printArb()

   f = ArbolRead('variable')
   f.printArb()

   d = ArbolRead(None)
   d.printArb()

   s = ArbolSend()
   s.printArb()