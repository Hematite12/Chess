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
            self.SELECTED = piece
            if piece != None:
                piece.select()
                self.markMoves(ySquare, xSquare, piece)
    
    def checkDeselect(self, x, y):
        self.SELECTED.deselect()
        if x>MARGIN and x<CANVASSIZE-MARGIN and y>MARGIN and y<CANVASSIZE-MARGIN:
            ySquare = (x-MARGIN) // CELLDIM
            xSquare = (y-MARGIN) // CELLDIM
            cell = self.matrix[xSquare][ySquare]
            if cell.attackable or cell.movable:
                cell.placePiece(self.SELECTED)
                self.SELECTED.moved = True
                self.matrix[self.SELECTED.origPos[0]][self.SELECTED.origPos[1]].piece = None
        self.SELECTED = None
        self.unmarkAll()
    
    def unmarkAll(self):
        for x in range(8):
            for y in range(8):
                self.matrix[x][y].unmark()
    
    def setPawnMovable(self, x, y):
        square = self.matrix[y][x]
        if square.piece == None:
            square.movable = True
    
    def setPawnAttackable(self, x, y, friendly):
        if x>=0 and x<8 and y>=0 and y<8:
            square = self.matrix[y][x]
            if square.piece != None and square.piece.c != friendly:
                square.attackable = True
    
    def setAttackMove(self, x, y, friendly):
        square = self.matrix[y][x]
        if square.piece == None:
            square.movable = True
        else:
            if square.piece.c != friendly:
                square.attackable = True
    
    def applyMovesMat(self, x, y, mat, friendly):
        xDist = len(mat[0]) // 2
        yDist = len(mat) // 2
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                xSquare = x+i-xDist
                ySquare = y+j-yDist
                if xSquare>=0 and xSquare<8 and ySquare>=0 and ySquare<8:
                    if mat[j][i] == "attack":
                        self.setAttackMove(x+i-xDist, y+j-yDist, friendly)
    
    def applyKnightJump(self, x, y, mat, friendly):
        xDist = len(mat[0]) // 2
        yDist = len(mat) // 2
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                xSquare = x+i-xDist
                ySquare = y+j-yDist
                if xSquare>=0 and xSquare<8 and ySquare>=0 and ySquare<8:
                    if mat[j][i] == "jump":
                        self.setAttackMove(x+i-xDist, y+j-yDist, friendly)
    def unvisitAll(self):
        for x in range(8):
            for y in range(8):
                self.matrix[x][y].visited = False
    
    def checkCellSight(self, x, y):
        cell = self.matrix[x][y]
        cell.visited = True
        dirX = self.SELECTED.origPos[0] - x
        dirY = self.SELECTED.origPos[1] - y
        if dirX == 0 and dirY == 0:
            return True
        if dirX > 0:
            newX = x + 1
        elif dirX == 0:
            newX = x
        elif dirX < 0:
            newX = x - 1
        if dirY > 0:
            newY = y + 1
        elif dirY == 0:
            newY = y
        elif dirY < 0:
            newY = y - 1
        check = self.checkCellSight(newX, newY)
        if not check:
            cell.movable = False
            cell.attackable = False
            return False
        elif cell.piece != None:
            return False
        else:
            return True
    
    def lineOfSight(self):
        for x in range(8):
            for y in range(8):
                if not self.matrix[x][y].visited:
                    self.checkCellSight(x, y)
        self.unvisitAll()
    
    def markMoves(self, x, y, piece):
        if piece.piece == "pawn":
            if piece.c == "white":
                if y == 6:
                    self.setPawnMovable(x, 4)
                self.setPawnMovable(x, y-1)
                self.setPawnAttackable(x-1, y-1, "white")
                self.setPawnAttackable(x+1, y-1, "white")
            elif piece.c == "black":
                if y == 1:
                    self.setPawnMovable(x, 3)
                self.setPawnMovable(x, y+1)
                self.setPawnAttackable(x+1, y+1, "black")
                self.setPawnAttackable(x-1, y+1, "black")
        
        elif piece.piece == "bishop":
            self.applyMovesMat(x, y, BISHOP, piece.c)
        elif piece.piece == "queen":
            self.applyMovesMat(x, y, QUEEN, piece.c)
        elif piece.piece == "rook":
            self.applyMovesMat(x, y, ROOK, piece.c)
        elif piece.piece == "knight":
            self.applyKnightJump(x, y, KNIGHT, piece.c)
        elif piece.piece == "king":
            self.applyMovesMat(x, y, KING, piece.c)
        if piece.piece != "knight":
            self.lineOfSight()
    
    

    
    
    
    
    
    
    
    
    
    
    