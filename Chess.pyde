from Constants import *
from Board import *

# Pic dimensions = 60 x 60 

def setup():
    global b, BB, BW, KB, KW, NB, NW, PB, PW, QB, QW, RB, RW
    BB = loadImage("BishopBlack.png")
    BW = loadImage("BishopWhite.png")
    KB = loadImage("KingBlack.png")
    KW = loadImage("KingWhite.png")
    NB = loadImage("KnightBlack.png")
    NW = loadImage("KnightWhite.png")
    PB = loadImage("PawnBlack.png")
    PW = loadImage("PawnWhite.png")
    QB = loadImage("QueenBlack.png")
    QW = loadImage("QueenWhite.png")
    RB = loadImage("RookBlack.png")
    RW = loadImage("RookWhite.png")
    imgs = (BB, BW, KB, KW, NB, NW, PB, PW, QB, QW, RB, RW)
    size(CANVASSIZE, CANVASSIZE)
    background(100)
    b = Board(imgs)

def draw():
    b.show()

def mousePressed():
    b.checkMouse(mouseX, mouseY)