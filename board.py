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