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

	def insertar(self,clave,info,comps=None):

  		# Descripción: Función para insertar en la tabla de símbolos.
  		# Parámetros: - clave: identificador bot declarado.
  		#			  - info:  Arreglo de la forma [tipo,valor,estado,posX,posY]
  		# 			  - comps: futura tabla hash que contiene los 
  		# 					   comportamientos de un bot. Puede ser vacía o no.		

		self.tabhash[clave] = [info,comps]

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
			self.tabhash[lista.h1.elem] = [[tipo.inst,None,2,0,0],diccComps] 
			if (lista.h2 != None) :
				self.agregarListaId(lista.h2,tipo,comps)

	def updateValue(self,clave,val):
		if clave in self.tabhash : 
			self.tabhash[clave][0][1] = val
		else :
			if (self.papa != None):
				self.papa.updateValue(clave,val)

	# FUNCIONES DE CAMBIOS EN LA TABLA DURANTE EJECUCION

	# Funcion para activar una lista de IDs
	def activate(self,lista):
		if not('activation' in self.tabhash[lista.h1.elem][1]):
			print("Error, no se puede activar un robot que no posea su comportamiento activation")
			exit(1)
		else:
			if self.tabhash[lista.h1.elem][0][2] == 1:
				print("Error ya el robot ha sido activado antes")
				exit(1)
			else:
				self.tabhash[lista.h1.elem][0][2] = 1
				# El run de aqui es el run del ArbolComp asociado a activate
				self.tabhash[lista.h1.elem][1]['activation'].run(lista.h1.elem)
				if lista.h2 != None :
					self.activate(lista.h2)

	def deactivate(self,lista):
		if not('deactivation' in self.tabhash[lista.h1.elem][1]):
			print("Error, no se puede desactivar un robot que no posea su comportamiento deactivation")
			exit(1)
		else:
			if self.tabhash[lista.h1.elem][0][2] == 0:
				print("Error ya el robot ha sido desactivado antes")
				exit(1)
			else:
				self.tabhash[lista.h1.elem][0][2] = 0
				self.tabhash[lista.h1.elem][1]['deactivation'].run(lista.h1.elem)
				if lista.h2 != None :
					self.deactivate(lista.h2)

	def imprimir(self):

		# Descripción: Método para imprimir la/las tablas de hashs.  
		print(self.tabhash)
		if (self.papa != None) :
			self.papa.imprimir()
