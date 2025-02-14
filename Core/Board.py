from Cell import Cell
from copy import deepcopy
import pygame


class Board:
    def __init__(self, width, height, x_indentation, y_indentation, screen):
        self.screen = screen
        self.cells = pygame.sprite.Group()
        self.width = width
        self.height = height
        self.pre_data_board = []
        self.data_board = []
        self.ui_board = []
        self.x_indentation = x_indentation
        self.y_indentation = y_indentation
        self.cell_size = 40

    def initiate(self):
        for y in range(self.height):
            self.ui_board.append([])
            self.data_board.append([])
            for x in range(self.width):
                self.ui_board[y].append(Cell(self.cells, x, y, self.x_indentation, self.y_indentation,
                                             cell_size=self.cell_size))
                self.data_board[y].append(0)
        self.pre_data_board = deepcopy(self.data_board)

    def update_cells(self):
        self.cells.update()

    def draw_cells(self):
        self.cells.draw(self.screen)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                                 (x * self.cell_size + self.x_indentation,
                                  y * self.cell_size + self.y_indentation, self.cell_size,
                                  self.cell_size), 2)

    # Эту функцию удобно использовать для расстановки клеток на старте (пкм - 1 команда, лкм - 2)
    def get_cell(self, mouse_pos, button):
        board_width = self.width * self.cell_size
        board_height = self.height * self.cell_size
        if self.x_indentation < mouse_pos[0] < self.x_indentation + board_width:
            if self.y_indentation < mouse_pos[1] < self.y_indentation + board_height:
                cell_cords = (mouse_pos[1] - self.x_indentation) // self.cell_size, \
                             (mouse_pos[0] - self.y_indentation) // self.cell_size
                if self.ui_board[cell_cords[0]][cell_cords[1]].get_status():
                    self.ui_board[cell_cords[0]][cell_cords[1]].kill()
                    self.data_board[cell_cords[0]][cell_cords[1]] = 0
                elif button == 1:
                    self.ui_board[cell_cords[0]][cell_cords[1]].revive(1)
                    self.data_board[cell_cords[0]][cell_cords[1]] = 1
                elif button == 3:
                    self.ui_board[cell_cords[0]][cell_cords[1]].revive(2)
                    self.data_board[cell_cords[0]][cell_cords[1]] = 2
        return None

    # функция обновления поля
    def life_cycle(self):
        self.pre_data_board = deepcopy(self.data_board)
        for y in range(self.height):
            for x in range(self.width):
                if self.pre_data_board[y][x] == 0:
                    c_1 = self.get_cells_3n3(y, x, 1)
                    c_2 = self.get_cells_3n3(y, x, 2)
                    c_1_power = 0
                    c_2_power = 0
                    if c_1 == 3:
                        c_1_power = self.get_cells_4n4(y, x, 1)
                    if c_2 == 3:
                        c_2_power = self.get_cells_4n4(y, x, 2)
                    if c_1_power > 0 or c_2_power > 0:
                        command = 0
                        if c_1_power > c_2_power:
                            command = 1
                        if c_2_power > c_1_power:
                            command = 2
                        self.data_board[y][x] = command
                        self.ui_board[y][x].revive(command)
                else:
                    command = self.pre_data_board[y][x]
                    if 1 < self.get_cells_3n3(y, x, command) < 4:
                        pass
                    else:
                        self.data_board[y][x] = 0
                        self.ui_board[y][x].kill()

    def get_cells_3n3(self, y, x, command):
        cnt = 0
        for y_ in range(max(0, y - 2), min(y + 2, self.height)):
            for x_ in range(max(0, x - 2), min(x + 2, self.width)):
                if self.pre_data_board[y_][x_] == command and y_ != y and x_ != x:
                    cnt += 1
        return cnt

    def get_cells_4n4(self, y, x, command):
        cnt = 0

        for y_ in range(max(0, y - 3), min(y + 3, self.height)):
            for x_ in range(max(0, x - 3), min(x + 3, self.width)):
                if self.pre_data_board[y_][x_] == command and y_ != y and x_ != x:
                    cnt += 1
        return cnt



