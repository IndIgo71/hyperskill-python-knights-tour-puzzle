from chessfigure import ChessFigure


class Knight(ChessFigure):
    def __init__(self, pos: tuple[int, int]):
        super().__init__(pos)
        self._allowed_steps = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1))
