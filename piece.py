class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        self.allFlags = False

    def getHasBomb(self):                   #if piece is a bomb
        return self.hasBomb

    def getClicked(self):                   #if piece has been revealed
        return self.clicked

    def getFlagged(self):                   #if piece is flagged
        return self.flagged

    def getNumAround(self):                 #number of bombs around piece
        return self.numAround

    def getNeighbors(self):                 #returns array of neighbor pieces
        return self.neighbors

    def getFlaggedAround(self):             #returns true if flags around piece is equal to num of bombs around piece
        return self.allFlags 

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()

    def setNumAround(self):
        self.numAround = 0
        for piece in self.neighbors:
            if(piece.getHasBomb()):
                self.numAround += 1

    def setFlaggedAround(self):
        self.flaggedAround = 0
        for piece in self.neighbors:
            if (piece.getFlagged()):
                self.flaggedAround += 1
        if(self.flaggedAround == self.numAround):
            print("all flags around piece")
            self.allFlags = True
        else:
            self.allFlags = False
        