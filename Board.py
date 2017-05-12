from BoardCell import *
from Constants import *
from Piece import *

class Board:
    def __init__(self, imgs):
        self.imgs = imgs
        self.SELECTED = None
        self.matrix = [[None for x in range(8)] for y in range(8)]
        for i in range(64):
            x = i % 8
            y = i // 8
            if (i+y)%2==0:
                self.matrix[x][y] = BoardCell("white", x, y)
            else:
                self.matrix[x][y] = BoardCell("black", x, y)
        self.pieces = []
        self.placePieces()
    
    def placePieces(self):
        for y in range(len(BOARD)):
            for x in range(len(BOARD)):
                if BOARD[x][y]!=None:
                    if BOARD[x][y]=="BR":
                        p = Piece("black", "rook", x, y, self.imgs)
                    elif BOARD[x][y]=="BN":
                        p = Piece("black", "knight", x, y, self.imgs)
                    elif BOARD[x][y]=="BB":
                        p = Piece("black", "bishop", x, y, self.imgs)
                    elif BOARD[x][y]=="BQ":
                        p = Piece("black", "queen", x, y, self.imgs)
                    elif BOARD[x][y]=="BK":
                        p = Piece("black", "king", x, y, self.imgs)
                    elif BOARD[x][y]=="BP":
                        p = Piece("black", "pawn", x, y, self.imgs)
                    elif BOARD[x][y]=="WP":
                        p = Piece("white", "pawn", x, y, self.imgs)
                    elif BOARD[x][y]=="WR":
                        p = Piece("white", "rook", x, y, self.imgs)
                    elif BOARD[x][y]=="WN":
                        p = Piece("white", "knight", x, y, self.imgs)
                    elif BOARD[x][y]=="WB":
                        p = Piece("white", "bishop", x, y, self.imgs)
                    elif BOARD[x][y]=="WQ":
                        p = Piece("white", "queen", x, y, self.imgs)
                    elif BOARD[x][y]=="WK":
                        p = Piece("white", "king", x, y, self.imgs)
                    self.pieces.append(p)
                    self.matrix[x][y].placePiece(p)
    
    def show(self):
        for x in range(8):
            for y in range(8):
                self.matrix[x][y].show()
    
    def checkSelect(self, x, y):
        if x>MARGIN and x<CANVASSIZE-MARGIN and y>MARGIN and y<CANVASSIZE-MARGIN:
            ySquare = (x-MARGIN) // CELLDIM
            xSquare = (y-MARGIN) // CELLDIM
            piece = self.matrix[xSquare][ySquare].piece
            if piece != None:
                piece.select()
            return piece
    
    def checkDeselect(self, x, y):
        self.SELECTED.deselect()
        self.SELECTED = None
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    