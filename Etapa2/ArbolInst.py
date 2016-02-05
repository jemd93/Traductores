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
# son instrucciones (palabras reservadas) o 
# variables, aquí entran todos esos casos.
class ArbolInst(object):
	def __init__(self,inst):
		self.inst = inst

	def printArb(self):
		print(self.inst)

# Arbol para la instruccion if. Considerando el caso if, y el caso if else
class ArbolIf(ArbolInst):
	def __init__(self,hexpr,hinst1,hinst2):
		self.h1 = ArbolInst('if')
		self.h2 = hexpr
		self.h3 = hinst1
		if not(hinst2 is None) :
			self.h4 = ArbolInst('else')
			self.h5 = hinst2
		else :
			self.h4 = None
			self.h5 = None

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()
		self.h3.printArb()
		if not(self.h4 is None) :
			self.h4.printArb()
			self.h5.printArb()

# Arbol para la instruccion While
class ArbolWhile(ArbolInst):
	def __init__(self,hexpr,hinst):
		self.h1 = ArbolInst('while')
		self.h2 = hexpr
		self.h3 = hinst

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()
		self.h3.printArb()

# ARBOLES PARA INSTRUCCIONES DE LOS ROBOTS 

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
	def __init__(self,hid):
		self.h1 = ArbolInst('collect')
		if not(id is None):
			self.h2 = hid
		else:
			self.h2 = None

	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None):
			self.h2.printArb()

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

# Arbol para las instrucciones de movimientos 
class ArbolMove(ArbolInst):
	def __init__(self,dir,h2):
		self.h1 = ArbolInst(dir)
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None

	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None):
			self.h2.printArb()

# Árbol para la instrucción Entrada y Salida
# con caso Read y caso Read as ID
class ArbolRead(ArbolInst):
	def __init__(self,hid):
		self.h1 = ArbolInst('read')
		if not(hid is None):
			self.h2 = hid
		else:
			self.h2 = None
	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None):
			self.h2.printArb()

# Árbol para la instrucción Send
class ArbolSend(ArbolInst):
	def __init__(self):
		self.h1 = ArbolInst('send')

	def printArb(self):
		self.h1.printArb()

# Árbol para la instrucción Recieve
class ArbolRecieve(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('recieve')
		self.h2 = h2

	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None):
			self.h2.printArb()

if __name__  == "__main__":

   # x1 = ArbolBin(1,None,None)
   # y1 = ArbolBin(3,None,None)
   # z1 = ArbolBin('<',x1,y1)

   # x2 = ArbolBin(7,None,None)
   # y2 = ArbolBin(5,None,None)
   # z2 = ArbolBin('+',x2,y2)

   # h1 = ArbolRecieve(z2)

   # h2 = ArbolSend()

   # i = ArbolIf(z1,h1,h2)
   # i.printArb()

   # w = ArbolWhile(z1,h1)
   # w.printArb()

   # j = ArbolMove('right',z)

   # j.printArb()

   # r = ArbolBin('-',x,y)
   # t = ArbolBin('*',x,y)
   # w = ArbolBin('/',x,y)
   # g = ArbolBin('%',x,y)

   # k = ArbolStore(z)

   # k.printArb()

   # m = ArbolCollect('variable')
   # m.printArb()

   # n = ArbolCollect(None)
   # n.printArb()

   # o = ArbolDrop(z)

   # o.printArb()

   # ñ = ArbolRecieve(z)

   # ñ.printArb()

   # up = ArbolUp(None)
   # up2 = ArbolUp(r)
   # up.printArb()
   # up2.printArb()

   # left = ArbolLeft(None)
   # left2 = ArbolLeft(t)
   # left.printArb()
   # left2.printArb()

   # down = ArbolDown(None)
   # down2 = ArbolDown(w)
   # down.printArb()
   # down2.printArb()

   # right = ArbolRight(None)
   # right2 = ArbolRight(g)
   # right.printArb()
   # right2.printArb()

   # f = ArbolRead('variable')
   # f.printArb()

   # d = ArbolRead(None)
   # d.printArb()

   # s = ArbolSend()
   # s.printArb()