# SETUP PYTHON
import pygame, sys

# REGICIDE MODULES
import cardy as cy
import regicide

# SETUP PYGAME/WINDOW
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Regicide")
pygame.display.set_icon(pygame.image.load("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\h1.png")) #FIX
WIDTH, HEIGHT = 1280, 720
WHITE, BLACK, RED, GREEN, BLUE, DARK_GREEN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (55, 77, 55)
FPS = 60
PIXEL_SCALE = 3
CARD_PIXEL_HEIGHT, CARD_PIXEL_WIDTH, CARD_SHADOW_PIXEL_HEIGHT, CARD_SHADOW_PIXEL_WIDTH =  (42 * PIXEL_SCALE), (29 * PIXEL_SCALE), (40 * PIXEL_SCALE), (27 * PIXEL_SCALE)
window = pygame.display.set_mode((WIDTH, HEIGHT), 0,  32) # (width, height), depth flag (default = 0), color depth
font = pygame.font.Font("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\PressStart2P-vaV7.ttf", 20) # (font, size)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 300, color) # text, antialias, color
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    my_deck = cy.deck([cy.card(1, 13), cy.card(3, 4)])

    player = regicide.player(8, my_deck)
    print(player.health)
    print(player.updatehealth())

    reg()

    print('Success!!')

def reg():
    image = []
    shadowimage = pygame.transform.scale(pygame.image.load("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\shadow.png"), (CARD_SHADOW_PIXEL_WIDTH, CARD_SHADOW_PIXEL_HEIGHT))
    for i in range(1, 11):
        current_name = ("c%d.png" % i)
        image.append(pygame.image.load("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\" + current_name)) #FIX
        image[i - 1] = pygame.transform.scale(image[i - 1], (CARD_PIXEL_WIDTH, CARD_PIXEL_HEIGHT))

    count = 0
    
    while 1:
        count += 1
        if (count // 60) > 9:
            count = 0
        card_set = count // 60
        window.fill(DARK_GREEN)
        window.blit(image[card_set], ((WIDTH / 2), (HEIGHT / 2)))
        window.blit(shadowimage, (600, 200))
        draw_text('Regicide: main menu', font, WHITE, window, 600, 350)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(FPS)

if __name__ == "__main__":
    main()