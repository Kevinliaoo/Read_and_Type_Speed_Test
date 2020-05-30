import pygame
import time
import math
import random

pygame.init()
clock = pygame.time.Clock()

timer_font = pygame.font.SysFont ("comicsans", 40)
title_font = pygame.font.SysFont ("comicsans", 70)

class Tiping: 

	def __init__ (self, win): 
		self.width = 800 
		self.height = 600
		self.win = win
		#Starting time
		self.time = time.time()
		#End time (configurado una vez terminado)
		self.tiempoFin = 0
		#Palabras que van a ir apareciendo
		self.words = []
		self.wordSize = 20
		#Lo llamo wordsTyped, pero en realidad cuenta la cantidad de letras, no palabras.
		self.wordsTyped = 0
		#La palabra que el usuario está tipiando
		self.currentTypingWord = None
		#Cantidad de letras tipeadas de currentTypingWord
		self.letrasTipeadasDeEstaPalabra = 0
		#El´índice del String de la letra tipeando
		self.currentTypingWordIndex = 0
		#Verdadero si el usuario está tipeando una palabra
		self.typingWord = False 
		
	def run(self):
		#Variables
	    run = True
	    FPS = 60
	    contadorAddNewWord = 0
	    #Positioning new words
	    positionLit = [i*self.wordSize for i in range(self.height//self.wordSize)]
	    positionLit.pop(0)
	    indexPosList = 0
	    #Almacena el objeto Word que se está tipeando
	    wrongWords = 0
	    acabaDeTipear = False
	    #Inicializar la lista de palabras con una palabra
	    self.words.append (Word(self.win, positionLit[indexPosList], self.wordSize))

	    while run:

	    	clock.tick (FPS)
	    	self.draw()

	    	#Resetea el self.currentTypingWord
	    	if self.typingWord == False: 
	    		self.currentTypingWord = None

	    	for event in pygame.event.get():
	    		
	    		if event.type == pygame.QUIT:
	    			run = False

	    		#Si se levanta una tecla
	    		if event.type == pygame.KEYUP: 

	    			#Tecla que el usuario presiona
	    			teclado = pygame.key.name(event.key)

	    			# #Si el usuario presiona enter, termina el juego
	    			if teclado == "return": 
	    				self.tiempoFin = math.floor(time.time() - self.time)
	    				run = False

	    			# #Si el usuario presiona la barra espaciadora, saltea la palabra.
	    			if teclado == "space": 
	    				self.resetFields()

	    			#En busca de la primera palabra
	    			if self.typingWord == False and acabaDeTipear == False: 
	    				for w in self.words: 
	    					if teclado == w.word[0]:
	    						self.currentTypingWord = w
	    						self.typingWord = True
	    						self.wordsTyped += 1
	    						self.letrasTipeadasDeEstaPalabra += 1
	    						self.currentTypingWordIndex += 1
	    						w.isTyping()
	    						acabaDeTipear = False
	    						break

	    			elif acabaDeTipear == True: 
	    				acabaDeTipear = False
	    			
	    			#Hay una palabra para ser tipeada
	    			elif self.typingWord == True: 
	    				#Tipea bien
	    				if teclado == self.currentTypingWord.word[self.currentTypingWordIndex]: 
	    					self.wordsTyped += 1
	    					self.letrasTipeadasDeEstaPalabra += 1
	    				#Tipea mal
	    				else: 
	    					wrongWords += 1
	    				self.currentTypingWordIndex += 1

	    			#Se encarga de resetear los valores una vez tipeado la palabra
	    			if self.currentTypingWord != None:
		    			if self.currentTypingWordIndex == len(self.currentTypingWord.word)-1: 
		    				self.typingWord = False
		    				self.currentTypingWordIndex = 0
		    				self.words.remove (self.currentTypingWord)
		    				self.letrasTipeadasDeEstaPalabra = 0
		    				acabaDeTipear = True

		    		#Hacer que la lista positionLit sea una lista ciruclar
	    			if indexPosList == len(positionLit)-1: 
	    				indexPosList = 0
	    			
	    			#Hacer que aparezca una nueva palabra cada 3 letras tipeadas
	    			if contadorAddNewWord == 3:
		    			self.words.append (Word(self.win, positionLit[indexPosList], self.wordSize))
		    			contadorAddNewWord = 0

	    			contadorAddNewWord += 1
	    			indexPosList += 1
	    			time.sleep(0.01)

	    	for w in self.words:
	    		if w.x == 0: 
	    			self.words.remove (w)
	    			self.resetFields()
	    		w.move()

	    showResults = True
	    while showResults: 

	    	self.displayResults()

	    	for event in pygame.event.get():
	    		
	    		if event.type == pygame.QUIT:
	    			run = False

	    		if event.type == pygame.KEYUP: 
	    			teclado = pygame.key.name(event.key)
	    			#Presionar enter para salir
	    			if teclado == "return": 
	    				showResults = False 

	def resetFields (self): 
		"""
		Esta función elimina todos los valores de las variables importantes. 
		Les pone valor = 0
		"""
		self.currentTypingWord = None
		self.letrasTipeadasDeEstaPalabra = 0
		self.currentTypingWordIndex = 0
		self.typingWord = False 
		if self.currentTypingWord != None: 
			self.words.remove (self.currentTypingWord)

	def draw(self):
		"""
		Redraw the pygame window.
		"""
		self.win.fill([0,0,0])

		runtime = timer_font.render(str(math.floor(time.time() - self.time)), 1, (255,255,255))
		self.win.blit(runtime, (0, 0))

		score = timer_font.render("Score: "+str(self.wordsTyped), 1, (255,255,255))
		self.win.blit(score, (self.width/2-20, 0))

		if self.currentTypingWord != None:
			restante = timer_font.render("Left: "+str(len(self.currentTypingWord.word)-self.letrasTipeadasDeEstaPalabra), 1, (255,255,255))
			self.win.blit(restante, (self.width-100, 0))

		for w in self.words: 
			w.draw()
		
		pygame.display.update()

	def displayResults (self): 
		"""
		Shows the results on screen.
		"""
		self.win.fill([0,0,0])

		endtime = timer_font.render("Total time: "+str(self.tiempoFin)+" secs.", 1, (255,255,255))
		self.win.blit(endtime, (40, 0))

		cantWords = timer_font.render("Letters typed: "+str(self.wordsTyped), 1, (255,255,255))
		self.win.blit(cantWords, (40, 50))

		wpm = timer_font.render("Letters per minute: "+str((self.wordsTyped*60)/self.tiempoFin), 1, (255,255,255))
		self.win.blit(wpm, (40, 100))

		end = timer_font.render("Press enter to end", 1, (255,0,0))
		self.win.blit(end, (40, 150))

		pygame.display.update()

class Word: 

	def __init__ (self, win, y, size): 
		"""
		Obtiene una palabra al azar del archivo words.txt y lo almacena en la variable self.words. 
		La coordenada x comienza del borde derecho de la pantalla.
		Altura y tamaño son pasados como parámetros.
		El color es blanco, pero si se está tipeando la palabra se convierte en verde. 
		"""
		with open ('texts/words.txt') as f: 
			data = f.read().split(',')
			i = random.randint (0, len(data)-1)
			self.word = data[i]
		self.vel = 1
		self.size = size
		self.win = win
		self.x = win.get_width()-50
		self.y = y
		self.color = (255,255,255)

	def __str__ (self): 
		return self.word

	def move (self): 
		self.x -= self.vel

	def isTyping (self): 
		"""
		Sets the word color to green when user is typing this word.
		"""
		self.color = (0,255,0)

	def draw (self): 
		palabra = timer_font.render(self.word, 1, self.color)
		self.win.blit(palabra, (self.x, self.y))