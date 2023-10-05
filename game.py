import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

PRETO = (0,0,0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Tale of Awlren')

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Elf\elf_regular_hair.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)

while True:
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update
    pygame.display.flip()


