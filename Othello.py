# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

class Board:
    """A board class for Othello"""
    black_player = {'name' : 'Joel',
                    'color' : 'Black',
                    'symbol' : 'B'}
    white_player = {'name' : 'Bonzo',
                   'color' : 'White',
                   'symbol' : 'W'}
    black_player['opposite_player'] = white_player
    white_player['opposite_player'] = black_player

    nobody = {'name' : '',
              'color' : '',
              'symbol' : '_'}
    
    def __init__(self):
        self.board = [[self.nobody for col in range(8)] for row in range(8)]
        self.board[3][3] = self.board[4][4] = self.white_player
        self.board[3][4] = self.board[4][3] = self.black_player
    
        self.active_player = self.black_player
    
    def legalMove(self, x, y, current_player ) :
        """returns boolean for whether current player taking spot (x,y) is legal"""
        if x < 0 or x >= 8 : return False
        if y < 0 or y >= 8 : return False
        if self.board[x][y] != self.nobody : return False
        
        for dirX in range(-1,2):
            for dirY in range(-1,2):
                if dirX == 0 and dirY == 0: continue
                if dirX + x < 0 or dirX + x >=8 : continue
                if dirY + y < 0 or dirY + y >=8 : continue
                if self.legalMoveDir(x, y, dirX, dirY, current_player) :
                    return True
        return False
    
    def legalMoveDir(self, x, y, dirX, dirY, current_player) :
        """checks the (dirX, dirY) direction to see if (x,y) was legal"""
        x += dirX
        y += dirY
        
        if x < 0 or x >=8 : return False
        if y < 0 or y >=8 : return False
        if self.board[x][y] != current_player['opposite_player'] : return False
        
        while True :
            x += dirX
            y += dirY
            if x < 0 or x >=8 : return False
            if y < 0 or y >=8 : return False
            if self.board[x][y] == current_player['opposite_player'] : continue
            if self.board[x][y] == current_player : return True
            if self.board[x][y] == self.nobody : return False
 
    def hasLegalMove(self, current_player) :
        for x in range(8):
            for y in range(8):
                if self.legalMove(x,y, current_player) : return True
        return False
    
    def makeMove(self, x, y, current_player = None) :
        """have the active player make move at (x,y)"""
        if current_player == None : current_player = self.active_player
            
        if not self.legalMove(x,y,current_player) : 
            print 'False by current player'
            print current_player['color']
            return False
        self.board[x][y] = current_player
        
        for dirX in range(-1,2):
            for dirY in range(-1,2):
                if dirX == 0 and dirY == 0 : continue
                if self.legalMoveDir(x,y,dirX, dirY, current_player) :
                    self.makeMoveDir(x,y,dirX,dirY, current_player)
        #self.active_player = current_player['opposite_player']
    
    def makeMoveDir(self, x, y, dirX, dirY, current_player) :
        while True: 
            x += dirX
            y += dirY
            if self.board[x][y] == current_player : return
            if self.board[x][y] == self.nobody :
                print 'Tried to move to NOBODY'
                return False
            self.board[x][y] = current_player
    
    def printBoard(self) :
        print ' 0|1|2|3|4|5|6|7'
        for i in range(8):
            line = str(i)
            for j in range(8) :
                line += self.board[i][j].get('symbol') + '|'
            print line[:-1]
    

# <codecell>

class Game:
    game_board = Board()
        
    def __init__(self):
        self.game_board = Board()
    
    def playGame(self):
        while True:
            print 'Turn: {}'.format(self.game_board.active_player['color'])
            self.game_board.printBoard()
            
            #replace with call to actual player
            move = raw_input("Enter your move (eg '3 2'): ").split()
            if move == ['exit'] : break
            x = int(move[0])
            y = int(move[1])
            
            if self.game_board.legalMove(x,y,self.game_board.active_player) :
                self.game_board.makeMove(x,y)
            else : print 'Illegal move chosen'
            
            self.game_board.active_player = self.game_board.active_player['opposite_player']
            

# <codecell>
