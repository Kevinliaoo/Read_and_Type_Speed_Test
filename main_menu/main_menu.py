import pygame
from tiping import Tiping
from reading import Reading

class MainMenu: 

    def __init__ (self, win): 
        self.width = 800
        self.height = 600
        self.win = win
        self.btn_type = (0, 0, 50, 50)
        self.btn_read = (60, 0, 50, 50)
        self.title_font = pygame.font.SysFont("comicsans", 70)

    def run(self):
        run = True

        while run:


            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_t]:
                tiping = Tiping (self.win)
                tiping.run ()
                del tiping

            elif keys[pygame.K_r]: 
                reading = Reading (self.win)
                reading.run ()
                del reading

        pygame.quit()

    def draw(self):
        self.win.fill([0,0,0])
        title_label = self.title_font.render("Press 'T' to type or 'R' to read", 1, (255,255,255))
        self.win.blit(title_label, (self.width/2 - title_label.get_width()/2, self.height/2))
        pygame.display.update()

