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

	def insertar(self,bot,tipo,comportamientos):

		if not (bot in self.tabhash):
			self.tabhash[bot] = [tipo,comportamientos]

	def modificar(self,bot,tipo,comportamientos):

		if bot in self.tabhash:
			self.tabhash[bot] = [tipo,comportamientos]
		else:
			if (self.papa != None):
				self.papa.actualizar(bot,tipo,comportamientos)

	def obtener(self,bot):

		if bot in self.tabhash:
			return self.tabhash[bot]
		else:
			if (self.papa != None):
				return self.papa.obtener(bot)
			else:
				print(" Error de contexto: no ha sido realizada la declaración de: " + bot)

def main():

	bot1 = 3
	bot2 = 4
	bot3 = 5
	bot4 = "hola"
	bot5 = "jejeps"
	activation = 3
	default = 0

	tabhash = SimTab(None)
	tabhash.insertar(bot1, "int", activation)
	tabhash.insertar(bot2, "int", activation)
	tabhash.insertar(bot3, "int", activation)
	tabhash.insertar(bot4, "int", activation)

	print(tabhash.obtener(bot1))
	print(tabhash.obtener(bot2))
	tabhash.obtener(bot3)
	tabhash.obtener(bot5)

	tabhash.modificar(bot1, "int", default)

	print(tabhash.obtener(bot1))

# Programa principal
if __name__ == "__main__":
  main()
