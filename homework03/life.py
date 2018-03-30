import pygame
from pygame.locals import *
import random

class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        # PUT YOUR CODE HERE

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE
            self.draw_cell_list(self.clist)
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
            self.update_cell_list(self.clist)
        pygame.quit()

    def cell_list(self, randomize=True):
        """ Создание списка клеток.

        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        # PUT YOUR CODE HERE
        for i in range(self.cell_height):
            temp = []
            for g in range(self.cell_width):
                if randomize:
                    temp.append(random.randint(0, 1))
                else:
                    temp.append(0)
            self.clist.append(temp)
        return self.clist

    def draw_cell_list(self, rects):
        """ Отображение списка клеток

        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for i in range(len(rects)):
            for g in range(len(rects[i])):
                if rects[i][g]:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (g*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (g*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))

    def get_neighbours(self, cell):
        """ Вернуть список соседей для указанной ячейки

        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        # PUT YOUR CODE HERE
        if (cell[0] - 1 >= 0) & (cell[1] - 1 >= 0):
            neighbours.append(self.clist[cell[0] - 1][cell[1] - 1])

        if cell[0] - 1 >= 0:
            neighbours.append(self.clist[cell[0] - 1][cell[1]])

        if (cell[0] - 1 >= 0) & (cell[1] + 1 < self.cell_width):
            neighbours.append(self.clist[cell[0] - 1][cell[1] + 1])

        if cell[1] + 1 < self.cell_width:
            neighbours.append(self.clist[cell[0]][cell[1] + 1])

        if (cell[0] + 1 < self.cell_height) & (cell[1] + 1 < self.cell_width):
            neighbours.append(self.clist[cell[0] + 1][cell[1] + 1])

        if cell[0] + 1 < self.cell_height:
            neighbours.append(self.clist[cell[0] + 1][cell[1]])

        if (cell[0] + 1 < self.cell_height) & (cell[1] - 1 >= 0):
            neighbours.append(self.clist[cell[0] + 1][cell[1] - 1])

        if cell[1] - 1 >= 0:
            neighbours.append(self.clist[cell[0]][cell[1] - 1])


        return neighbours

    def update_cell_list(self, cell_list):
        """ Выполнить один шаг игры.

        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.

        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = []
        # PUT YOUR CODE HERE
        for i in range(len(cell_list)):
            temp = []
            for g in range(len(cell_list[i])):
                if cell_list[i][g] == 0:
                    if self.get_neighbours((i, g)).count(1) == 3:
                        temp.append(1)
                    else:
                        temp.append(0)
                else:
                    if self.get_neighbours((i, g)).count(1) in range(2,4):
                        temp.append(1)
                    else:
                        temp.append(0)
            new_clist.append(temp)

        self.clist = new_clist
        return self.clist

if __name__ == '__main__':
    game = GameOfLife(800, 600, 20, 10)
    print(game.cell_list(randomize=True))
    game.run()
    # clist = game.cell_list(randomize=True)
    # game.draw_cell_list(clist)
    # pygame.display.flip()
    # print(clist)
    # time.sleep(5)

