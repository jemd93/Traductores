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

# Clase para la tabla de símbolos
class SimTab(object):

	def __init__(self,papa=None):

  		# Descripción: Constructor para la tabla de símbolos.
  		# Parámetros: - papa: apuntador hacia tabla de símbolos.

		self.tabhash = {}
		self.papa = papa

	def insertar(self,clave,tipo,comps=None):

  		# Descripción: Función para insertar en la tabla de símbolos.
  		# Parámetros: - clave: identificador bot declarado.
  		#			  - tipo:  tipo del bot declarado.
  		# 			  - comps: futura tabla hash que contiene los 
  		# 					   comportamientos de un bot. Puede ser vacía o no.		

		self.tabhash[clave] = [tipo,comps]

	def eliminar(self,clave):

  		# Descripción: Método para eliminar una clave en la tabla hash.
  		# Parámetros: - clave: clave a buscar en la tabla hash para eliminar.

		del self.tabhash[clave]

	def obtener(self,clave,linea):

		# Descripción: Método para obtener una clave en la tabla hash y despúes
		# 			   devolver la tupla correspondiente.
  		# Parámetros: - clave: clave a buscar en la tabla hash.
  		#			  - linea: linea correspondiente a posible error en el 
  		#					   analizador de contexto.

		if clave in self.tabhash:
			return self.tabhash[clave]
		else:
			if (self.papa != None):
				return self.papa.obtener(clave,linea)
			else:
				print("Error en la linea "+str(linea)+": no ha sido realizada la declaración de: " + clave)
				exit(1)

	def obtenerClave(self,clave,linea):

		# Descripción: Método para obtener una clave en la tabla hash y despúes
		# 			   devolver la clave correspondiente.
  		# Parámetros: - clave: clave a buscar en la tabla hash.
  		#			  - linea: linea correspondiente a posible error en el 
  		#					   analizador de contexto.

		if clave in self.tabhash:
			return clave
		else:
			if (self.papa != None):
				return self.papa.obtenerClave(clave,linea)
			else :
				print("Error en la linea "+str(linea)+": no ha sido realizada la declaración de: " + clave)
				exit(1)

	# FUNCIONES PARA LA CREACIÓN DE LA TABLA DE SÍMBOLOS

	def agregarDecInit(self,lista) :

		# Descripción: Método para agregar lista de declaraciones de DecListInit
		#			   a la tabla de simbolos.
  		# Parámetros: - lista: lista de declaraciones de bots.

		if (lista.h2 != None) :
			self.agregarDecList(lista.h1,lista.h2)
		else :
			self.agregarDecList(lista.h1,None)

	def agregarDecList(self,dec,lista) :

		# Descripción: Método para agregar todas las declaraciones de una 
		# 			   DecList en la tabla de simbolos.
  		# Parámetros: - dec: declaracion a agregar en la lista de declaraciones.
  		# 			  - lista: lista de declaraciones de bots.

		self.agregarListaId(dec.h3,dec.h1,dec.h4)
		if (lista != None) :
			self.agregarDecList(lista.h1,lista.h2)

	def agregarListaId(self,lista,tipo,comps) :

		# Descripción: Método para agregar todos los ids de una listaId con sus 
		# 			   respectivos tipos y comportamientos.
  		# Parámetros: - lista: lista de ids de bots.
  		#			  - tipo: tipo de los identificadores de los bots.
  		#			  - comps: tabla hash de comportamientos para los bots.

		if lista.h1.elem in self.tabhash:
			print("Error : la variable "+lista.h1.elem+" ya fue declarada anteriormente")
			exit(1)
		else :
			diccComps = comps.generarTablaComps({})
			self.tabhash[lista.h1.elem] = [tipo.inst,diccComps] 
			if (lista.h2 != None) :
				self.agregarListaId(lista.h2,tipo,comps)

	def imprimir(self):

		# Descripción: Método para imprimir la/las tablas de hashs.  

		print(self.tabhash)
		if (self.papa != None) :
			self.papa.imprimir()
