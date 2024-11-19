from board import Board

class ChessFigure:
    '''
    Class that represents chess figure
    '''
    def __init__(self, board, x, y, symbol):
        pass
    
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
        pass
    
    def position_in_bounds(self, x, y):
        '''
        Checks if position is in bounds
        
        Arguments
        ---------
        x : int
            column number position on board (start from 1)
        y : int
            raw number position on board (start from 1)
            
        Returns:
            bool : True if position in bounds false if not

        '''
        pass


    def make_move(self, x, y):
        '''
        Arguments
        ---------
        x : int
            column number position on board (start from 1)
        y : int
            raw number position on board (start from 1)

        Throws "Eception: Position x, y is already ocupied by symbol" exception if position is in not bounds
        Throws "Exception: Position x, y is not on the board" if position is not on the board
        Moves the piece to the specified position on board

        '''
        pass