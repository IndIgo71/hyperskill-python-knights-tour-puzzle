import copy
from chessfigure import ChessFigure


class Board:
    def __init__(self, col_cnt: int, row_cnt: int):
        self.__row_cnt = row_cnt
        self.__col_cnt = col_cnt
        self.__yaxiswidth = self.__digits(row_cnt)
        self.__xaxiswidth = self.__digits(row_cnt * col_cnt)
        self.__board = [['_' * self.__xaxiswidth for _ in range(col_cnt)] for _ in range(row_cnt)]
        self.__figure: ChessFigure = None
        self.__visited_cells = []

    @property
    def row_cnt(self):
        return self.__row_cnt

    @property
    def col_cnt(self):
        return self.__col_cnt

    @property
    def figure(self):
        return self.__figure

    @property
    def visited_cells(self):
        return self.__visited_cells

    @staticmethod
    def __digits(num):
        return len(str(num))

    def solved(self):
        return len(self.__visited_cells) == (self.col_cnt * self.row_cnt)

    def set_figure(self, figure):
        if self.__figure is None:
            self.__figure = figure
            self.__visited_cells.append(figure.pos)
            self.get_possible_steps()
            self.__set_figure_on_board()
        else:
            print('Board cannot have more 1 figure!')

    def __set_figure_on_board(self):
        self.__board[self.__figure.pos[0]][self.__figure.pos[1]] = 'X'.rjust(self.__xaxiswidth, ' ')

    def show(self, solution=None) -> None:
        tmp = copy.deepcopy(self.__board)
        if solution is not None:
            for i, cell in enumerate(solution, start=1):
                tmp[cell[0]][cell[1]] = str(i).rjust(self.__xaxiswidth, ' ')
        else:
            for key, val in self.__figure.possible_steps.items():
                tmp[key[0]][key[1]] = str(val).rjust(self.__xaxiswidth, ' ')

        separator = "-" * (self.col_cnt * (self.__xaxiswidth + 1) + 3)
        print(f'{" " * self.__yaxiswidth}{separator}')
        for i in range(self.row_cnt - 1, -1, -1):
            print(f'{str(i + 1).rjust(self.__yaxiswidth, " ")}| {" ".join(tmp[i])} |')
        print(f'{" " * self.__yaxiswidth}{separator}')
        print(
            f"{' ' * self.__yaxiswidth}  {' '.join(str(i + 1).rjust(self.__xaxiswidth, ' ') for i in range(self.col_cnt))}")

    @staticmethod
    def shift_pos(pos, step):
        return pos[0] + step[0], pos[1] + step[1]

    def is_pos_allowed(self, pos):
        return (0 <= pos[1] < self.col_cnt) and (0 <= pos[0] < self.row_cnt) and pos not in self.__visited_cells

    def count_allowed(self, pos, steps):
        return sum(list(map(lambda step: 1 if self.is_pos_allowed(self.shift_pos(pos, step)) else 0, steps)))

    def get_possible_steps(self):
        self.__figure.possible_steps.clear()
        for step in self.__figure.allowed_steps:
            pos = self.shift_pos(self.__figure.pos, step)
            if self.is_pos_allowed(pos):
                self.__figure.possible_steps[pos] = self.count_allowed(pos, self.__figure.allowed_steps)

    def move_figure(self, pos=None) -> None:
        self.__board[self.__figure.pos[0]][self.__figure.pos[1]] = '*'.rjust(self.__xaxiswidth, ' ')
        self.__figure.pos = pos
        self.__visited_cells.append(pos)
        self.get_possible_steps()
        self.__set_figure_on_board()
