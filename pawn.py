from chess_figure import ChessFigure

class Pawn(ChessFigure):
    FRONT = 1
    DOUBLE_FRONT = 2
    # SYMBOL = "♙"
    SYMBOL = "p"

    def __init__(self, board, x, y):
        super().__init__(board,x,y, self.SYMBOL)

    def __get_moved_pos(self, move_type):
        if move_type == Pawn.FRONT:
            return (self.x, self.y+1)
        if move_type == Pawn.DOUBLE_FRONT:
            return (self.x, self.y+2)

    def step(self, move_type):
        x, y = self.__get_moved_pos(move_type)
        self.make_move(x, y)