class Board():
    def __init__(self,width,height):
        self.height = height
        self.width = width
        self.board = [[False]*width for x in range(height)] 


    def as_str(self):
        rv = ""
        for row in self.board:
            rv +="".join([".0" [c] for c in row])
            rv += "\n"
        return rv
    
    def place_cell(self,row,col):
        self.board[row][col] = True

    def get_cell(self,row,col):
        if 0 <= row < self.height and 0<=col<self.width:
            return self.board[row][col]
        return False 

    def get_alive_neighbours(self,row, col):
        accumulator = 0
        for r in (-1,0,1):
            for c in (-1,0,1):
                if r == c and r == 0 :
                    continue
                if self.get_cell(row+r ,col+c):
                    accumulator +=1
        return accumulator
    


    def next_shape(self):
        new_board = [[False] * self.width for _ in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                alive_neighbors = self.get_alive_neighbours(row, col)
                if self.board[row][col]:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_board[row][col] = False
                    else:
                        new_board[row][col] = True
                else:
                    if alive_neighbors == 3:
                        new_board[row][col] = True
        self.board = new_board

        
