import pygame
from Board import Board


if __name__ == '__main__':
    pygame.init()
    size = 1920, 1000
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')
    board = Board(10, 10, 100, 100, screen)
    board.initiate()
    running = True
    clock = pygame.time.Clock()
    recycle = pygame.USEREVENT + 1
    pygame.time.set_timer(recycle, 5000)
    start = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_cell(event.pos, event.button)
            if event.type == pygame.WINDOWMINIMIZED:
                start = True
            if event.type == recycle and start:
                board.life_cycle()
        clock.tick(15)
        screen.fill((255, 255, 255))
        board.update_cells()
        board.draw_cells()
        board.render(screen)
        pygame.display.flip()
    pygame.quit()