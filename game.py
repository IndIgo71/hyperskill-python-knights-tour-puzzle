from knight import Knight
from board import Board
from solver import Solver


class Game:
    @staticmethod
    def get_board_dimension():
        while True:
            dimensions = input('Enter your board dimensions: ').split()
            if len(dimensions) != 2 or not all(map(lambda d: d.isdigit() and int(d) > 0, dimensions)):
                print('Invalid dimensions!')
                continue
            return list((map(int, dimensions)))

    @staticmethod
    def get_start_coordinates(rows, cols):
        while True:
            try:
                coordinates = list(map(lambda c: int(c) - 1, input("Enter the knight' starting position: ").split()))[
                              ::-1]
                if len(coordinates) != 2 or coordinates[0] < 0 or coordinates[0] > cols \
                        or coordinates[1] < 0 or coordinates[1] > rows:
                    print('Invalid dimensions!')
                    continue
                return tuple(coordinates)
            except ValueError:
                print('Invalid dimensions!')

    def start(self):
        board = Board(*self.get_board_dimension())
        knight = Knight(self.get_start_coordinates(board.row_cnt, board.col_cnt))
        board.set_figure(knight)
        while True:
            answer = input('Do you want to try the puzzle? (y/n): ').lower()
            if answer in 'ny':
                break
            else:
                print('Invalid input!')

        solver = Solver()
        solver.solve(board)

        if answer == 'y':
            if not solver.status.solved:
                print('No solution exists!')
            else:
                board.show()
                print()
                while True:
                    if board.solved():
                        print('What a great tour! Congratulations!')
                        break

                    if len(board.figure.possible_steps) == 0:
                        print('No more possible moves!')
                        print(f'Your knight visited {len(board.visited_cells)} squares!')
                        break

                    pos = tuple(map(lambda c: int(c) - 1, input('Enter your next move: ').split()[::-1]))
                    if pos not in knight.possible_steps:
                        print('Invalid move!', end=' ')
                        continue

                    board.move_figure(pos)
                    board.show()
                    print()
        else:
            if not solver.status.solved:
                print('No solution exists!')
            else:
                print("\nHere's the solution!")
                board.show(solver.status.sequence)


if __name__ == '__main__':
    game = Game()
    game.start()
