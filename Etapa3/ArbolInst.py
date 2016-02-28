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
from SimTab import *

cont = 0

# ArbolInst inicial. Como todas las hojas
# son instrucciones (palabras reservadas) o 
# variables, aquí entran todos esos casos.
class ArbolInst(object):
	def __init__(self,inst):
		self.inst = inst

	def printArb(self,tabs,usarTabs):
		print(self.inst)

# Árbol para el programa principal o los subprogramas
class ArbolProgram(ArbolInst):
	def __init__(self,decList,execute):
		self.h2 = execute
		if not(decList is None):
			self.h1 = decList
		else:
			self.h1 = None

	def printArb(self,tabs,usarTabs):
		if not(self.h1 is None):
			self.h2.printArb(tabs,usarTabs)
		else:
			self.h2.printArb(tabs,usarTabs)

# Arbol para el inicio de las listas de declaraciones
class ArbolDecListInit(ArbolInst):
	def __init__(self,decList):
		self.h1 = ArbolInst('create')
		self.h2 = decList

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)

# Árbol para la lista de declaraciones para la creación de robots
class ArbolDecList(ArbolInst):
	def __init__(self,dec,decList):
		self.h1 = dec
		if not(decList is None):
			self.h2 = decList
		else:
			self.h2 = None

	def printArb(self,tabs,usarTabs):
		if not(self.h2 is None):
			self.h1.printArb(0,True)
			self.h2.printArb(0,True)
		else:
			self.h1.printArb(0,True)	

# Árbol para una declaración de robot
class ArbolDec(ArbolInst):
	def __init__(self,arbTipo,idList,compList):
		self.h1 = arbTipo
		self.h2 = ArbolInst('bot')
		self.h3 = idList
		self.h4 = compList

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)
		self.h3.printArb(0,True)
		self.h4.printArb(0,True)

# Árbol para el tipo del robot a crear
class ArbolTipo(ArbolInst):
	def __init__(self, tipo):
		self.h1 = ArbolInst(tipo)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)

# Árbol de la lista de identificadores
class ArbolIdList(ArbolInst): 
	def __init__(self,arbId,arbList):
		self.h1 = arbId
		if not(arbList is None):
			self.h2 = arbList
		else:
			self.h2 = None

	def printArb(self,tabs,usarTabs):
		print("\t"*tabs,end="")
		print("- var: ",end="")
		self.h1.printArb(tabs,True)
		if not(self.h2 is None):
			self.h2.printArb(tabs,True)

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

	def printArb(self,tabs,usarTabs):
		if (not(self.h1 is None) and not(self.h2 is None)):
			self.h1.printArb(0,True)
			self.h2.printArb(0,True)
		elif ((self.h2 is None) and not(self.h1 is None)):
			self.h1.printArb(0,True)

# Árbol para comportamiento de un robot
class ArbolComp(ArbolInst):
	def __init__(self, expsta, inst):
		self.h1 = ArbolInst('on')
		self.h2 = expsta
		self.h3 = inst

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)
		self.h3.printArb(0,True)

# Árbol de estados en los que puede estar un robot
class ArbolState(ArbolInst):
	def __init__(self,state):
		self.h1 = ArbolInst(state)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)

# Árbol para la lista de instrucciones del robot
class ArbolInstBotList(ArbolInst):
	def __init__(self,inst,instList):
		self.h1 = inst
		if not(instList is None):
			self.h2 = instList
		else:
			self.h2 = None

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		if not(self.h2 is None):
			self.h2.printArb(0,True)

######################## INSTRUCCIONES DE LOS ROBOTS ########################### 

# Árbol para la instrucción Store
class ArbolStore(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('store')
		self.h2 = h2

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)

# Árbol para la instrucción Collect
# con caso Collect y caso Collect as ID
class ArbolCollect(ArbolInst):
	def __init__(self,hid):
		self.h1 = ArbolInst('collect')
		if not(hid is None):
			self.h2 = hid
		else:
			self.h2 = None

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		if not(self.h2 is None):
			self.h2.printArb(0,True)

# Árbol para la instrucción Drop
class ArbolDrop(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('drop')
		self.h2 = h2

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)

# Árbol para la instrucción Entrada y Salida
# con caso Read y caso Read as ID
class ArbolRead(ArbolInst):
	def __init__(self,hid):
		self.h1 = ArbolInst('read')
		if not(hid is None):
			self.h2 = hid
		else:
			self.h2 = None

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		if not(self.h2 is None):
			self.h2.printArb(0,True)

# Árbol para la instrucción Send
class ArbolSend(ArbolInst):
	def __init__(self):
		self.h1 = ArbolInst('send')

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)

# Árbol para la instrucción Recieve
class ArbolRecieve(ArbolInst):
	def __init__(self,h2):
		self.h1 = ArbolInst('recieve')
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		if not(self.h2 is None):
			self.h2.printArb(0,True)

##################### FIN DE LAS INSTRUCCIONES DEL ROBOT #######################

# Árbol para las instrucciones de movimientos 
class ArbolDir(ArbolInst):
	def __init__(self,h1,h2):
		self.h1 = h1
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(tabs,True)
		if not(self.h2 is None):
			self.h2.printArb(tabs,True)

# Árbol para ejecutar las instrucciones de controlador
class ArbolInstExe(ArbolInst):
	def __init__(self,contList):
		self.h1 = ArbolInst('execute')
		self.h2 = contList

	def printArb(self,tabs,usarTabs):
		if usarTabs : 
			print("\t"*tabs,end="")
		print("EXECUTE")
		if not(self.h2.h2 == None):
			print("\t"*(tabs+1),end="")
			print("SECUENCIACION")
			self.h2.printArb(tabs+2,True)
		else : 
			self.h2.printArb(tabs+1,True)

