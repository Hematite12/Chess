from Constants import *
from Board import *

# Pic dimensions = 60 x 60

THREAD = "OFF"

def setup():
    size(CANVASSIZE, CANVASSIZE)
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
    background(100)
    b = Board(imgs)
    b.show()

def draw():
    background(100)
    b.show()
    if b.SELECTED != None:
        b.SELECTED.setPos(mouseX, mouseY)
        b.SELECTED.show()

def mousePressed():
    if b.SELECTED == None:
        piece = b.checkSelect(mouseX, mouseY)
        b.SELECTED = piece
    else:
        b.checkDeselect(mouseX, mouseY)