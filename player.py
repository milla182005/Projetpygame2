import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("player.png")
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.position = [x, y]
        self.speed = 3

    def move_right(self): self.position[0] += self.speed

    def move_left(self): self.position[0] -= self.speed

    def move_up(self): self.position[1] -= self.speed

    def move_down(self): self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface((32, 32))
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image