from Constants import *
from Piece import *

class BoardCell:
    def __init__(self, c, x, y, piece=None):
        self.c = c
        self.x = x
        self.y = y
        self.piece = piece
        self.movable = False
        self.attackable = False
    
    def placePiece(self, piece):
        self.piece = piece
        self.piece.x = self.x
        self.piece.y = self.y
    
    def __repr__(self):
        return self.c
    
    def show(self):
        if self.c == "black":
            fill(165, 42, 42)
        else:
            fill(255)
        rect(self.x*CELLDIM+MARGIN, self.y*CELLDIM+MARGIN, CELLDIM, CELLDIM)
        if self.piece != None:
            self.piece.show()
    
    def getPieceType(self):
        if self.piece == None:
            return None
        return self.piece.piece