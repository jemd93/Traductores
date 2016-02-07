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

################################################################################

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
		if not(hid is None):
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
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None

	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None):
			self.h2.printArb()

################################################################################

# ÁRBOLES PARA INSTRUCCIONES DEL CONTROLADOR 

# Árbol para la instrucciones activate, deactivate y advance
# NOTA : Hecho de la misma forma que la parte de left,right,etc,
# no ando claro si vaa funcionar siempre, pero por ahora si.
class ArbolContBot(ArbolInst):
	def __init__(self,inst,idList):
		self.h1 = ArbolInst(inst)
		self.h2 = idList

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()

# Árbol para la lista de instrucciones de controlador
class ArbolContList(ArbolInst):
	def __init__(self,contInst,instList):
		self.h1 = contInst
		if not(instList is None):
			self.h2 = instList
		else:
			self.h2 = None

	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None):
			self.h2.printArb()

# Arbol para la instruccion if y if-else
class ArbolIf(ArbolInst):
	def __init__(self,expr,inst1,inst2):
		self.h1 = ArbolInst('if')
		self.h2 = expr
		self.h3 = inst1
		if not(inst2 is None):
			self.h4 = ArbolInst('else')
			self.h5 = inst2
		else:
			self.h4 = None
			self.h5 = None

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()
		self.h3.printArb()
		if not(self.h4 is None): 
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

# Árbol para el programa principal o los subprogramas
class ArbolProgram(ArbolInst):
	def __init__(self,decList,execute):
		self.h2 = execute
		if not(decList is None):
			self.h1 = decList
		else:
			self.h1 = None

	def printArb(self):
		if not(self.h1 is None):
			self.h1.printArb()
			self.h2.printArb()
		else:
			self.h2.printArb()

# Árbol para ejecutar las instrucciones de controlador
class ArbolExecute(ArbolInst):
	def __init__(self,contList):
		self.h1 = ArbolInst('execute')
		self.h2 = contList

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()

# Arbol para el inicio de las listas de declaraciones
class ArbolDecListInit(ArbolInst) :
	def __init__(self,decList):
		self.h1 = ArbolInst('create')
		self.h2 = decList


	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()


# Árbol para una declaración de robot
class ArbolDec(ArbolInst):
	def __init__(self,arbTipo,idList,compList):
		self.h1 = arbTipo
		self.h2 = ArbolInst('bot')
		self.h3 = idList
		self.h4 = compList

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()
		self.h3.printArb()
		self.h4.printArb()

# Árbol para la lista de declaraciones para la creación de robots
class ArbolDecList(ArbolInst):
	def __init__(self,dec,decList):
		self.h1 = dec
		if not(decList is None):
			self.h2 = decList
		else:
			self.h2 = None

	def printArb(self):
		if not(self.h2 is None):
			self.h1.printArb()
			self.h2.printArb()
		else:
			self.h1.printArb()	

# Árbol de la lista de identificadores
class ArbolIdList(ArbolInst): 
	def __init__(self,arbId,arbList):
		self.h1 = arbId
		if not(arbList is None):
			self.h2 = arbList
		else:
			self.h2 = None

	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None):
			self.h2.printArb()

# Árbol para el tipo del robot a crear
class ArbolTipo(ArbolInst):
	def __init__(self, tipo):
		self.h1 = ArbolInst(tipo)

	def printArb(self):
		self.h1.printArb()

# Árbol para la lista de robots
class ArbolBotList(ArbolInst):
	def __init__(self,inst,instList):
		self.h1 = inst
		if not(instList is None):
			self.h2 = instList
		else:
			self.h2 = None

	def printArb(self):
		self.h1.printArb()
		if not(self.h2 is None):
			self.h2.printArb()

# NOTA: NO ESTOY SEGURA AQUI EN EXPSTA, PUEDE SER UNA EXPR O UN STATE
# Árbol para comportamiento de un robot
class ArbolComp(ArbolInst):
	def __init__(self, expsta, inst):
		self.h1 = ArbolInst('on')
		self.h2 = expsta
		self.h3 = inst

	def printArb(self):
		self.h1.printArb()
		self.h2.printArb()
		self.h3.printArb()

# Árbol para la lista de comportamientos de un robot
class ArbolCompList(ArbolInst):
	def __init__(self,comp,compList):
		if (not(comp is None) and not(compList is None)):
			self.h1 = comp
			self.h2 = compList
		elif ((compList is None) and not(comp is None)):
			self.h1 = comp
			self.h2 = None
		else:
			self.h1 = None
			self.h2 = None

	def printArb(self):
		if (not(self.h1 is None) and not(self.h2 is None)):
			self.h1.printArb()
			self.h2.printArb()
		elif ((self.h2 is None) and not(self.h1 is None)):
			self.h1.printArb()

# Árbol de estados en los que puede estar un robot
class ArbolState(ArbolInst):
	def __init__(self,state):
		self.h1 = ArbolInst(state)

	def printArb(self):
		self.h1.printArb()

################################################################################

if __name__  == "__main__":

   x1 = ArbolBin(1,None,None)
   y1 = ArbolBin(3,None,None)
   z1 = ArbolBin('<',x1,y1)

   x2 = ArbolBin(7,None,None)
   y2 = ArbolBin(5,None,None)
   z2 = ArbolBin('+',x2,y2)

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

   # k = ArbolStore(ArbolInst('me'),z1)
   # k.printArb()

   # k1 = ArbolStore(None,z1)
   # k1.printArb()

   # m = ArbolCollect('variable')
   # m.printArb()

   # n = ArbolCollect(None)
   # n.printArb()

   # o = ArbolDrop(ArbolInst('me'),z2)
   # o.printArb()

   # o1 = ArbolDrop(None,z2)
   # o1.printArb()

   # ñ = ArbolRecieve(z)

   # ñ.printArb()

   # f = ArbolRead(ArbolExpr('variable'))
   # f.printArb()

   # d = ArbolRead(None)
   # d.printArb()

   # s = ArbolSend()
   # s.printArb()

   # h = ArbolProgram(None,ArbolInst('activate'))
   # h.printArb()

   # k2 = ArbolState('activation')
   # k2.printArb()

   # h6 = ArbolComp(z1,'recieve')
   # h6.printArb()

   # h7 = ArbolComp(k2,'recieve')
   # h7.printArb()

   # h8 = ArbolCompList(h6, None)
   # h8.printArb()

   # h81 = ArbolCompList(h6, h7)

   # h9 = ArbolCompList(h6, h81)
   # h9.printArb()

   # h10 = ArbolTipo('bool')
   # h10.printArb()

   # h11 = ArbolDec(h10,ArbolIdList(ArbolExpr('var0'),None), h8)
   # h11.printArb()