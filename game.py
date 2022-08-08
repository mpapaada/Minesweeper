from turtle import position, right
from piece import Piece
import pygame
import os

class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screenSize))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN ): #and ( not self.board.getLost() and not self.board.getWin())):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        topLeft = (0,0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row,col))
                image = self.getImages(piece)
                background = self.getBackground(piece)
                self.screen.blit(background, topLeft)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if not fileName.endswith(".png"):
                continue
            image = pygame.image.load(r"images/"+fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImages(self, piece):
        string = None
        if (piece.getClicked()):
            string = "mine" if piece.getHasBomb() else "number_" + str(piece.getNumAround()) if piece.getNumAround() > 0 else "tile_revealed"
        elif(piece.getFlagged()):
            string = "flag"
        else:
            string = "tile_hidden"
        
        return self.images[string]

    def getBackground(self, piece):
        if(piece.getClicked()):
            string = "tile_revealed" 
        else:
            string = "tile_hidden"
        return self.images[string]

    def handleClick(self, pos, rightClick):
        index = pos[1] // self.pieceSize[1], pos[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)

