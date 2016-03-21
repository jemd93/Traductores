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

import ArbolExpr
from ArbolExpr import *
from SimTab import *
from ContBot import *

# OJO REVISAR
global superficie
superficie = {}

# ArbolInst inicial. Como todas las hojas
# son instrucciones (palabras reservadas) o 
# variables, aquí entran todos esos casos.
class ArbolInst(object):
	def __init__(self,inst,linea):
		self.inst = inst
		self.linea = linea

	def printArb(self,tabs,usarTabs):
		print(self.inst)

	def run(self):
		return

# Árbol para el programa principal o los subprogramas
class ArbolProgram(ArbolInst):
	def __init__(self,decList,execute):
		self.h2 = execute
		if not(decList is None):
			self.h1 = decList
		else:
			self.h1 = None

		self.simTab = SimTab()

	def printArb(self,tabs,usarTabs):
		if not(self.h1 is None):
			self.h2.printArb(tabs,usarTabs)
		else:
			self.h2.printArb(tabs,usarTabs)

	def run(self):
		self.h2.run(self.simTab)

# Arbol para el inicio de las listas de declaraciones
class ArbolDecListInit(ArbolInst):
	def __init__(self,decList,linea):
		self.h1 = ArbolInst('create',linea)
		self.h2 = decList
		self.linea = linea

	def check(self,simTab,linea,esDec) :
		self.h2.check(simTab,self.linea,esDec)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)

# Árbol para la lista de declaraciones para la creación de robots
class ArbolDecList(ArbolInst):
	def __init__(self,dec,decList,linea):
		self.h1 = dec
		if not(decList is None):
			self.h2 = decList
		else:
			self.h2 = None
		self.linea = linea

	def check(self,simTab,linea,esDec):
		self.h1.check(simTab,self.linea,esDec)
		if (self.h2 != None) :
			self.h2.check(simTab,self.linea,esDec)

	def printArb(self,tabs,usarTabs):
		if not(self.h2 is None):
			self.h1.printArb(0,True)
			self.h2.printArb(0,True)
		else:
			self.h1.printArb(0,True)	

# Árbol para una declaración de robot
class ArbolDec(ArbolInst):
	def __init__(self,arbTipo,idList,compList,linea):
		self.h1 = arbTipo
		self.h2 = ArbolInst('bot',linea)
		self.h3 = idList
		self.h4 = compList
		self.linea = linea

	def check(self,simTab,linea,esDec) :
		simTab.insertar("me",[self.h1.inst,None,2,0,0],{})
		self.h4.check(self.h1.inst,simTab,self.linea,esDec)
		# OJO ESTO ESTABA DESCOMENTADO ANTES.
		# simTab.eliminar("me")

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)
		self.h3.printArb(0,True)
		self.h4.printArb(0,True)

# Árbol para el tipo del robot a crear
class ArbolTipo(ArbolInst):
	def __init__(self, tipo):
		self.h1 = ArbolInst(tipo,linea)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)

# Árbol de la lista de identificadores
class ArbolIdList(ArbolInst): 
	def __init__(self,arbId,arbList,linea):
		self.h1 = arbId
		if not(arbList is None):
			self.h2 = arbList
		else:
			self.h2 = None
		self.linea = linea

	def check(self,simTab,linea,esDec) :
		simTab.obtenerClave(self.h1.elem,linea)
		if (self.h2 != None) :
			self.h2.check(simTab,linea,esDec)

	def printArb(self,tabs,usarTabs):
		print("\t"*tabs,end="")
		print("- var: ",end="")
		self.h1.printArb(tabs,True)
		if not(self.h2 is None):
			self.h2.printArb(tabs,True)

# Árbol para la lista de comportamientos de un robot
class ArbolCompList(ArbolInst):
	def __init__(self,comp,compList,linea):
		if (not(comp is None) and not(compList is None)):
			self.h1 = comp
			self.h2 = compList
		elif ((compList is None) and not(comp is None)):
			self.h1 = comp
			self.h2 = None
		else:
			self.h1 = None
			self.h2 = None
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec) :
		if (self.h1 != None) :
			self.h1.check(tipo,simTab,linea,esDec)
		if (self.h2 != None) :
			self.h2.check(tipo,simTab,linea,esDec)

	def generarTablaComps(self,tabla):
		if self.h1 != None and self.h2.h1 != None :
			if not(isinstance(self.h1.h2,ArbolExpr.ArbolExpr)) :
				if self.h1.h2.inst == 'default' :
					print("Error en la linea "+str(self.h1.linea)+": El comportamiento 'default'")
					print("debe ser declarado de ultimo en la lista de comportamientos")
					exit(1)
		if (self.h1 != None):
			self.h1.agregarATabla(tabla)
		if (self.h2 != None):
			self.h2.generarTablaComps(tabla)
		return tabla

	def printArb(self,tabs,usarTabs):
		if (not(self.h1 is None) and not(self.h2 is None)):
			self.h1.printArb(0,True)
			self.h2.printArb(0,True)
		elif ((self.h2 is None) and not(self.h1 is None)):
			self.h1.printArb(0,True)

