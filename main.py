from turtle import screensize
from game import Game
from board import Board
from start import Start

startSize = (600, 200)
start = Start(startSize)
info = start.run()
print(info)

size = (info[0],info[1])
prob = info[2]
board = Board(size, prob)
screenSize = (50*info[1],50*info[0])
game = Game(board, screenSize)
game.run()