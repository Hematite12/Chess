from BoardCell import *
from Constants import *
from Piece import *

class Board:
    def __init__(self, imgs):
        self.imgs = imgs
        self.matrix = [[None for x in range(8)] for y in range(8)]
        for i in range(64):
            row = i // 8
            col = i % 8
            if (i+row)%2==0:
                self.matrix[row][col] = BoardCell("white", col, row)
            else:
                self.matrix[row][col] = BoardCell("black", col, row)
        self.pieces = []
        self.placePieces()
    
    def placePieces(self):
        for i in range(0, 8, 7):
            p = Piece("black", "rook", i, 0, self.imgs)
            self.pieces.append(p)
            self.matrix[0][i].placePiece(p)
        for i in range(1, 8, 5):
            p = Piece("black", "knight", i, 0, self.imgs)
            self.pieces.append(p)
            self.matrix[0][i].placePiece(p)
        for i in range(2, 8, 3):
            p = Piece("black", "bishop", i, 0, self.imgs)
            self.pieces.append(p)
            self.matrix[0][i].placePiece(p)
        p = Piece("black", "queen", 3, 0, self.imgs)
        self.pieces.append(p)
        self.matrix[0][3].placePiece(p)
        p = Piece("black", "king", 4, 0, self.imgs)
        self.pieces.append(p)
        self.matrix[0][4].placePiece(p)
        for i in range(8):
            p = Piece("black", "pawn", i, 1, self.imgs)
            self.pieces.append(p)
            self.matrix[1][i].placePiece(p)
        for i in range(8):
            p = Piece("white", "pawn", i, 6, self.imgs)
            self.pieces.append(p)
            self.matrix[6][i].placePiece(p)
        for i in range(0, 8, 7):
            p = Piece("white", "rook", i, 7, self.imgs)
            self.pieces.append(p)
            self.matrix[7][i].placePiece(p)
        for i in range(1, 8, 5):
            p = Piece("white", "knight", i, 7, self.imgs)
            self.pieces.append(p)
            self.matrix[7][i].placePiece(p)
        for i in range(2, 8, 3):
            p = Piece("white", "bishop", i, 7, self.imgs)
            self.pieces.append(p)
            self.matrix[7][i].placePiece(p)
        p = Piece("white", "queen", 3, 7, self.imgs)
        self.pieces.append(7)
        self.matrix[7][3].placePiece(p)
        p = Piece("white", "king", 4, 7, self.imgs)
        self.pieces.append(p)
        self.matrix[7][4].placePiece(p)
    
    def show(self):
        for i in range(8):
            for j in range(8):
                self.matrix[i][j].show()
    
    def checkMouse(self, x, y):
        if x>MARGIN and x<CANVASSIZE-MARGIN and y>MARGIN and y<CANVASSIZE-MARGIN:
            xSquare = x // CELLDIM
            ySquare = y // CELLDIM
            piece = self.matrix[x][y].getPieceType()
            if piece != None:
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    