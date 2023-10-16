from board import Board
board = Board(3,3)
for x in range(3):
     board.place_cell(x,1)
print(board.as_str())

