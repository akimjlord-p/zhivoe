import pygame


class Cell(pygame.sprite.Sprite):
    sprite_sheet_c1 = alive_cell_c1 = pygame.image.load('../media/cell_c1.png')
    sprite_sheet_c2 = alive_cell_c2 = pygame.image.load('../media/cell_c2.png')
    image = dead_cell = pygame.image.load('../media/dead_cell.png')

    def __init__(self, group, x, y, x_indent, y_indent, cell_size):
        self.cell_size = cell_size
        self.is_alive = False
        super().__init__(group)
        self.command = 0
        self.frames_c1 = []
        self.frames_c2 = []
        self.cur_frame = 0
        self.cut_sheet_c1(Cell.alive_cell_c1)
        self.cut_sheet_c2(Cell.alive_cell_c2)
        self.rect = pygame.rect.Rect(0, 0, cell_size, cell_size)

        self.rect.x = x * cell_size + x_indent
        self.rect.y = y * cell_size + y_indent

    def cut_sheet_c1(self, sheet):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 3,
                                sheet.get_height() // 3)
        for j in range(3):
            for i in range(3):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames_c1.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def cut_sheet_c2(self, sheet):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 3,
                                sheet.get_height() // 3)
        for j in range(3):
            for i in range(3):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames_c2.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def revive(self, command):
        self.is_alive = True
        self.cur_frame = 0
        self.command = command

    def kill(self):
        self.is_alive = False
        self.command = 0

    def get_status(self):
        return self.is_alive

    def update(self):
        if self.is_alive and self.command == 1:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_c1)
            self.image = self.frames_c1[self.cur_frame]
        elif self.is_alive and self.command == 2:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_c2)
            self.image = self.frames_c2[self.cur_frame]
        else:
            self.image = Cell.dead_cell



