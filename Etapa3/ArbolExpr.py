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

# Árbol de Expresiones con un solo elemento
# para las hojas, que será usualmente un ID,
# un número o un booleano.
class ArbolExpr(object):
	def __init__(self, x):
		self.elem = x

	def check(self,tipo,simTab) :
		return True

	def printArb(self,tabs,userTabs):
		print(self.elem)


class ArbolExInt(ArbolExpr):
	def __init__(self,x):
		self.elem = x

	def check(self,tipo,simTab):
		if tipo == "int" :
			return True
		else : 
			return False
	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExBool(ArbolExpr):
	def __init__(self,x):
		self.elem = x

	def check(self,tipo,simTab):
		if tipo == "bool" :
			return True
		else : 
			return False
	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExChar(ArbolExpr):
	def __init__(self,x):
		self.elem = x

	def check(self,tipo,simTab):
		if tipo == "char" :
			return True
		else : 
			return False

	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExId(ArbolExpr):
	def __init__(self,x):
		self.elem = x

	def check(self,tipo,simTab):
		if simTab.obtener(self.elem)[0] == tipo :
			return True
		else : 
			return False

	def printArb(self,tabs,userTabs):
		print(self.elem)

class ArbolExMe(ArbolExpr):
	def __init__(self,x):
		self.elem = x

	def check(self,tipo,simTab):
		if tipo == "me" :
			return True
		else : 
			return False

	def printArb(self,tabs,userTabs):
		print(self.elem)

# Árbol unario para el operador de negación
# o el negativo unario aritmético
class ArbolUn(ArbolExpr):
	def __init__(self,elem,a1):
		self.elem = elem
		self.hijo = a1

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
	def __init__(self,elem,a1,a2):
		self.elem = elem
		self.hizq = a1
		self.hder = a2

	def check(self,tipo,simTab) :
		if (self.hizq.check(tipo,simTab) 
			and self.hder.check(tipo,simTab)) :
			return True
		else :
			print("Error, los operadores de la operacion "+self.elem+" deben ser de tipo "+tipo)
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
