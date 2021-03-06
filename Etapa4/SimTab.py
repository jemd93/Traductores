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

	def agregarDecInit(self,lista,check) :

		# Descripción: Método para agregar lista de declaraciones de DecListInit
		#			   a la tabla de simbolos.
  		# Parámetros: - lista: lista de declaraciones de bots.
  		#			  - check: booleano que indica comportamiento inexistente.

		if (lista.h2 != None) :
			self.agregarDecList(lista.h1,lista.h2,check)
		else :
			self.agregarDecList(lista.h1,None,check)

	def agregarDecList(self,dec,lista,check) :

		# Descripción: Método para agregar todas las declaraciones de una 
		# 			   DecList en la tabla de simbolos.
  		# Parámetros: - dec: declaracion a agregar en la lista de declaraciones.
  		# 			  - lista: lista de declaraciones de bots.
  		# 			  - check: booleano que indica comportamiento inexistente.

		self.agregarListaId(dec.h3,dec.h1,dec.h4,check)
		if (lista != None) :
			self.agregarDecList(lista.h1,lista.h2,check)

	def agregarListaId(self,lista,tipo,comps,check) :

		# Descripción: Método para agregar todos los ids de una listaId con sus 
		# 			   respectivos tipos y comportamientos.
  		# Parámetros: - lista: lista de ids de bots.
  		#			  - tipo: tipo de los identificadores de los bots.
  		#			  - comps: tabla hash de comportamientos para los bots.
  		# 			  - check: booleano que indica comportamiento inexistente.

		if (lista.h1.elem in self.tabhash) and check:
			print("Error : la variable "+lista.h1.elem+" ya fue declarada anteriormente")
			exit(1)
		else :
			diccComps = comps.generarTablaComps({},False)
			self.tabhash[lista.h1.elem] = [[tipo.inst,None,0,0,0],diccComps] 
			if (lista.h2 != None) :
				self.agregarListaId(lista.h2,tipo,comps,check)

	def updateValue(self,clave,val):

		# Descripción: Método para modificar y/o actualizar el valor de un bot.
		# Parámetros: - clave: nombre del bot a buscar en la tabla hash
		#			  - val: valor a actualizar en el bot.

		if clave in self.tabhash :
			tipo = self.tabhash[clave][0][0]
			if ((((isinstance(val,float) or isinstance(val,int)) and not(isinstance(val,bool))) and 
				(tipo == 'int')) or (isinstance(val,bool) and tipo == 'bool') 
				or (isinstance(val,str) and tipo == 'char')) :
				if (tipo == 'char') and len(val) > 1 and not(val == "\\n" or val == "\\t" or val == "\\'"):
					print("Error : La entrada introducida no es valida.")
					exit(1)

				self.tabhash[clave][0][1] = val
			else :
				if val == None :
					print("Error : La variable "+clave+" no ha sido inicializada")
					exit(1)
				print("Error : El tipo del valor a asignar y la variable no son iguales")
				exit(1)
		else :
			if (self.papa != None):
				self.papa.updateValue(clave,val)

	def updatePos(self,clave,posx=None,posy=None):

		# Descripción: Método para modificar y/o actualizar la posición tanto 
		#			   en x como en y, de un bot.
		# Parámetros: - clave: nombre del bot a buscar en la tabla hash.
		#			  - posx: posición a actualizar en el bot.
		# 			  - posy: posición a actualizar en el bot.

		if clave in self.tabhash:
			if posx != None:
				self.tabhash[clave][0][3] = self.tabhash[clave][0][3] + posx
			elif posy != None:
				self.tabhash[clave][0][4] = self.tabhash[clave][0][4] + posy
		else:
			if (self.papa != None):
				self.papa.updatePos(clave,posx,posy)


	# FUNCIONES DE CAMBIOS EN LA TABLA DURANTE EJECUCION

	def activate(self,lista):

		# Descripción: Método para activar el bot cuando la instrucción en
		#			   execute lo indica.
		# Parámetros: - lista: un bot o la lista de bots a activar.

		if lista.h1.elem in self.tabhash:
			if self.tabhash[lista.h1.elem][0][2] == 1:
				print("Error ya el robot "+str(lista.h1.elem)+" ha sido activado anteriormente")
				exit(1)
			self.tabhash[lista.h1.elem][0][2] = 1
			if ('activation' in self.tabhash[lista.h1.elem][1]):
				# El run de aqui es el run del ArbolComp asociado a activate
				self.tabhash[lista.h1.elem][1]['activation'].run(lista.h1.elem)
				if lista.h2 != None :
					self.activate(lista.h2)
		else:
			if self.papa != None:
				self.papa.activate(lista)

	def deactivate(self,lista):

		# Descripción: Método para desactivar el bot cuando la instrucción en
		#			   execute lo indica.
		# Parámetros: - lista: un bot o la lista de bots a desactivar.

		if lista.h1.elem in self.tabhash:
			if self.tabhash[lista.h1.elem][0][2] == 0:
				print("Error ya el robot "+str(lista.h1.elem)+" ha sido desactivado anteriormente")
				exit(1)
			self.tabhash[lista.h1.elem][0][2] = 0		
			if ('deactivation' in self.tabhash[lista.h1.elem][1]):
				self.tabhash[lista.h1.elem][1]['deactivation'].run(lista.h1.elem)
				if lista.h2 != None :
					self.deactivate(lista.h2)
		else:
			if self.papa != None:
				self.papa.deactivate(lista)

	def advance(self,lista):

		# Descripción: Método para avanzar el bot cuando la instrucción en
		#			   execute lo indica.
		# Parámetros: - lista: un bot o la lista de bots a avanzar.

		# Busca algun comportamiento con expresiones :
		ran = False
		if ('advance' in self.tabhash[lista.h1.elem][1]):
			for par in self.tabhash[lista.h1.elem][1]['advance']:
				if par[0].evaluate(self,lista.h1.elem) :
					ran = True
					par[1].run(lista.h1.elem)
					break

			# En caso de que no existan, o ninguna expresion se cumpla, si hay comp de default, lo corre
			if not(ran) and ('default' in self.tabhash[lista.h1.elem][1]):
				ran = True
				self.tabhash[lista.h1.elem][1]['default'].run(lista.h1.elem)
			if lista.h2 != None :
				self.advance(lista.h2)

		elif ('default' in self.tabhash[lista.h1.elem][1]):
			self.tabhash[lista.h1.elem][1]['default'].run(lista.h1.elem)
			if lista.h2 != None :
				self.advance(lista.h2)

	def imprimir(self):

		# Descripción: Método para imprimir la/las tablas de hashs. 

		print(self.tabhash)
		if (self.papa != None) :
			self.papa.imprimir()