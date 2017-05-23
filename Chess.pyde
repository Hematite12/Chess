add_library('minim')
minim = Minim(this)
from Constants import *
from Board import *

# Pic dimensions = 60 x 60

THREAD = "OFF"
# "CHESS", "DXD"
STYLE = "DXD"

def setup():
    size(CANVASSIZE, CANVASSIZE)
    global b, BB, BW, KB, KW, NB, NW, PB, PW, QB, QW, RB, RW, audio
    if STYLE == "CHESS":
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
    elif STYLE == "DXD":
        BB = loadImage("AsiaBlack.png")
        BW = loadImage("AsiaWhite.png")
        KB = loadImage("GremoryBlack.png")
        KW = loadImage("GremoryWhite.png")
        NB = loadImage("KibaBlack.png")
        NW = loadImage("KibaWhite.png")
        PB = loadImage("IsseiBlack.png")
        PW = loadImage("IsseiWhite.png")
        QB = loadImage("AkenoBlack.png")
        QW = loadImage("AkenoWhite.png")
        RB = loadImage("KonekoBlack.png")
        RW = loadImage("KonekoWhite.png")
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
        b.checkSelect(mouseX, mouseY)
    else:
        b.checkDeselect(mouseX, mouseY)
        if STYLE == "DXD":
            audio = minim.loadFile("Seinfeld.mp3")
            audio.play()