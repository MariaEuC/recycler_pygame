import pygame, sys, random
import pygame_menu
from colores import Colores


pygame.init()

# Crear una ventana
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
score = 0
enemy_score = 0
bottle_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()


# Se crean los sprites de las botellas
class Bottle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png").convert()
        # Se quita el color negro del fondo
        self.image.set_colorkey(Colores.BLACK)
        # Se toman la posicion
        self.rect = self.image.get_rect()

# Se crean los sprites de los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("basura.png").convert()
        # Se quita el color negro del fondo
        self.image.set_colorkey(Colores.BLACK)
        # Se toman la posicion
        self.rect = self.image.get_rect()

# Se crean los sprites del reciclador
class Recycler(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recycler.png").convert()
        self.image.set_colorkey(Colores.BLACK)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (60, 60))


recycler = Recycler()

all_sprite_list.add(recycler)


for i in range(20):
    bottle = Bottle()
    bottle.rect.x = random.randrange(800)
    bottle.rect.y = random.randrange(500)

    bottle_list.add(bottle)
    all_sprite_list.add(bottle)

for i in range(5):
    enemy = Enemy()
    enemy.rect.x = random.randrange(900)
    enemy.rect.y = random.randrange(600)

    enemy_list.add(enemy)
    all_sprite_list.add(enemy)


def start_the_game():
    score = 0
    enemy_score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Se obtine la posicion del mouse
        x, y = pygame.mouse.get_pos()

        # Color de fondo
        screen.fill(Colores.GRASS)

        # Area de dibujo
        all_sprite_list.draw(screen)

        # Para mover el reclicador en el tablero
        recycler.rect.x = x
        recycler.rect.y = y

        # Se detectan las colisiones
        bottle_collide_list = pygame.sprite.spritecollide(recycler, bottle_list, True)
        # Se detectan las colisiones
        enemy_collide_list = pygame.sprite.spritecollide(recycler, enemy_list, True)


        # Para guardar el marcador
        for botlle in bottle_collide_list:
            score += 1
        for enemy in enemy_collide_list:
            enemy_score += 1

        # se acaba el juego
        if enemy_score > 0:
            screen.fill(Colores.WHITE)
            font = pygame.font.SysFont("arial", 24)
            text = font.render(
                "Reciclaste una basura enemigo perdiste!!!", True, Colores.BLACK)
            screen.blit(text, (200, 250))
        if score == 20:
            screen.fill(Colores.WHITE)
            font = pygame.font.SysFont("arial", 24)
            text = font.render("Reciclaste todas las botellas!!!", True, Colores.BLACK)
            screen.blit(text, (200, 250))

        pygame.display.flip()
        clock.tick(60)

menu = pygame_menu.Menu('Bienvenido',400,300, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('Jugar', start_the_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(screen)