# Árbol para comportamiento de un robot
class ArbolComp(ArbolInst):
	def __init__(self, expsta, inst,linea):
		self.h1 = ArbolInst('on',linea)
		self.h2 = expsta
		self.h3 = inst
		self.linea = linea
		self.simTab = SimTab()

	def check(self,tipo,simTab,linea,esDec) :
		# Creamos una nueva tabla de simbolos para este comportamiento
		simTab = SimTab(simTab)
		if (isinstance(self.h2,ArbolExpr.ArbolExpr)) :
			if not(self.h2.check("bool",simTab,self.linea,True)):
				print("Error en la linea "+str(self.linea)+" : la expresion debe ser de tipo bool")
				exit(1)
		self.h3.check(tipo,simTab,self.linea,esDec)
		# Desempilamos la tabla de simbolos del comportamiento
		self.simTab = simTab
		simTab = simTab.papa
		# simTab.clean() 

	def agregarATabla(self,tabla):
		if (isinstance(self.h2,ArbolExpr.ArbolExpr)):
			# ESTA AGREGANDO EXPS CON IDS INEXSISTENTES
			if not('advance' in tabla) : 
				tabla['advance'] = {}
			# OJO AQUI ESTABA SELF.H3 EN VEZ DE SELF.
			tabla['advance'][self.h2] = self
			return 

		if self.h2.inst in tabla : 
			print("Error en la linea "+str(self.linea)+" : No es posible declarar dos veces un comportamiento")
			exit(1)
		tabla[self.h2.inst] = self

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)
		self.h3.printArb(0,True)

	def run(self,var):
		self.h3.run(self.simTab,var)

# Árbol de estados en los que puede estar un robot
class ArbolState(ArbolInst):
	def __init__(self,state):
		self.h1 = ArbolInst(state,linea)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)

# Árbol para la lista de instrucciones del robot
class ArbolInstBotList(ArbolInst):
	def __init__(self,inst,instList,linea):
		self.h1 = inst
		if not(instList is None):
			self.h2 = instList
		else:
			self.h2 = None
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec) :
		self.h1.check(tipo,simTab,linea,esDec)
		if (self.h2 != None) :
			self.h2.check(tipo,simTab,linea,esDec)
		self.linea = linea

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		if not(self.h2 is None):
			self.h2.printArb(0,True)

	def run(self,simTab,var):
		self.h1.run(simTab,var)
		if not(self.h2 is None):
			self.h2.run(simTab,var)

######################## INSTRUCCIONES DE LOS ROBOTS ########################### 

# Árbol para la instrucción Store
class ArbolStore(ArbolInst):
	def __init__(self,h2,linea):
		self.h1 = ArbolInst('store',linea)
		self.h2 = h2
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec) :
		if not(self.h2.check(tipo,simTab,self.linea,esDec)):
			print("Error en la linea "+str(self.linea)+" : la expresion debe ser de tipo "+tipo)
			exit(1)
	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)

	def run(self,simTab,var):
		simTab.updateValue(var,self.h2.evaluate(simTab,var))

# Árbol para la instrucción Collect
# con caso Collect y caso Collect as ID
class ArbolCollect(ArbolInst):
	def __init__(self,hid,linea):
		self.h1 = ArbolInst('collect',linea)
		if not(hid is None):
			self.h2 = hid
		else:
			self.h2 = None
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		if (self.h2 != None) :
			if self.h2.elem in simTab.tabhash : 
				print("Error en la linea " + str(self.linea)+ ": La variable " + self.h2.elem + " ya ha sido declarada")
				exit(1)
			simTab.insertar(self.h2.elem,[tipo,None,2,0,0],{'clean':'clean'})
			self.h2.check(tipo,simTab,self.linea,esDec)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		if not(self.h2 is None):
			self.h2.printArb(0,True)

	def run(self,simTab,var):
		global superficie
		if (self.h2 is None):
			if ((simTab.obtener(var,self.linea)[0][3],simTab.obtener(var,self.linea)[0][4]) in superficie) :
				simTab.updateValue(var,superficie[(simTab.obtener(var,self.linea)[0][3],simTab.obtener(var,self.linea)[0][4])])
		else :
			if ((simTab.obtener(var,self.linea)[0][3],simTab.obtener(var,self.linea)[0][4]) in superficie) :
				simTab.updateValue(self.h2.elem,superficie[(simTab.obtener(var,self.linea)[0][3],simTab.obtener(var,self.linea)[0][4])])

