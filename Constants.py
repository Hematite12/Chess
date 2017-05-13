MARGIN = 50
CELLDIM = 60
CANVASSIZE = CELLDIM*8+2*MARGIN

BLACK = (165, 42, 42)
BLACKATTACKABLE = (220, 30, 30)
BLACKMOVABLE = (130, 40, 100)
BLACKSELECTED = (30, 220, 30)

WHITE = (255, 255, 255)
WHITEATTACKABLE = (255, 140, 140)
WHITEMOVABLE = (180, 180, 255)
WHITESELECTED = (180, 255, 180)

BOARD = [["BR","BN","BB","BQ","BK","BB","BN","BR"],
         ["BP","BP","BP","BP","BP","BP","BP","BP"],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         ["WP","WP","WP","WP","WP","WP","WP","WP"],
         ["WR","WN","WB","WQ","WK","WB","WN","WR"]]

x = None
A = "attack"
M = "move"
J = "jump"
S = "start"
C = "castle"

WHITEPAWNSTART = [[x,M,x],
                  [A,M,A],
                  [x,S,x],
                  [x,x,x],
                  [x,x,x]]

WHITEPAWN = [[A,M,A],
             [x,S,x],
             [x,x,x]]

BLACKPAWNSTART = [[x,x,x],
                  [x,x,x],
                  [x,S,x],
                  [A,M,A],
                  [x,M,x]]

BLACKPAWN = [[x,x,x],
             [x,S,x],
             [A,M,A]]

KNIGHT = [[x,J,x,J,x],
          [J,x,x,x,J],
          [x,x,S,x,x],
          [J,x,x,x,J],
          [x,J,x,J,x]]

BISHOP = [[A,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,A],
          [x,A,x,x,x,x,x,x,x,x,x,x,x,x,x,A,x],
          [x,x,A,x,x,x,x,x,x,x,x,x,x,x,A,x,x],
          [x,x,x,A,x,x,x,x,x,x,x,x,x,A,x,x,x],
          [x,x,x,x,A,x,x,x,x,x,x,x,A,x,x,x,x],
          [x,x,x,x,x,A,x,x,x,x,x,A,x,x,x,x,x],
          [x,x,x,x,x,x,A,x,x,x,A,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,A,x,A,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,S,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,A,x,A,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,A,x,x,x,A,x,x,x,x,x,x],
          [x,x,x,x,x,A,x,x,x,x,x,A,x,x,x,x,x],
          [x,x,x,x,A,x,x,x,x,x,x,x,A,x,x,x,x],
          [x,x,x,A,x,x,x,x,x,x,x,x,x,A,x,x,x],
          [x,x,A,x,x,x,x,x,x,x,x,x,x,x,A,x,x],
          [x,A,x,x,x,x,x,x,x,x,x,x,x,x,x,A,x],
          [A,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,A]]

ROOK = [[x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [A,A,A,A,A,A,A,A,S,A,A,A,A,A,A,A,A],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,x]]

QUEEN =  [[A,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,A],
          [x,A,x,x,x,x,x,x,A,x,x,x,x,x,x,A,x],
          [x,x,A,x,x,x,x,x,A,x,x,x,x,x,A,x,x],
          [x,x,x,A,x,x,x,x,A,x,x,x,x,A,x,x,x],
          [x,x,x,x,A,x,x,x,A,x,x,x,A,x,x,x,x],
          [x,x,x,x,x,A,x,x,A,x,x,A,x,x,x,x,x],
          [x,x,x,x,x,x,A,x,A,x,A,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,A,A,A,x,x,x,x,x,x,x],
          [A,A,A,A,A,A,A,A,S,A,A,A,A,A,A,A,A],
          [x,x,x,x,x,x,x,A,A,A,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,A,x,A,x,A,x,x,x,x,x,x],
          [x,x,x,x,x,A,x,x,A,x,x,A,x,x,x,x,x],
          [x,x,x,x,A,x,x,x,A,x,x,x,A,x,x,x,x],
          [x,x,x,A,x,x,x,x,A,x,x,x,x,A,x,x,x],
          [x,x,A,x,x,x,x,x,A,x,x,x,x,x,A,x,x],
          [x,A,x,x,x,x,x,x,A,x,x,x,x,x,x,A,x],
          [A,x,x,x,x,x,x,x,A,x,x,x,x,x,x,x,A]]

KING = [[A,A,A],
        [A,S,A],
        [A,A,A]]

KINGCASTLEKING = [[x, A, A, A, x],
                  [x, A, S, A, C],
                  [x, A, A, A, x]]

KINGCASTLEQUEEN = [[x, A, A, A, x],
                   [C, A, S, A, x],
                   [x, A, A, A, x]]