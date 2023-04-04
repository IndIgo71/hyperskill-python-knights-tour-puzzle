import copy
from dataclasses import dataclass

from board import Board


@dataclass
class Status:
    solved = False
    sequence = list()


class Solver:
    def __init__(self):
        self.status = Status()

    def solve(self, board: Board) -> list | None:
        self.visit_node(board, self.status)
        return self.status.sequence if self.status.solved else None

    def visit_node(self, board: Board, status: Status):
        status.sequence.append(board.figure.pos)

        if board.solved():
            status.solved = True
            return

        steps = [k for k in sorted(board.figure.possible_steps, key=board.figure.possible_steps.get, reverse=True)]

        while steps:
            _board = copy.deepcopy(board)
            _board.move_figure(steps.pop())
            self.visit_node(_board, status)
            if status.solved:
                return
        else:
            status.sequence.pop()