# Árbol para la instrucción Drop
class ArbolDrop(ArbolInst):
	def __init__(self,h2,linea):
		self.h1 = ArbolInst('drop',linea)
		self.h2 = h2
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		if (self.h2.check("int",simTab,self.linea,esDec) or self.h2.check("bool",simTab,self.linea,esDec)
		or self.h2.check("char",simTab,self.linea,esDec)):
			return
		else :
			print("Error en la linea "+str(self.linea)+" : la expresion debe ser de tipo "+tipo)
			exit(1)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		self.h2.printArb(0,True)

	def run(self,simTab,var):
		global superficie
		# OJO DEVUELVE "'a'" en vez de 'a'
		superficie[(simTab.obtener(var,self.linea)[0][3],simTab.obtener(var,self.linea)[0][4])] = self.h2.evaluate(simTab,var)

# Árbol para la instrucción Entrada y Salida
# con caso Read y caso Read as ID
class ArbolRead(ArbolInst):
	def __init__(self,hid,linea):
		self.h1 = ArbolInst('read',linea)
		if not(hid is None):
			self.h2 = hid
		else:
			self.h2 = None
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec) :
		if (self.h2 != None) :
			if self.h2.elem in simTab.tabhash : 
				print("Error en la linea "+str(self.linea)+": La variable " + self.h2.elem + " ya ha sido declarada")
				exit(1)
			simTab.insertar(self.h2.elem,[tipo,None,2,0,0],{'clean','clean'})
			self.h2.check(tipo,simTab,self.linea,esDec)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		if not(self.h2 is None):
			self.h2.printArb(0,True)

	def run(self,simTab,var):
		tipo = simTab.obtener(var,self.linea)[0][0]
		i = input()
		if len(i) == 1 :
			if (tipo == 'int') and (i.isdigit()) :
				i = int(i)
		else :
			if ((i[0] == '-') or (i[0].isdigit())) and (i[1:].isdigit()):
				if (i[0] == '0'):
					print("Error : Los numeros no pueden empezar por 0")
					exit(1)
				i = int(i)
			elif i == "false":
				i = False
			elif i == "true" :
				i = True

		if (self.h2 is None) :
			simTab.updateValue(var,i)
		else :
			simTab.updateValue(self.h2.elem,i)



# Árbol para la instrucción Send
class ArbolSend(ArbolInst):
	def __init__(self,linea):
		self.h1 = ArbolInst('send',linea)
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		return True

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)

	def run(self,simTab,var):
		# OJO. SI NO HAY VALOR IMPRIME NONE. NO SE SI ES ERROR.
		val = simTab.obtener(var,self.linea)[0][1]
		if val == False :
			print("false")
		elif val == True :
			print("true")
		elif val is None :
			print("Error : La variable "+var+" no ha sido inicializada")
			exit(1)
		else:
			print(val)

# Árbol para la instrucción Recieve
class ArbolRecieve(ArbolInst):
	def __init__(self,hid,linea):
		self.h1 = ArbolInst('recieve',linea)
		if not(hid is None):
			self.h2 = hid
		else:
			self.h2 = None
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec) :
		if (self.h2 != None) :
			if self.h2.elem in simTab.tabhash : 
				print("Error en la linea "+str(self.linea)+": La variable " + self.h2.elem + " ya ha sido declarada")
				exit(1)
			simTab.insertar(self.h2.elem,[tipo,None,2,0,0],{'clean','clean'})
			self.h2.check(tipo,simTab,self.linea,esDec)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(0,True)
		if not(self.h2 is None):
			self.h2.printArb(0,True)

	def run(self,simTab,var):
		tipo = simTab.obtener(var,self.linea)[0][0]
		i = input()
		if len(i) == 1 :
			if (tipo == 'int') and (i.isdigit()) :
				i = int(i)
		else :
			if ((i[0] == '-') or (i[0].isdigit())) and (i[1:].isdigit()):
				if (i[0] == '0'):
					print("Error : Los numeros no pueden empezar por 0")
					exit(1)
				i = int(i)
			elif i == "false":
				i = False
			elif i == "true" :
				i = True

		if (self.h2 is None) :
			simTab.updateValue(var,i)
		else :
			simTab.updateValue(self.h2.elem,i)



