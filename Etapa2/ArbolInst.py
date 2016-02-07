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

# Árbol para el programa principal o los subprogramas
class ArbolProgram(ArbolInst):
	def __init__(self,a1,a2):
		self.a2 = ArbolExecute()
		if not(a1 is None):
			self.a1 = ArbolDecList()

	def printArb(self):
		if not(self.a1 is None):
			self.a1.printArb()
			self.a2.printArb()
		else:
			self.a2.printArb()

# NOTA : :'(
# Árbol para la lista de declaraciones para la creación de robots
class ArbolDecList(ArbolInst):
	def __init__(self,a1,a2,a3):
		if not(a1 is None):
			self.a1 = ArbolInst('create')
		self.a2 = ArbolDec()

# Árbol para ejecutar las instrucciones de controlador
class ArbolExecute(ArbolInst):
	def __init__(self,a2):
		self.a1 = ArbolInst('execute')
		self.a2 = ArbolInstContList()
		self.a3 = ArbolInst('end')

	def printArb(self):
		self.a1.printArb()
		self.a2.printArb()
		self.a3.printArb()

# Árbol para una declaración de robot
class ArbolDec(ArbolInst):
	def __init__(self,a1,a5):
		self.a1 = ArbolTipo()
		self.a2 = ArbolInst('bot')
		self.a3 = ArbolIdList()
		self.a4 = ArbolCompList()
		self.a5 = ArbolInst('end')

	def printArb(self):
		self.a1.printArb()
		self.a2.printArb()
		self.a3.printArb()
		self.a4.printArb()
		self.a5.printArb()

# Árbol para la lista de instrucciones de controlador
class ArbolInstContList(ArbolInst):
	def __init__(self,a1):
		if not(a1 is None):
			self.a1 = ArbolInstContList()
		self.a2 = ArbolInstCont()

# Árbol para el tipo del robot a crear
class ArbolTipo(ArbolInst):
	def __init__(self, tipo):
		self.h1 = ArbolInst(tipo)

	def printArb(self):
		self.h1.printArb()

# class ArbolIdList(ArbolInst):
# 	def __init__(self,):

# class ArbolCompList(ArbolInst):
# 	def __init__(self,):

# class ArbolInstCont(ArbolInst):
# 	def __init__(self,inst):
# 		self.a1 = ArbolInst(inst)
# 		self.a2 = ArbolIdList()	

# Árbol para la instruccion if. Considerando el caso if, y el caso if else
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


# ÁRBOLES PARA INSTRUCCIONES DE LOS ROBOTS 

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

# Árbol para las instrucciones de movimientos 
class ArbolMove(ArbolInst):
	def __init__(self,h1,h2):
		self.h1 = h1
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

class ArbolIdList(ArbolInst): 
	def __init__(self,arbId,arbList):
		self.h1 = arbId
		if not(arbList is None):
			self.h2 = arbList
		else :
			self.h2 = None

	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None) :
			self.h2.printArb()

# ARBOLES PARA INSTRUCCIONES DEL CONTROLADOR 

# Arbol para la instrucciones activate, deactivate y advance
# NOTA : Hecho de la misma forma que la parte de left,right,etc,
# no ando claro si vaa funcionar siempre, pero por ahora si.
class ArbolContBot(ArbolInst):
	def __init__(self,inst,idList):
		self.h1 = ArbolInst(inst)
		self.h2 = idList

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()

# Arbol para la instruccion if y if-else
class ArbolIf(ArbolInst):
	def __init__(self,expr,inst1,inst2):
		self.h1 = ArbolInst('if')
		self.h2 = expr
		self.h3 = inst1
		if not(inst2 is None) :
			self.h4  = ArbolInst('else')
			self.h5 = inst2
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

class ArbolWhile(ArbolInst):
	def __init__(self,expr,inst):
		self.h1 = ArbolInst('while')
		self.h2 = expr
		self.h3 = inst

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()
		self.h3.printArb()

class ArbolContList(ArbolInst):
	def __init__(self,contInst,instList):
		self.h1 = contInst
		if not(instList is None) :
			self.h2 = instList
		else :
			self.h2 = None


	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None) :
			self.h2.printArb()

# if __name__  == "__main__":

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

   # j = ArbolMove('right',z1)

   # j.printArb()

   # r = ArbolBin('-',x1,y1)
   # t = ArbolBin('*',x1,y1)
   # w = ArbolBin('/',x1,y1)
   # g = ArbolBin('%',x1,y1)

   # k = ArbolStore(z1)

   # k.printArb()

   # m = ArbolCollect('variable')
   # m.printArb()

   # n = ArbolCollect(None)
   # n.printArb()

   # o = ArbolDrop(z)

   # o.printArb()

   # ñ = ArbolRecieve(z)

   # ñ.printArb()

   # f = ArbolRead(ArbolExpr('variable'))
   # f.printArb()

   # d = ArbolRead(None)
   # d.printArb()

   # s = ArbolSend()
   # s.printArb()

   # t = ArbolIdList([ArbolExpr('var1'),ArbolExpr('var2'),ArbolExpr('var3')])
   # t.printArb()