# Árbol para la lista de instrucciones de controlador
class ArbolInstContList(ArbolInst):
	def __init__(self,contInst,instList):
		self.h1 = contInst
		if not(instList is None):
			self.h2 = instList
		else:
			self.h2 = None

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(tabs,usarTabs)
		if not(self.h2 is None):
			self.h2.printArb(tabs,usarTabs)

###################### INSTRUCCIONES DEL CONTROLADOR ###########################

# Árbol para la instrucción activate 
class ArbolActivate(ArbolInst):
	def __init__(self,idList):
		self.h1 = ArbolInst('activate')
		self.h2 = idList

	def check(self,simTab):
		clave = self.h2.h1.elem
		simTab.obtenerclave(clave)
		while self.h2.h2 != None:
			self.h2 = self.h2.h2
			clave = self.h2.h1.elem
			simTab.obtenerclave(clave)

	def printArb(self,tabs,usarTabs):
		if usarTabs : 
			print("\t"*tabs,end="")
		print("ACTIVACION")
		self.h2.printArb(tabs+1,True)

# Árbol para la instrucción advance
class ArbolAdvance(ArbolInst):
	def __init__(self,idList):
		self.h1 = ArbolInst('advance')
		self.h2 = idList

	def printArb(self,tabs,usarTabs):
		if usarTabs : 
			print("\t"*tabs,end="")
		print("AVANCE")
		self.h2.printArb(tabs+1,True)

# Árbol para la instrucción deactivate
class ArbolDeactivate(ArbolInst):
	def __init__(self,idList):
		self.h1 = ArbolInst('deactivate')
		self.h2 = idList

	def printArb(self,tabs,usarTabs):
		if usarTabs : 
			print("\t"*tabs,end="")
		print("DESACTIVACION")
		self.h2.printArb(tabs+1,True)

# Árbol para la instrucción if y if-else
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

	def check(self,tipo,simTab):
		if tipo == "int":
			if ((self.h2.elem == '>') or (self.h2.elem == '<')
			or (self.h2.elem == '<=') or (self.h2.elem == '>=')
			or (self.h2.elem == '=') or (self.h2.elem == '/=')): 
				if ((self.h2.hizq.check("int",simTab)) 
				and (self.h2.hder.check("int",simTab))):
					return True
			else:
				print("Error, no esta permitido el operador " +self.h2.elem+ " en un condicional")
				exit(1)

		elif tipo == "bool":
			if ((self.h2.elem == '=') or (self.h2.elem == '/=')):
				for t in ["int","bool","char"] :
					if ( (self.h2.hizq.check(t,simTab))
					and (self.h2.hder.check(t,simTab)) ):
						return True
			elif ((self.h2.elem == '/\\') or (self.h2.elem == '\/')) :
				print("Error, no esta permitido el operador " +self.h2.elem+ " en un condicional")
				exit(1)

	def printArb(self,tabs,usarTabs):
		if usarTabs :
			print("\t"*tabs,end="")
		print("CONDICIONAL")
		print("\t"*(tabs+1),end="")
		print("- guardia: ",end="")
		self.h2.printArb(tabs+2,True)
		print("\t"*(tabs+1),end="")
		print("- exito: ",end="")
		if not(self.h3.h2 == None):
			print("SECUENCIACION")
			self.h3.printArb(tabs+2,True)
		else :
			self.h3.printArb(tabs+1,False)
		if not(self.h4 is None):
			print("\t"*(tabs+1),end="")
			print("- fracaso: ",end="") 
			if not(self.h5.h2 == None):
				print("SECUENCIACION")
				self.h5.printArb(tabs+2,True)
			else :
				self.h5.printArb(tabs+1,False)

# Árbol para la instrucción while
class ArbolWhile(ArbolInst):
	def __init__(self,expr,inst):
		self.h1 = ArbolInst('while')
		self.h2 = expr
		self.h3 = inst

	def check(self,tipo,simTab):
		if tipo == "int":
			if ((self.h2.elem == '>') or (self.h2.elem == '<')
			or (self.h2.elem == '<=') or (self.h2.elem == '>=')
			or (self.h2.elem == '=') or (self.h2.elem == '/=')): 
				if ((self.h2.hizq.check("int",simTab)) 
				and (self.h2.hder.check("int",simTab))):
					return True
			else:
				print("Error, no esta permitido el operador " +self.h2.elem+ " en un condicional")
				exit(1)

		elif tipo == "bool":
			if ((self.h2.elem == '=') or (self.h2.elem == '/=')):
				for t in ["int","bool","char"] :
					if ( (self.h2.hizq.check(t,simTab))
					and (self.h2.hder.check(t,simTab)) ):
						return True
			elif ((self.h2.elem == '/\\') or (self.h2.elem == '\/')) :
				print("Error, no esta permitido el operador " +self.h2.elem+ " en un condicional")
				exit(1)

	def printArb(self,tabs,usarTabs):
		if usarTabs :
			print("\t"*tabs,end="")
		print("ITERACION INDETERMINADA")
		print("\t"*(tabs+1),end="")
		print("- guardia: ",end="")
		self.h2.printArb(tabs+2,True)
		print("\t"*(tabs+1),end="")
		print("- exito: ",end="")
		if not(self.h3.h2 == None) :
			print("SECUENCIACION")
			self.h3.printArb(tabs+2,True)
		else : 
			self.h3.printArb(tabs+1,False)

################# FIN DE LAS INSTRUCCIONES DEL CONTROLADOR #####################