import pygame


class Cell(pygame.sprite.Sprite):
    sprite_sheet = alive_cell = pygame.image.load('../media/Cell.png')
    image = dead_cell = pygame.image.load('../media/dead_cell.png')

    def __init__(self, group, x, y, x_indent, y_indent):
        self.is_alive = False
        super().__init__(group)
        self.frames = []
        self.cur_frame = 0
        self.cut_sheet(Cell.alive_cell)
        self.rect = pygame.rect.Rect(0, 0, 100, 100)

        self.rect.x = x * 100 + x_indent
        self.rect.y = y * 100 + y_indent

    def cut_sheet(self, sheet):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 3,
                                sheet.get_height() // 3)
        for j in range(3):
            for i in range(3):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def revive(self):
        self.is_alive = True
        self.cur_frame = 0

    def kill(self):
        self.is_alive = False

    def get_status(self):
        return self.is_alive

    def update(self):
        if self.is_alive:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        else:
            self.image = Cell.dead_cell

# Для теста
# size = width, height = 1920, 1000
# screen = pygame.display.set_mode(size)
# all_sprites = pygame.sprite.Group()
# pygame.display.set_caption('Инициализация игры')

# Cell(all_sprites, 0, 0, 300, 300).kill()
# Cell(all_sprites, 1, 1, 300, 300)
# clock = pygame.time.Clock()
# running = True

# while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#    clock.tick(10)
#    screen.fill((255, 255, 255))
#    all_sprites.update()
#   all_sprites.draw(screen)
#    pygame.display.flip()
# pygame.quit()
