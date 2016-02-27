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

		self.tabhash = {}
		self.papa = papa

	def insertar(self,clave,tipo,comps=None):

		self.tabhash[clave] = [tipo,comps]

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

	# FUNCIONES PARA LA CREACION DE LA TABLA DE SIMBOLOS

	# Agrega la lista de declaraciones de DecListInit a la tabla de simbolos.
	def agregarDecInit(self,lista) :
		if (lista.h2 != None) :
			self.agregarDecList(lista.h1,lista.h2)
		else :
			self.agregarDecList(lista.h1,None)

	# Agrega todas las declaraciones de una DecList en la tabla de simbolos.
	def agregarDecList(self,dec,lista) :
		self.agregarListaId(dec.h3,dec.h1,dec.h4)
		if (lista != None) :
			self.agregarDecList(lista.h1,lista.h2)

	# Agrega todos los ids de una listaId con sus respectivos tipos y comportamientos
	# a la tabla de hash.
	def agregarListaId(self,lista,tipo,comps) :
		self.tabhash[lista.h1.elem] = [tipo.inst,comps] 
		if (lista.h2 != None) :
			self.agregarListaId(lista.h2,tipo,comps)

	def imprimir(self) :
		print(self.tabhash)
		if (self.papa != None) :
			self.papa.imprimir()

def main():

	comps1 = {}
	comps1['activation'] = "store 'x'. send"
	comps1['default'] = "y = x+2"
	simT1 = SimTab()

	simT1.insertar("bot1","int",comps1)

	comps2 = {}
	comps2['deactivation'] = "store 'h'"
	comps2['activation'] = "1+1=2"


	simT2 = SimTab(simT1)
	simT2.insertar("bot2","bool",comps2)

	simT2.imprimir()

	# bot2 = 4
	# bot3 = 5
	# bot4 = "hola"
	# bot5 = "jejeps"
	# activation = 3
	# default = 0
	# store = 3

	# tabhash = SimTab()
	# tab2 = SimTab()

	# tab2.insertar(default, store)

	# tabhash.insertar(bot1, "int", activation)
	# tabhash.insertar(bot2, "int", activation)
	# tabhash.insertar(bot3, "int", activation)
	# tabhash.insertar(bot4, "int", tab2)

	# print(tabhash.obtener(bot1))
	# print(tabhash.obtener(bot4))
	# print(tab2.obtener(default))
	# tabhash.obtener(bot3)
	# tabhash.obtener(bot5)

	#tabhash.modificar(bot1, "int", default)

	#print(tabhash.obtener(bot1))

# Programa principal
if __name__ == "__main__":
  main()
