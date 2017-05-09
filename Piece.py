from Constants import *

class Piece:
    def __init__(self, c, piece, x, y, imgs):
        self.moved = False
        self.x = x
        self.y = y
        self.c = c
        self.piece = piece
        self.BB = imgs[0]
        self.BW = imgs[1]
        self.KB = imgs[2]
        self.KW = imgs[3]
        self.NB = imgs[4]
        self.NW = imgs[5]
        self.PB = imgs[6]
        self.PW = imgs[7]
        self.QB = imgs[8]
        self.QW = imgs[9]
        self.RB = imgs[10]
        self.RW = imgs[11]
    
    def showImage(self, img):
        image(img, self.x*CELLDIM+MARGIN, self.y*CELLDIM+MARGIN)
    
    def show(self):
        if self.c == "white":
            if self.piece == "bishop":
                self.showImage(self.BW)
            elif self.piece == "king":
                self.showImage(self.KW)
            elif self.piece == "knight":
                self.showImage(self.NW)
            elif self.piece == "pawn":
                self.showImage(self.PW)
            elif self.piece == "queen":
                self.showImage(self.QW)
            else:
                self.showImage(self.RW)
        else:
            if self.piece == "bishop":
                self.showImage(self.BB)
            elif self.piece == "king":
                self.showImage(self.KB)
            elif self.piece == "knight":
                self.showImage(self.NB)
            elif self.piece == "pawn":
                self.showImage(self.PB)
            elif self.piece == "queen":
                self.showImage(self.QB)
            else:
                self.showImage(self.RB)