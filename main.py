# SETUP PYTHON
import pygame, sys
from pygame import mixer

# REGICIDE MODULES
import cardy as cy
import regicide
import graphics as g

PIXEL_SCALE = 3

def main():
    # mixer.music.load('C:\\Users\\RobbN\\Documents\Programs\\_Python\\Regicide\\audio\\opening.mp3')
    # mixer.music.play()

    reg()

    print('Success!!')

def reg():
    # Set enemy deck
    enemy = regicide.enemy(cy.deck((cy.card('h', 11), cy.card('h', 12), cy.card('h', 13), cy.card('d', 11), cy.card('d', 12), cy.card('d', 13), cy.card('s', 11), cy.card('s', 12), cy.card('s', 13), cy.card('c', 11), cy.card('c', 12), cy.card('c', 13))))
    print(f"CURR SUITE -> {enemy.current_card.suite}, CURR RANK -> {enemy.current_card.rank}")
    print("ENEMY DECK:")
    enemy.deck.printdeck()


    # card_visuals = g.gameobject(29, 42, ("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\c1.png",), PIXEL_SCALE)

    image = []
    # shadowimage = pygame.transform.scale(pygame.image.load("C:\\Users\\RobbN\Documents\\Programs\\_Python\\Regicide\\graphics\\shadow.png"), (g.CARD_SHADOW_PIXEL_WIDTH, g.CARD_SHADOW_PIXEL_HEIGHT))

    while 1:
        g.window.fill(g.DARK_GREEN)
        g.draw_text('Regicide: main menu', g.psfont, g.WHITE, g.window, 600, 350)
        # g.window.blit(card_visuals.sprites[0], (card_visuals.x, card_visuals.y))

        for event in pygame.event.get():
            if event.type == g.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == g.KEYDOWN:
                if event.key == g.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        g.mainClock.tick(g.FPS)

if __name__ == "__main__":
    main()