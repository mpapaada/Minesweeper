from operator import truediv
from piece import Piece
from random import shuffle

class Board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.lost = False
        self.won = False
        self.numClicked = 0
        self.numClear = 0
        self.setBoard()
        self.numMines = 0

        

    def setBoard(self):
        self.board = []
        self.mines = []

        self.numClear = (self.size[0]*self.size[1])-self.prob

        for mine in range(self.prob):
            self.mines.append("1")
        for clear in range(self.numClear):
            self.mines.append("0")

        shuffle(self.mines)
        
        for row in range(self.size[0]):
            rows  = []
            for col in range(self.size[1]):
                index = int(row*self.size[1]) + int(col)
                if self.mines[index] == "1":
                    hasBomb = True
                else:
                    hasBomb = False
                peice = Piece(hasBomb)
                rows.append(peice)
            self.board.append(rows)
        self.setNeighbors()
    
    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row,col))
                neighbors = self.getNeighbors((row,col))
                piece.setNeighbors(neighbors)

    def getNeighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] +2):
            for col in range(index[1]-1, index[1]+2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row,col)))
        return neighbors

    def getSize(self):
        return self.size

    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        if (not flag and piece.getFlagged()):        #if i left click on a flag
            return
        elif(flag and not piece.getClicked()):       #if i right click on a unrevealed piece
            if(piece.getFlagged()):
                piece.flagged = False
            else:
                piece.flagged = True
            for neighbor in piece.getNeighbors():
                neighbor.setFlaggedAround()
            return
        elif(not piece.getClicked()):               #if piece hasnt been clicked yet
            if(piece.getHasBomb()):
                piece.clicked = True
                # self.game.GameLost = True
                return
            elif(piece.getNumAround() == 0):
                for neighbor in piece.getNeighbors():
                    piece.clicked = True
                    self.handleClick(neighbor, False)
                return
            else:
                piece.clicked = True
                return
        elif(piece.getClicked()):                   #if piece is already clicked
            print("before flag check")
            if(piece.getFlaggedAround()):
                print("we get here")
                for neighbor in piece.getNeighbors():
                    if(not neighbor.getClicked() and not neighbor.getFlagged()):
                        self.handleClick(neighbor, False)
                return
            return







    
            