##################### FIN DE LAS INSTRUCCIONES DEL ROBOT #######################

# Árbol para las instrucciones de movimientos 
class ArbolDir(ArbolInst):
	def __init__(self,h1,h2,linea):
		self.h1 = h1
		if not(h2 is None):
			self.h2 = h2
		else:
			self.h2 = None
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec) :
		if (self.h2 != None) :
			if not(self.h2.check("int",simTab,self.linea,esDec)):
				print("Error en la linea "+str(self.linea)+" : La expresion debe ser de tipo int")
				exit(1)
			# else:
			# 	if type(self.h2) == ArbolExpr.ArbolUn:
			# 		print("Error en la linea "+str(self.linea)+" : La expresion debe ser no negativa")
			# 		exit(1)

	def printArb(self,tabs,usarTabs):
		self.h1.printArb(tabs,True)
		if not(self.h2 is None):
			self.h2.printArb(tabs,True)

# Árbol para ejecutar las instrucciones de controlador
class ArbolInstExe(ArbolInst):
	def __init__(self,contList,linea):
		self.h1 = ArbolInst('execute',linea)
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

	def run(self,simTab):
		self.h2.run(simTab)

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

	def run(self,simTab):
		self.h1.run(simTab)
		if not(self.h2 is None):
			self.h2.run(simTab)

###################### INSTRUCCIONES DEL CONTROLADOR ###########################

# Árbol para la instrucción activate 
class ArbolActivate(ArbolInst):
	def __init__(self,idList,linea):
		self.h1 = ArbolInst('activate',linea)
		self.h2 = idList
		self.linea = linea

	def check(self,simTab,linea,esDec):
		self.h2.check(simTab,self.linea,esDec)

	def printArb(self,tabs,usarTabs):
		if usarTabs : 
			print("\t"*tabs,end="")
		print("ACTIVACION")
		self.h2.printArb(tabs+1,True)

	def run(self,simTab):
		simTab.activate(self.h2)

# Árbol para la instrucción advance
class ArbolAdvance(ArbolInst):
	def __init__(self,idList,linea):
		self.h1 = ArbolInst('advance',linea)
		self.h2 = idList
		self.linea = linea

	def check(self,simTab,linea,esDec):
		self.h2.check(simTab,self.linea,esDec)

	def printArb(self,tabs,usarTabs):
		if usarTabs : 
			print("\t"*tabs,end="")
		print("AVANCE")
		self.h2.printArb(tabs+1,True)

	def run(self,simTab):
		simTab.advance(self.h2)

# Árbol para la instrucción deactivate
class ArbolDeactivate(ArbolInst):
	def __init__(self,idList,linea):
		self.h1 = ArbolInst('deactivate',linea)
		self.h2 = idList
		self.linea = linea

	def check(self,simTab,linea,esDec):
		self.h2.check(simTab,self.linea,esDec)

	def printArb(self,tabs,usarTabs):
		if usarTabs : 
			print("\t"*tabs,end="")
		print("DESACTIVACION")
		self.h2.printArb(tabs+1,True)

	def run(self,simTab):
		simTab.deactivate(self.h2)

# Árbol para la instrucción if y if-else
class ArbolIf(ArbolInst):
	def __init__(self,expr,inst1,inst2,linea):
		self.h1 = ArbolInst('if',linea)
		self.h2 = expr
		self.h3 = inst1
		if not(inst2 is None):
			self.h4 = ArbolInst('else',linea)
			self.h5 = inst2
		else:
			self.h4 = None
			self.h5 = None
		self.linea = linea

	def check(self,simTab,linea,esDec):
		if not(self.h2.check("bool",simTab,self.linea,esDec)):
			print("Error en la linea "+str(self.linea)+" : La expresion debe ser de tipo bool")
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

	def run(self,simTab):
		if self.h2.evaluate(simTab,None) == True:
			self.h3.run(simTab)
		else:
			if not(self.h5 is None):
				self.h5.run(simTab)

# Árbol para la instrucción while
class ArbolWhile(ArbolInst):
	def __init__(self,expr,inst,linea):
		self.h1 = ArbolInst('while',linea)
		self.h2 = expr
		self.h3 = inst
		self.linea = linea

	def check(self,simTab,linea,esDec):
		if not(self.h2.check("bool",simTab,self.linea,esDec)):
			print("Error en la linea " + str(self.linea) + " : la expresion debe ser de tipo bool")
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

	# def run(self,simTab):
	# 	while (self.h2.evaluate(simTab,None)):
	# 		self.h3.run(SimTab)

################# FIN DE LAS INSTRUCCIONES DEL CONTROLADOR #####################