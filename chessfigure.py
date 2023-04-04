class ChessFigure:
    def __init__(self, pos: tuple[int, int]):
        self.pos = pos
        self._allowed_steps = tuple()
        self.possible_steps = dict()

    @property
    def allowed_steps(self):
        return self._allowed_steps
