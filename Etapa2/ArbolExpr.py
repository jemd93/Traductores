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

# OJO NO ESTOY SEGURO SI EN EL ARBOL DEBEN APARECER
# LOS PARENTESIS Y LOS PUNTOS. CREO QUE NO.

# Árbol de Expresiones con un solo elemento
# para las hojas, que sera usualmente un ID,
# un número o un booleano.
class ArbolExpr(object):
    def __init__(self, x):
        self.elem = x

# Árbol unario para el operador de negación
# o el negativo unario aritmético
class ArbolUn(ArbolExpr):
	def __init__(self,elem,a1):
		self.elem = elem
		self.hijo = a1

	def printArb(self):
		print(self.elem)
		if self.hijo is not None:
			self.hijo.printArb()
				
# Árbol binario para el resto de las
# expresiones, tanto aritméticas como booleanas
class ArbolBin(ArbolExpr):
	def __init__(self,elem,a1,a2):
		self.elem = elem
		self.hizq = a1
		self.hder = a2

	def printArb(self):
		print(self.elem)
		if self.hizq is not None:
			self.hizq.printArb()
		if self.hder is not None:
			self.hder.printArb()

if __name__  == "__main__":
   x = ArbolBin(1,None,None)
   y = ArbolBin(3,None,None)
   z = ArbolBin('+',x,y)

   p = ArbolBin(2,None,None)
   k = ArbolBin('*',p,z)

   i = ArbolBin(True,None,None)
   j = ArbolBin(False,None,None)
   l = ArbolBin('/\\',i,j)

   l.printArb()

   m = ArbolUn(2,None)
   n = ArbolUn('-',m)

   d = ArbolBin('*',z,n)
   d.printArb()