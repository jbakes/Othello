# Othello Tests

b = Board()
print 'active player = {}'.format(b.active_player['name'])
b.legalMove(3,2, b.black_player )

# <codecell>

b.printBoard()

# <codecell>

b.makeMove(3,2)

# <codecell>

b.printBoard()

# <codecell>

b.makeMove(2,2)
b.printBoard()

# <codecell>

b.active_player

# <codecell>

for i in range(8):
    for j in range(8):
        if b.legalMove(i,j,b.active_player): print i,j

# <codecell>

b.makeMove(2,2)

# <codecell>

b.active_player

# <codecell>

game = Game()

# <codecell>

game.playGame()

# <codecell>

game.playGame()

# <codecell>

del b

# <codecell>

game = Game()

# <codecell>

game.playGame()

# <codecell>

game.game_board.printBoard()

# <codecell>

del game
del b

# <codecell>

del game

# <codecell>

game = Game()

# <codecell>

game.game_board.printBoard()

# <codecell>

game.playGame()

# <codecell>

game = Game()

# <codecell>

game.game_board.printBoard()

# <codecell>

game.playGame()

# <codecell>

game2 = Game()

# <codecell>

game.playGame()

# <codecell>

game2.playGame()

# <codecell>

game.game_board.active_player['opposite_player']['name'] = 'Joel'
print game2.game_board.active_player['name']

# <codecell>

game2.playGame()

# <codecell>


