# -*- encoding: utf-8 -*-

#!/usr/bin/env python3  

# -------------------------------------------------
#  Universidad Simón Bolívar
#  Traductores e interpretadores - CI3725
#  Prof. Ricardo Monascal
#
#  Autores: Jorge Marcano   # Carnet 11-10566
#           Meggie Sánchez  # Carnet 11-10939
#
# Proyecto BOT - Etapa 3 - Clase para la tabla de 
# símbolos
# -------------------------------------------------

class SimTab(object):

	def __init__(self,papa=None):

		self.tabhash = dict()
		self.papa = papa

	def insertar(self,clave,tipo,comportamientos=None):

		self.tabhash[clave] = [tipo,comportamientos]

	# def modificar(self,clave,tipo,comportamientos=None):

	# 	if clave in self.tabhash:
	# 		self.tabhash[clave] = [tipo,comportamientos]
	# 	else:
	# 		if (self.papa != None):
	# 			self.papa.actualizar(clave,tipo,comportamientos)

	def obtener(self,clave):

		if clave in self.tabhash:
			return self.tabhash[clave]
		else:
			if (self.papa != None):
				return self.papa.obtener(clave)
			else:
				print(" Error de contexto: no ha sido realizada la declaración de: " + clave)

def main():

	bot1 = 3
	bot2 = 4
	bot3 = 5
	bot4 = "hola"
	bot5 = "jejeps"
	activation = 3
	default = 0
	store = 3

	tabhash = SimTab()
	tab2 = SimTab()

	tab2.insertar(default, store)

	tabhash.insertar(bot1, "int", activation)
	tabhash.insertar(bot2, "int", activation)
	tabhash.insertar(bot3, "int", activation)
	tabhash.insertar(bot4, "int", tab2)

	print(tabhash.obtener(bot1))
	print(tabhash.obtener(bot4))
	print(tab2.obtener(default))
	tabhash.obtener(bot3)
	tabhash.obtener(bot5)

	#tabhash.modificar(bot1, "int", default)

	#print(tabhash.obtener(bot1))

# Programa principal
if __name__ == "__main__":
  main()
