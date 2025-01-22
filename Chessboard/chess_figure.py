from board import Board

class ChessFigure:
    '''
    Class that represents chess figure
    '''
    def __init__(self, board, x, y, symbol):
        self.board = board
        self.x = x
        self.y = y
        self.symbol = symbol
        board.set(self.x, self.y, self.symbol)
    
    def position_free(self, x,y):
        '''
        Checks if position is ocupied or free
        
        Arguments
        ---------
        x : int
            column number position on board (start from 1)
        y : int
            raw number position on board (start from 1)
            
        Returns:
            bool : True if position is free, False if position is occupied

        '''
        return self.board.get( x, y) == Board.EMPTY_FIELD
    
    def position_in_bounds(self, x, y):
        return (1 <= x <= 8) and (1 <= y <= 8)


    def make_move(self, x, y):
        if not self.position_in_bounds(x, y):
            raise Exception(f"Position {x}, {y} is not on the board")
        if not self.position_free(x, y):
            raise Exception(f"Position {x}, {y} is already ocupied by {self.board.get(x, y)}")
        self.board.set(self.x, self.y, Board.EMPTY_FIELD)
        self.x = x
        self.y = y
        self.board.set(self.x, self.y, self.symbol)
