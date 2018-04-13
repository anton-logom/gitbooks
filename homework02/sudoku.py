import random
import threading
import time

def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    rez = []
    for i in range(0, len(values), n):
        rez.append(values[i:(i+n):])
    return rez


def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return values[pos[0]]


def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    rez = []
    for i in values:
        rez.append(i[pos[1]])
    return rez


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    rez = []
    for i in range(0, len(values), 3):
        if pos[0] in range(i, i+3):
            for j in range(0, len(values[i]), 3):
                if pos[1] in range(j, j + 3):
                    for k in range(i, i+3):
                        for m in range(j, j+3):
                            rez.append(values[k][m])
    return rez


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    rez = [-1, -1]
    for i in grid:
        rez[0] += 1
        for j in i:
            rez[1] += 1
            if j == '.':
                return tuple(rez)
        rez[1] = -1
    # return tuple(rez)


def find_possible_values(grid, pos):
    """ Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    col = get_col(grid, pos)
    row = get_row(grid, pos)
    kv = get_block(grid, pos)
    zn = set()
    for i in range(1, 10):
        if (col.count(str(i)) == 0) & (row.count(str(i)) == 0) & (kv.count(str(i)) == 0):
            zn.add(str(i))
    return zn


def solve(grid):
    """ Решение пазла, заданного в grid
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    """
    pos = find_empty_positions(grid)
    if not pos:
        return grid
    for i in find_possible_values(grid, pos):
        grid[pos[0]][pos[1]] = i
        if solve(grid):
            return solve(grid)
        else:
            grid[pos[0]][pos[1]] = '.'


def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    for i in range(len(solution)):
        for g in range(len(solution[i])):
            col = get_col(solution, (i, g))
            row = get_row(solution, (i, g))
            kv = get_block(solution, (i, g))
            setcol = set(col)
            setrow = set(row)
            setkv = set(kv)
            if not((len(col) == len(setcol)) & (len(row) == len(setrow)) & (len(kv) == len(setkv))):
                return False
    return True


def generate_sudoku(N):
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    grid = []
    for i in range(81):
        grid.append('.')
    grid = group(grid, 9)
    if N > 0:
        grid = solve(grid)
        if N > 81:
            return grid
        g = 0
        while g <= N:
            pos = (random.randint(0, 8), random.randint(0, 8))
            if not(grid[pos[0]][pos[1]] == '.'):
                grid[pos[0]][pos[1]] = '.'
                # for i in find_possible_values(grid, pos):
                #     grid[pos[0]][pos[1]] = i
                g += 1
    return grid



def run_solve(fname):

    start = time.time()
    grid = read_sudoku(fname)
    display(grid)
    print(fname + ' решается...')
    solution = solve(grid)
    print('Решение ' + fname)
    display(solution)
    end = time.time() - start
    print(fname + ': ' + str(end))
    print('=================================')

if __name__ == "__main__":
    for fname in ('puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt'):
       # t = threading.Thread(target=run_solve, args=(fname,))
       # t.start()
        run_solve(fname)

    print('Сгенерированный судоку')
    grid = generate_sudoku(40)
    display(grid)
    solution = solve(grid)
    print('Решение сгенерированного судоку:')
    display(solution)
    print('=================================')