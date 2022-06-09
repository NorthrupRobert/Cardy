# Setup python
import pygame, sys

# Import Regicide Modules
import card

# Setup pygame/window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Regicide")
WIDTH, HEIGTH = 500, 724
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGTH), 0,  32) # (width, height), depth flag (default = 0), color depth
font = pygame.font.SysFont("calibri", 40) # (font, size)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 100, color) # text, antialias, color
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    in_menu = True
    image = []
    for i in range(1, 11):
        current_name = ("c%d.png" % i)
        image.append(pygame.image.load("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\" + current_name))
        image[i - 1] = pygame.transform.scale(image[i - 1], (WIDTH, HEIGTH))

    count = 0
    
    while in_menu:
        count += 1
        if (count // 60) > 9:
            count = 0
        card_set = count // 60
        window.fill(BLACK)
        window.blit(image[card_set], (0, 0))
        draw_text('main menu', font, WHITE, window, 0, 0)


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

def main():
    # firstCard = card.card(1, 2)

    main_menu()

if __name__ == "__main__":
    main()