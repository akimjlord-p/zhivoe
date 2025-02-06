import os
import sys
import pygame


class Cell(pygame.sprite.Sprite):
    image = pygame.image.load('../media/Cell.png')

    def __init__(self, group, x, y):
        super().__init__(group)
        self.frames = []
        self.cur_frame = 0
        self.cut_sheet(Cell.image)
        self.rect = pygame.rect.Rect(0, 0, 100, 100)

        self.rect.x = x
        self.rect.y = y

    def cut_sheet(self, sheet):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 3,
                                sheet.get_height() // 3)
        for j in range(3):
            for i in range(3):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


size = width, height = 500, 500
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
pygame.display.set_caption('Инициализация игры')

Cell(all_sprites, 100, 100)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        clock.tick(10)
        screen.fill((255, 255, 255))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()

