import pygame
from forme import Forme


pygame.init()
all_draw_rect = pygame.sprite.Group()


# default pygame variableult pygame variable
screenSize = (1080, 920)
screenColor = "#264653"
screen = pygame.display.set_mode(screenSize)

cursor = pygame.Rect(0, 0, 10, 10)
onClick = [False, ""]
mouseDown = False
spaceDown = False
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            events_key = {
                pygame.K_1: Forme('1'),
                pygame.K_2: Forme('2'),
            }
            if event.key in [pygame.K_1, pygame.K_2]:
                formes = events_key[event.key]
                all_draw_rect.add(formes)
            elif event.key == pygame.K_SPACE:
                if spaceDown:
                    spaceDown = False
                else:
                    spaceDown = True
            elif event.key == pygame.K_DELETE:
                all_draw_rect = pygame.sprite.Group()

        elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

    if mouseDown:
        for draw in all_draw_rect:
            if cursor.colliderect(draw.rect):

screenSize = (1080, 920)
screenColor = "#264653"
screen = pygame.display.set_mode(screenSize)

cursor = pygame.Rect(0, 0, 10, 10)
onClick = [False, ""]
mouseDown = False
spaceDown = False
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            events_key = {
                pygame.K_1: Forme('1'),
                pygame.K_2: Forme('2'),
            }
            if event.key in [pygame.K_1, pygame.K_2]:
                formes = events_key[event.key]
                all_draw_rect.add(formes)
            elif event.key == pygame.K_SPACE:
                if spaceDown:
                    spaceDown = False
                else:
                    spaceDown = True
            elif event.key == pygame.K_DELETE:
                all_draw_rect = pygame.sprite.Group()

        elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

    if mouseDown:
        for draw in all_draw_rect:
            if cursor.colliderect(draw.rect):
                draw.rect.center = pygame.mouse.get_pos()
    if spaceDown or not spaceDown:
        for forme in all_draw_rect:
            if not mouseDown and not forme.rect.colliderect(cursor):
                forme.updateGravity(0.001, spaceDown)

    screen.fill(screenColor)
    cursor.center = pygame.mouse.get_pos()
    pygame.draw.rect(screen, pygame.Color(screenColor), cursor)

    for draws in all_draw_rect:
        pygame.draw.rect(screen, draws.color, draws.rect)

    pygame.display.flip()
    pygame.display.update()

pygame.quit()