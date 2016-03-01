# -------------------------------------------------
#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-10566
#           Meggie Sánchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 2 - Árbol de Expresiones tanto binario como unario
# -------------------------------------------------

import ContBot
ContBot.numeroLineas()

# Árbol de Expresiones con un solo elemento
# para las hojas, que será usualmente un ID,
# un número o un booleano.
class ArbolExpr(object):
	def __init__(self, x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea) :
		return True

	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExInt(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea):
		if tipo == "int" :
			return True
		else : 
			print("Error la operacion que intenta realizar requiere operadores de tipo "+tipo+ ". El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
			exit(1)
			
	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExBool(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea):
		if tipo == "bool" :
			return True
		else : 
			print("Error la operacion que intenta realizar requiere operadores de tipo "+tipo+ ". El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
			exit(1)

	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExChar(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea):
		if tipo == "char" :
			return True
		else : 
			print("Error la operacion que intenta realizar requiere operadores de tipo "+tipo+ ". El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
			exit(1)

	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExId(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea):
		if simTab.obtener(self.elem)[0] == tipo :
			return True
		else : 
			print("Error la operacion que intenta realizar requiere operadores de tipo "+tipo+ ". El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
			exit(1)

	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExMe(ArbolExpr):
	def __init__(self,x,linea):
		self.elem = x
		self.linea = linea

	def check(self,tipo,simTab,linea):
		if simTab.obtener(self.elem)[0] == tipo :
			return True
		else : 
			print("Error la operacion que intenta realizar requiere operadores de tipo "+tipo+ ". El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
			exit(1)

	def printArb(self,tabs,userTabs):
		print(self.elem)

# Árbol unario para el operador de negación
# o el negativo unario aritmético
class ArbolUn(ArbolExpr):
	def __init__(self,elem,a1,linea):
		self.elem = elem
		self.hijo = a1
		self.linea = linea

	def check(self,tipo,simTab,linea):
		if (self.elem == '-'):
			if self.hijo.check("int",simTab,self.linea) and (tipo == "int"):
				return True
			else:
				print("Error, los operadores de la operacion "+self.elem+" deben ser de tipo int. El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
				exit(1)

		elif (self.elem == '~'):
			if self.hijo.check("bool", simTab,self.linea) and (tipo == "bool"):
				return True
			else:
				print("Error, los operadores de la operacion "+self.elem+" deben ser de tipo int. El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
				exit(1)		

	def printArb(self,tabs,userTabs):
		# print(self.elem)
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
				
# Árbol binario para el resto de las
# expresiones, tanto aritméticas como booleanas
class ArbolBin(ArbolExpr):
	def __init__(self,elem,a1,a2,linea):
		self.elem = elem
		self.hizq = a1
		self.hder = a2
		self.linea = linea

	def check(self,tipo,simTab,linea) :
		if ((self.elem == '+') or (self.elem == '-') 
		or (self.elem == '*') or (self.elem == '/') 
		or (self.elem == '%')) :
			if (self.hizq.check("int",simTab,self.linea)
			and self.hder.check("int",simTab,self.linea)
			and tipo == "int") :
				return True
			else :
				print("Error, los operadores de la operacion "+self.elem+" deben ser de tipo int. El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
				exit(1)
		elif ((self.elem == '>') or (self.elem == '<')
		or (self.elem == '<=') or (self.elem == '>=')) : 
			if (self.hizq.check("int",simTab,self.linea) 
			and self.hder.check("int",simTab,self.linea)
			and tipo == "bool") :
				return True
			else :
				print("Error, los operadores de la operacion "+self.elem+" deben ser de tipo int. El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
				exit(1)
		elif ((self.elem == '/\\') or (self.elem == '\/')) :
			if (self.hizq.check("bool",simTab,self.linea)
			and self.hder.check("bool",simTab,self.linea)
			and tipo=="bool") :
				return True
			else :
				print("Error, los operadores de la operacion "+self.elem+" deben ser de tipo bool. El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
				exit(1)
		elif ((self.elem == '=') or (self.elem == '/=')) :
			for t in ["int","bool","char"] :
				if (self.hizq.check(t,simTab,self.linea)
				and self.hder.check(t,simTab,self.linea)
				and tipo=="bool") :
					return True

			print("Error, los operadores de la operacion "+self.elem+" deben ser del mismo tipo. El error se encuentra en la línea " + str(self.linea+1-ContBot.numLines))
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
