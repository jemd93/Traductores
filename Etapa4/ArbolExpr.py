# ----------------------------------------------------
#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-10566
#           Meggie Sánchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 2 - Árbol de Expresiones 
#						   tanto binario como unario
# ----------------------------------------------------

import ContBot
from SimTab import *
ContBot.numeroLineas()

# Árbol de Expresiones con un solo elemento
# para las hojas, que será usualmente un ID,
# un número o un booleano.
class ArbolExpr(object):
	def __init__(self, x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec) :
		return True

	def printArb(self,tabs,userTabs):
		print(self.elem)

	def evaluate(self,simTab,var):
		return self.elem

class ArbolExInt(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		return tipo=="int"
			
	def printArb(self,tabs,userTabs):
		print(self.elem)

	def evaluate(self,simTab,var):
		return self.elem		

class ArbolExBool(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		return tipo=="bool"

	def printArb(self,tabs,userTabs):
		print(self.elem)

	def evaluate(self,simTab,var):
		if (self.elem == "true"):
			return True
		else :
			return False

class ArbolExChar(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		return tipo=="char"

	def printArb(self,tabs,userTabs):
		print(self.elem)

	def evaluate(self,simTab,var):
		return self.elem

class ArbolExId(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		if esDec and (not('clean' in simTab.obtener(self.elem,self.linea)[1])) :
			print("Error en la linea " +str(self.linea)+": La variable "+self.elem+" no ha sido declarada")
			exit(1)
		return simTab.obtener(self.elem,self.linea)[0][0] == tipo

	def printArb(self,tabs,userTabs):
		print(self.elem)

	def evaluate(self,simTab,var):
		val = simTab.obtener(self.elem,self.linea)[0][1]
		if val is None :
			print("Error : La variable "+str(var)+" no ha sido inicializada")
			exit(1)
		return val

class ArbolExMe(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		return simTab.obtener(self.elem,self.linea)[0][0] == tipo 

	def printArb(self,tabs,userTabs):
		print(self.elem)

	def evaluate(self,simTab,var):
		val = simTab.obtener(var,self.linea)[0][1]
		if val is None :
			print("Error : La variable "+str(var)+" no ha sido inicializada")
			exit(1)
		return val

# Árbol unario para el operador de negación
# o el negativo unario aritmético
class ArbolUn(ArbolExpr):
	def __init__(self,elem,a1,linea):
		self.elem = elem
		self.hijo = a1
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec):
		if (self.elem == '-'):
			if (tipo == "int") :
				if self.hijo.check("int",simTab,self.linea,esDec):
					return True
				else:
					print("Error en la linea "+str(self.linea)+": El operador de la operacion "+self.elem+" deben ser de tipo "+tipo)
					exit(1)
			else :
				return False

		elif (self.elem == '~'):
			if (tipo == "bool"):
				if self.hijo.check("bool", simTab,self.linea,esDec) and (tipo == "bool"):
					return True
				else:
					print("Error en la linea "+str(self.linea)+": El operador de la operacion "+self.elem+" deben ser de tipo "+tipo)
					exit(1)
			else :
				return False

	def printArb(self,tabs,userTabs):
		if self.hijo is not None:
			if (self.elem == '-'): 
				print("EXP UNARIA ARITMETICA")
			elif (self.elem == '~'):
				print("EXP UNARIA BOOLEANA")
			print("\t"*tabs,end="")
			print("- operacion : ",end="")
			if (self.elem == '-'):
				print("'-' Unario")
			if (self.elem == '~'):
				print("Negacion")
			print("\t"*tabs,end="")
			print("- operador : ",end="")
			self.hijo.printArb(tabs+1,True)	

	def evaluate(self,simTab,var):
		if (self.elem == '-'):
			return -(self.hijo.evaluate(simTab,var))
		elif (self.elem == '~'):
			return not(self.hijo.evaluate(simTab,var))

# Árbol binario para el resto de las
# expresiones, tanto aritméticas como booleanas
class ArbolBin(ArbolExpr):
	def __init__(self,elem,a1,a2,linea):
		self.elem = elem
		self.hizq = a1
		self.hder = a2
		self.linea = linea

	def check(self,tipo,simTab,linea,esDec) :
		if ((self.elem == '+') or (self.elem == '-') 
		or (self.elem == '*') or (self.elem == '/') 
		or (self.elem == '%')) :
			if tipo == "int":
				if (self.hizq.check("int",simTab,self.linea,esDec)
				and self.hder.check("int",simTab,self.linea,esDec)) :
					return True
				else :
					print("Error en la linea "+str(self.linea)+": Los operadores de la operacion "+self.elem+" deben ser de tipo "+tipo)
					exit(1)
			else :
				return False
		elif ((self.elem == '>') or (self.elem == '<')
		or (self.elem == '<=') or (self.elem == '>=')) : 
			if tipo == "bool" :
				if (self.hizq.check("int",simTab,self.linea,esDec) 
				and self.hder.check("int",simTab,self.linea,esDec)) :
					return True
				else :
					print("Error en la linea "+str(self.linea)+": Los operadores de la operacion "+self.elem+" deben ser de tipo "+tipo)
					exit(1)
			else :
				return False
		elif ((self.elem == '/\\') or (self.elem == '\/')) :
			if tipo=="bool" :
				if (self.hizq.check("bool",simTab,self.linea,esDec)
				and self.hder.check("bool",simTab,self.linea,esDec)) :
					return True
				else :
					print("Error en la linea "+str(self.linea)+": Los operadores de la operacion "+self.elem+" deben ser de tipo "+tipo)
					exit(1)
			else :
				return False
		elif ((self.elem == '=') or (self.elem == '/=')) :
			for t in ["int","bool","char"] :
				if tipo=="bool" :
					if (self.hizq.check(t,simTab,self.linea,esDec)
					and self.hder.check(t,simTab,self.linea,esDec)) :
						return True
				else :
					return False
			print("Error en la linea "+str(self.linea)+": Los operadores de la operacion "+self.elem+" deben ser del mismo tipo.")
			exit(1)

	def printArb(self,tabs,userTabs):
		if ((self.elem == '+') or (self.elem == '-') 
		or (self.elem == '*') or (self.elem == '/') 
		or (self.elem == '%')) :
			print("EXP BINARIA ARITMETICA")
		elif ((self.elem == '/\\') or (self.elem == '\/')) :
			print("EXP BINARIA BOOLEANA")
		elif ((self.elem == '=') or (self.elem == '/=') 
		or (self.elem == '<') or (self.elem == '>')
		or (self.elem == '<=') or (self.elem == '>=')) :
			print("EXP BINARIA RELACIONAL")

		print("\t"*tabs,end="")
		print("- operacion: ",end="")
		if (self.elem == '+'): 
			print("'Suma'")

		if (self.elem == '-'):
			print("'Resta'")

		if (self.elem == '*'):
			print("'Multiplicacion'")

		if (self.elem == '/'):
			print("'Division'")

		if (self.elem == '%'):
			print("'Modulo'")

		if (self.elem == '/\\'):
			print("'Conjuncion'")

		if (self.elem == '\/'):
			print("'Disyuncion'")

		if (self.elem == '='):
			print("'Igual que'")

		if (self.elem == '>'):
			print("'Mayor que'")

		if (self.elem == '<'):
			print("'Menor que'")

		if (self.elem == '<='):
			print("'Menor o igual que'")

		if (self.elem == '>='):
			print("'Mayor o igual que'")

		if (self.elem == '/='):
			print("'Distinto que'")

		if self.hizq is not None:
			print("\t"*tabs,end="")
			print("- operador izquierdo: ",end="")
			self.hizq.printArb(tabs+1,True)
			print("\t"*tabs,end="")
			print("- operador derecho: ",end="")
		if self.hder is not None:
			self.hder.printArb(tabs+1,True)

	def evaluate(self,simTab,var):
		if (self.elem == '+'): 
			return self.hizq.evaluate(simTab,var) + self.hder.evaluate(simTab,var)

		elif (self.elem == '-'):
			return self.hizq.evaluate(simTab,var) - self.hder.evaluate(simTab,var)

		elif (self.elem == '*'):
			return self.hizq.evaluate(simTab,var) * self.hder.evaluate(simTab,var)

		elif (self.elem == '/'):
			if self.hder.evaluate(simTab,var) == 0:
				print("Error en la linea " + str(self.linea) + " : la division por cero es ilegal")
				exit(1)
			return self.hizq.evaluate(simTab,var) / self.hder.evaluate(simTab,var)

		elif (self.elem == '%'):
			return self.hizq.evaluate(simTab,var) % self.hder.evaluate(simTab,var)

		elif (self.elem == '/\\'):
			return self.hizq.evaluate(simTab,var) and self.hder.evaluate(simTab,var)

		elif (self.elem == '\/'):
			return self.hizq.evaluate(simTab,var) or self.hder.evaluate(simTab,var)

		elif (self.elem == '='):
			return self.hizq.evaluate(simTab,var) == self.hder.evaluate(simTab,var)

		elif (self.elem == '>'):
			return self.hizq.evaluate(simTab,var) > self.hder.evaluate(simTab,var)

		if (self.elem == '<'):
			return self.hizq.evaluate(simTab,var) < self.hder.evaluate(simTab,var)

		if (self.elem == '<='):
			return self.hizq.evaluate(simTab,var) <= self.hder.evaluate(simTab,var)

		if (self.elem == '>='):
			return self.hizq.evaluate(simTab,var) >= self.hder.evaluate(simTab,var)

		if (self.elem == '/='):
			return self.hizq.evaluate(simTab,var) != self.hder.evaluate(simTab,var)
