from BoardCell import *
from Constants import *
from Piece import *

class Board:
    def __init__(self, imgs):
        self.playing = "white"
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
    
    def changePlayer(self):
        if self.playing == "white":
            self.playing = "black"
        else:
            self.playing = "white"
    
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
            if piece != None and piece.c == self.playing:
                self.matrix[xSquare][ySquare].selected = True
                self.SELECTED = piece
                piece.select()
                self.markMoves(ySquare, xSquare, piece)
    
    def checkDeselect(self, x, y):
        self.SELECTED.deselect()
        if x>MARGIN and x<CANVASSIZE-MARGIN and y>MARGIN and y<CANVASSIZE-MARGIN:
            ySquare = (x-MARGIN) // CELLDIM
            xSquare = (y-MARGIN) // CELLDIM
            cell = self.matrix[xSquare][ySquare]
            if cell.attackable or cell.movable or cell.castlable:
                cell.placePiece(self.SELECTED)
                self.SELECTED.moved = True
                self.matrix[self.SELECTED.origPos[0]][self.SELECTED.origPos[1]].piece = None
                self.changePlayer()
                if cell.castlable:
                    if cell.y == 6:
                        if cell.x == 7:
                            self.matrix[7][5].placePiece(self.matrix[7][7].piece)
                            self.matrix[7][7].piece.moved = True
                            self.matrix[7][7].piece = None
                        else:
                            self.matrix[0][5].placePiece(self.matrix[0][7].piece)
                            self.matrix[0][7].piece.moved = True
                            self.matrix[0][7].piece = None
                    else:
                        if cell.x == 7:
                            self.matrix[7][3].placePiece(self.matrix[7][0].piece)
                            self.matrix[7][0].piece.moved = True
                            self.matrix[7][0].piece = None
                        else:
                            self.matrix[0][3].placePiece(self.matrix[0][0].piece)
                            self.matrix[0][0].piece.moved = True
                            self.matrix[0][0].piece = None
                if cell.pawnDouble:
                    cell.enpassantable = 2
                if self.SELECTED.piece == "pawn" and cell.enpassantAttackable:
                    if cell.x == 2:
                        self.matrix[cell.x+1][cell.y].piece = None
                    elif cell.x == 5:
                        self.matrix[cell.x-1][cell.y].piece = None
        self.SELECTED = None
        self.unmarkAll()
    
    def unmarkAll(self):
        for x in range(8):
            for y in range(8):
                self.matrix[x][y].unmark()
    
    def setMove(self, x, y):
        square = self.matrix[y][x]
        if square.piece == None:
            square.movable = True
    
    def setPawnDouble(self, x, y):
        square = self.matrix[y][x]
        if square.piece == None:
            square.movable = True
            square.pawnDouble = True
    
    def setCastle(self, x, y):
        square = self.matrix[y][x]
        square.castlable = True
    
    def setAttack(self, x, y, friendly):
        if x>=0 and x<8 and y>=0 and y<8:
            square = self.matrix[y][x]
            if square.piece != None and square.piece.c != friendly:
                square.attackable = True
    
    def setEnpassant(self, x, y, friendly):
        square = self.matrix[y][x]
        square.attackable = True
        square.enpassantAttackable = True
    
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
                        self.setAttackMove(xSquare, ySquare, friendly)
                    if mat[j][i] == "castle":
                        self.setCastle(xSquare, ySquare)
    
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
                    self.setPawnDouble(x, 4)
                self.setMove(x, y-1)
                self.setAttack(x-1, y-1, "white")
                self.setAttack(x+1, y-1, "white")
                if y == 3:
                    if self.matrix[y][x+1].enpassantable == 1:
                        self.setEnpassant(x+1, 2, "white")
                    if self.matrix[y][x-1].enpassantable == 1:
                        self.setEnpassant(x-1, 2, "white")
                
            elif piece.c == "black":
                if y == 1:
                    self.setPawnDouble(x, 3)
                self.setMove(x, y+1)
                self.setAttack(x+1, y+1, "black")
                self.setAttack(x-1, y+1, "black")
                if y == 4:
                    if self.matrix[y][x+1].enpassantable == 1:
                        self.setEnpassant(x+1, 5, "white")
                    if self.matrix[y][x-1].enpassantable == 1:
                        self.setEnpassant(x-1, 5, "white")
                
        elif piece.piece == "bishop":
            self.applyMovesMat(x, y, BISHOP, piece.c)
        elif piece.piece == "queen":
            self.applyMovesMat(x, y, QUEEN, piece.c)
        elif piece.piece == "rook":
            self.applyMovesMat(x, y, ROOK, piece.c)
        elif piece.piece == "knight":
            self.applyKnightJump(x, y, KNIGHT, piece.c)
        elif piece.piece == "king":
            mat = KING
            kingside = False
            queenside = False
            if piece.c=="white":
                col = 7
            else:
                col = 0
            if not piece.moved:
                if self.matrix[col][5].piece==None and self.matrix[col][6].piece==None:
                    if self.matrix[col][7].piece!=None and not self.matrix[col][7].piece.moved:
                        kingside = True
                if self.matrix[col][3].piece==None and self.matrix[col][2].piece==None:
                    if self.matrix[col][0].piece!=None and not self.matrix[col][0].piece.moved:
                        queenside = True
            if kingside and queenside:
                mat = KINGCASTLEBOTH
            elif kingside:
                mat = KINGCASTLEKING
            elif queenside:
                mat = KINGCASTLEQUEEN
            self.applyMovesMat(x, y, mat, piece.c)
        if piece.piece != "knight":
            self.lineOfSight()
    
    
    
    
    
    
    
    
    
    
    
    
    