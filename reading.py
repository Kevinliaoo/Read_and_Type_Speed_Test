import pygame
import time
import random
import wikipedia
import math

pygame.init()

text_font = pygame.font.SysFont ("comicsans", 40)

class Reading: 

	def __init__ (self, win): 
		self.width = 1200 
		self.height = 600
		self.win = win
		self.wordSize = 45
		self.positionLit = [i*self.wordSize for i in range(self.height//self.wordSize)]
		#Obtener una palabra random de words.txt para buscarlo en wikipedia
		with open ('texts/words.txt') as f: 
			data = f.read().split(',')
			i = random.randint (0, len(data)-1)
			self.searchWord = data[i]

		try: 
			self.content = wikipedia.summary(self.searchWord)
		except wikipedia.exceptions.DisambiguationError as e:
			self.content = wikipedia.summary (str(e.options[0]))

		#Lista de palabras del texto extraído
		self.wordSeparatedText = self.content.split(' ')
		#Separar self.content en fragmentos de 50 caracteres
		self.contentFragmented = []
		lineLength = 11
		lines = 11
		for i in range(lines):
			self.contentFragmented.append(self.fragmentText(i*lineLength, (i+1)*lineLength))
		self.ammountOfWords = lineLength*lines
		#Starting time
		self.time = time.time()
		self.tiempoFin = 0

	def fragmentText (self, start, end): 
		"""
		Esta función se encarga de fragmentar el self.content. 
		:param start: Integer
		:param end: Integer
		:return: list
		"""
		temp = ""
		for i in self.wordSeparatedText[start:end]: 
			temp += str(i) + " "
		return temp


	def run(self):
	    run = True

	    while run:
	        for event in pygame.event.get():
	        	if event.type == pygame.QUIT:
	        		run = False

	        	if event.type == pygame.KEYUP:
	        		teclado = pygame.key.name(event.key)
	        		if teclado == "return": 
	        			self.tiempoFin = math.floor(time.time() - self.time)
	        			run = False 

	        self.draw()

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


	def draw(self):
		self.win.fill([0,0,0])
		renglon = 0

		runtime = text_font.render(str(math.floor(time.time() - self.time)), 1, (255,255,255))
		self.win.blit(runtime, (0, self.positionLit[renglon]))
		renglon += 1

		for c in self.contentFragmented: 
			reading_content = text_font.render(c, 1, (255,255,255))
			self.win.blit(reading_content, (40, self.positionLit[renglon]))
			renglon += 1

		finish = text_font.render("Press enter to finish", 1, (255,0,0))
		self.win.blit(finish, (200, self.positionLit[renglon]))

		pygame.display.update()

	def displayResults (self): 
		"""
		Shows the results on screen.
		"""
		self.win.fill([0,0,0])

		endtime = text_font.render("Total time: "+str(self.tiempoFin)+" secs.", 1, (255,255,255))
		self.win.blit(endtime, (40, self.positionLit[1]))

		cantWords = text_font.render("Words read: "+str(self.ammountOfWords), 1, (255,255,255))
		self.win.blit(cantWords, (40, self.positionLit[2]))

		wpm = text_font.render("Words per minute: "+str((self.ammountOfWords*60)/self.tiempoFin), 1, (255,255,255))
		self.win.blit(wpm, (40, self.positionLit[3]))

		end = text_font.render("Press enter to end", 1, (255,0,0))
		self.win.blit(end, (40, self.positionLit[4]))

		pygame.display.update()