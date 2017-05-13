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
        self.visited = False
        self.selected = False
    
    def placePiece(self, piece):
        self.piece = piece
        self.piece.x = self.x
        self.piece.y = self.y
    
    def unmark(self):
        self.movable = False
        self.attackable = False
    
    def __repr__(self):
        return self.c
    
    def show(self):
        if self.c == "black":
            if self.attackable:
                fill(*BLACKATTACKABLE)
            elif self.movable:
                fill(*BLACKMOVABLE)
            else:
                fill(*BLACK)
        else:
            if self.attackable:
                fill(*WHITEATTACKABLE)
            elif self.movable:
                fill(*WHITEMOVABLE)
            else:
                fill(*WHITE)
        rect(self.y*CELLDIM+MARGIN, self.x*CELLDIM+MARGIN, CELLDIM, CELLDIM)
        if self.piece != None and not self.piece.selected:
            self.piece.show()
    
    def getPieceType(self):
        if self.piece == None:
            return None
        return self.piece.piece