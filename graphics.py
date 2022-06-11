import pygame

# SETUP PYGAME/WINDOW
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Regicide")
pygame.display.set_icon(pygame.image.load("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\h1.png")) #FIX
WIDTH, HEIGHT = 1280, 720
WHITE, BLACK, RED, GREEN, BLUE, DARK_GREEN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (55, 77, 55)
FPS = 60
# CARD_PIXEL_HEIGHT, CARD_PIXEL_WIDTH, CARD_SHADOW_PIXEL_HEIGHT, CARD_SHADOW_PIXEL_WIDTH =  (42 * PIXEL_SCALE), (29 * PIXEL_SCALE), (40 * PIXEL_SCALE), (27 * PIXEL_SCALE)
window = pygame.display.set_mode((WIDTH, HEIGHT), 0,  32) # (width, height), depth flag (default = 0), color depth
psfont = pygame.font.Font("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\PressStart2P-vaV7.ttf", 20) # PressStart font

class gameobject():
    inanimation = False
    x, y = 0, 0

    def __init__(self, width, height, images=(), scale_factor=1):
        assert isinstance(images, tuple), "must give tuple to gameobject"

        self.sprites = []
        self.scale_factor = scale_factor
        for i in range(len(images)):
            self.sprites.append(pygame.transform.scale(pygame.image.load(images[i]), (scale_factor * width, scale_factor * height)))

    def update(self):
        pass

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 300, color) # text, antialias, color
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)