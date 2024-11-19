from board import Board
from pawn import Pawn

my_board=Board()

my_Pawns=[Pawn(my_board,1,2), Pawn(my_board,2,2), Pawn(my_board,3,2), Pawn(my_board,4,2)]
black_pawn = Pawn(my_board,2,7)

my_board.print()

for n in range(2,8):
  my_Pawns[1].step(Pawn.FRONT)
  my_board.print()