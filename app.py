import pygame, sys, random
from colores import Colores


pygame.init()

# Crear una ventana
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
score = 0
bottle_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()


# Se crea los sprites de las botellas
class Bottle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png").convert()
        # Se quita el color negro del fondo
        self.image.set_colorkey(Colores.BLACK)
        # Se toman la posicion
        self.rect = self.image.get_rect()


# Se crea los sprites de las botellas
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
    bottle.rect.x = random.randrange(900)
    bottle.rect.y = random.randrange(600)

    bottle_list.add(bottle)
    all_sprite_list.add(bottle)

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

    # Para guardar el marcador
    for botlle in bottle_collide_list:
        score += 1

    # se acaba el juego
    if score == 20:
        screen.fill(Colores.WHITE)
        font = pygame.font.SysFont("arial", 24)
        text = font.render("Reciclaste todas las botellas!!!", True, Colores.BLACK)
        screen.blit(text, (200, 250))

    pygame.display.flip()
    clock.tick(60)
