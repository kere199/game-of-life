from board import Board
import time
board = Board(3,3)
for x in range(board.height):
     board.place_cell(x,1)
print(board.as_str())
print(board.get_alive_neighbours(1,2))
board.next_shape()
print(board.as_str())
while True:
    time.sleep(1)
    board.next_shape()
    print(board.as_str())
     