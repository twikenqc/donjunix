import pygame
import itertools, random
pygame.init()


class Game:

    def __init__(self):
        self.player = Player()
        self.monster = Monster()
        self.pressed = {}

class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bg.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 665
        self.rect.y = 70

    def kill(self):
        self.rect.x = 3000
        monstre = False
        game.pressed[event.key] = False


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('icone/icone.png')
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 235
        self.velocity = 170

    def move_right(self):
        self.rect.x += self.velocity
        game.pressed[event.key] = False

    def move_left(self):
        self.rect.x -= self.velocity
        game.pressed[event.key] = False

    def move_up(self):
        self.rect.y -= self.velocity
        game.pressed[event.key] = False

    def move_down(self):
        self.rect.y += self.velocity
        game.pressed[event.key] = False

    def start_pos(self):
        self.rect.x = 65
        self.rect.y = 235



#arriere plan
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((750, 500))
background = pygame.image.load('plato.png')

#instance Player
player = Player()
monster = Monster()

#instance Game
game = Game()

running = True
action = False
killMonster = False

tour = 1
tourMax = 1



while running:

    background = pygame.transform.scale(background,(750,500))
    screen.blit(background, (0, 0))

    game.player.image = pygame.transform.scale(game.player.image,(30,30))
    screen.blit(game.player.image, game.player.rect)

    game.monster.image = pygame.transform.scale(game.monster.image,(30,30))
    screen.blit(game.monster.image, game.monster.rect)

    pygame.display.flip()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True


    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
        action = True
    if game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
        action = True
    if game.pressed.get(pygame.K_UP):
        game.player.move_up()
        action = True
    if game.pressed.get(pygame.K_DOWN):
        game.player.move_down()
        action = True


    if game.pressed.get(pygame.K_1):
        game.monster.kill()
        action += 1
        killMonster = True


    if action:
        tour += 1
        tourMax += 1
        action = False
    if tour > 4:
        tour -= 4
    if tourMax == 21:
        game.player.start_pos()
        tourMax = 0



    print(game.pressed)
    print("joueur",tour,"a vous !")
    print(tourMax)
    if killMonster:
        print("vous avez tuer le monstre")

