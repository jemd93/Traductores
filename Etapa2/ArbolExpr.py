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

	def printArb(self,tabs):
		print(self.elem)

# Árbol unario para el operador de negación
# o el negativo unario aritmético
class ArbolUn(ArbolExpr):
	def __init__(self,elem,a1):
		self.elem = elem
		self.hijo = a1

	def printArb(self,tabs):
		print("EXPRESION UNARIA")
		# print(self.elem)
		if self.hijo is not None:
			print("\t"*tabs,end="")
			print("- operador derecho: ",end="")
			self.hijo.printArb(0)
				
# Árbol binario para el resto de las
# expresiones, tanto aritméticas como booleanas
class ArbolBin(ArbolExpr):
	def __init__(self,elem,a1,a2):
		self.elem = elem
		self.hizq = a1
		self.hder = a2

	def printArb(self,tabs):
		print("EXPRESION BINARIA")
		# print(self.elem)
		print("\t"*tabs,end="")
		print("- operacion: ",end="")
		if (self.elem == '+'): 
			print("Suma")

		if (self.elem == '-'):
			print("'Resta'")

		if (self.elem == '*'):
			print("'Multiplica'")

		if (self.elem == '/'):
			print("'Divide'")

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
			self.hizq.printArb(0)
			print("\t"*tabs,end="")
			print("- operador derecho: ",end="")
		if self.hder is not None:
			self.hder.printArb(0)
