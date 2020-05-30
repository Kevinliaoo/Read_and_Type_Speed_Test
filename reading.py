import pygame

pygame.init()


class Reading: 

	def __init__ (self, win): 
		self.width = 800 
		self.height = 600
		self.win = win
		self.title_font = pygame.font.SysFont("comicsans", 70)

	def run(self):
	    run = True

	    while run:
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                run = False

	        self.draw()


	def draw(self):
		self.win.fill([0,0,0])
		title_label = self.title_font.render("Reading mode", 1, (255,255,255))
		self.win.blit(title_label, (self.width/2 - title_label.get_width()/2, self.height/2))
		pygame.display.update()