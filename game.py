import pygame
import pytmx
import pyscroll

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_up(self):
        self.rect.y -= 3

    def move_down(self):
        self.rect.y += 3

    def move_left(self):
        self.rect.x -= 3

    def move_right(self):
        self.rect.x += 3

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygame Image Display")
        self.clock = pygame.time.Clock()
        self.running = True

        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame("./fichier Tiled.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 0.499  # Utiliser un point décimal pour dézoomer

        # Generer un joueur
        player_position  = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)


        # déssiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()

    def run(self):

        clock = pygame.time.Clock()
        # Boucle du jeu
        running = True

        while running:

            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.clock.tick(60)  # Utiliser self.clock pour limiter le framerate

        pygame.quit()