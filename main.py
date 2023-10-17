from board import Board
import time
board = Board(10,10)
# for x in range(board.height):
#      board.place_cell(x,1)
board.place_cell(2,3)
board.place_cell(2,4)
board.place_cell(2,5)
board.place_cell(1,5)
board.place_cell(0,4)
print(board.as_str())
print(board.get_alive_neighbours(1,2))
board.next_shape()
print(board.as_str())
while True:
    time.sleep(1)
    board.next_shape()
    print(board.as_str())