import pygame

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Reading and typing speed test")
    from main_menu.main_menu import MainMenu
    mainMenu = MainMenu(win)
    mainMenu.run()