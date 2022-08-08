from turtle import screensize
import pygame

class Start():

    def __init__(self,screenSize):
        self.screenSize = screenSize
        self.numBombs = 0
        self.width_text = "16"
        self.height_text = "30"
        self.mine_text = "99"


    def getNumBombs(self):
        pass

    def getBoardSize(self):
        pass

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screenSize))

        self.base_font = pygame.font.Font(None, 32)

        boxColor = (190,190,190)

        boxHeight = 32

        self.easy_rect              = self.box_info(3,self.screenSize[0], 1, 3, self.screenSize[1], boxHeight, 1)
        self.intermediate_rect      = self.box_info(3,self.screenSize[0], 2, 3, self.screenSize[1], boxHeight, 1)
        self.expert_rect            = self.box_info(3,self.screenSize[0], 3, 3, self.screenSize[1], boxHeight, 1)
        self.width_input_rect       = self.box_info(6,self.screenSize[0], 2, 3, self.screenSize[1], boxHeight, 2)
        self.height_input_rec       = self.box_info(6,self.screenSize[0], 4, 3, self.screenSize[1], boxHeight, 2)
        self.width_text_rect        = self.box_info(6,self.screenSize[0], 1, 3, self.screenSize[1], boxHeight, 2)
        self.height_text_rec        = self.box_info(6,self.screenSize[0], 3, 3, self.screenSize[1], boxHeight, 2)
        self.mine_text_rec          = self.box_info(6,self.screenSize[0], 5, 3, self.screenSize[1], boxHeight, 2)
        self.mine_input_rec         = self.box_info(6,self.screenSize[0], 6, 3, self.screenSize[1], boxHeight, 2)
        self.submit_rect            = self.box_info(1,self.screenSize[0], 1, 3, self.screenSize[1], boxHeight, 3)





        self.width_rect_active = False
        self.height_rect_active = False
        self.mine_rect_active = False

        running = True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if self.easy_rect.collidepoint(event.pos):
                        self.width_text = "8"
                        self.height_text = "8"
                        self.mine_text = "10"
                    if self.intermediate_rect.collidepoint(event.pos):
                        self.width_text = "16"
                        self.height_text = "16"
                        self.mine_text = "40"
                    if self.expert_rect.collidepoint(event.pos):
                        self.width_text = "16"
                        self.height_text = "30"
                        self.mine_text = "99"
                    if self.width_input_rect.collidepoint(event.pos):
                        self.width_rect_active = True
                        self.height_rect_active = False
                        self.mine_rect_active = False
                    if self.height_input_rec.collidepoint(event.pos):
                        self.height_rect_active = True
                        self.width_rect_active = False
                        self.mine_rect_active = False
                    if self.mine_input_rec.collidepoint(event.pos):
                        self.mine_rect_active = True
                        self.width_rect_active = False
                        self.height_rect_active = False
                    if self.submit_rect.collidepoint(event.pos):
                            return [int(self.width_text), int(self.height_text), int(self.mine_text)]
                if event.type == pygame.KEYDOWN:
                    if self.width_rect_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.width_text = self.width_text[:-1]
                        else:
                            self.width_text += event.unicode
                    if self.height_rect_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.height_text = self.height_text[:-1]
                        else:
                            self.height_text += event.unicode
                    if self.mine_rect_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.mine_text = self.mine_text[:-1]
                        else:
                            self.mine_text += event.unicode


            self.easy_rect_surface              = self.base_font.render("Easy", True, (0, 0, 0))
            self.intermediate_rect_surface      = self.base_font.render("Intermediate", True, (0, 0, 0))
            self.expert_rect_surface            = self.base_font.render("Expert", True, (0, 0, 0))
            self.width_input_rect_surface       = self.base_font.render(self.width_text, True, (0, 0, 0))
            self.height_input_rec_surface       = self.base_font.render(self.height_text, True, (0, 0, 0))
            self.width_text_rect_surface        = self.base_font.render("Width:", True, (0, 0, 0))
            self.height_text_rec_surface        = self.base_font.render("Height:", True, (0, 0, 0))
            self.mine_text_rec_surface          = self.base_font.render("Mine:", True, (0, 0, 0))
            self.mine_input_rec_surface         = self.base_font.render(self.mine_text, True, (0, 0, 0))
            self.submit_rect_surface            = self.base_font.render("Submit", True, (0, 0, 0))

            self.screen.fill((200,200,200))
            pygame.draw.rect(self.screen, boxColor      , self.easy_rect        )
            pygame.draw.rect(self.screen, boxColor      , self.intermediate_rect)
            pygame.draw.rect(self.screen, boxColor      , self.expert_rect      )
            pygame.draw.rect(self.screen, (255,255,255) , self.width_input_rect )
            pygame.draw.rect(self.screen, (200,200,200) , self.width_text_rect  )
            pygame.draw.rect(self.screen, (255,255,255) , self.height_input_rec )
            pygame.draw.rect(self.screen, (200,200,200) , self.height_text_rec  )
            pygame.draw.rect(self.screen, (255,255,255) , self.mine_input_rec   )
            pygame.draw.rect(self.screen, (200,200,200) , self.mine_text_rec    )
            pygame.draw.rect(self.screen, boxColor      , self.submit_rect      )

            
            self.screen.blit(self.easy_rect_surface        , (self.easy_rect.x + 5          , self.easy_rect.y + 5 ))  
            self.screen.blit(self.intermediate_rect_surface, (self.intermediate_rect.x + 5  , self.intermediate_rect.y + 5 ))  
            self.screen.blit(self.expert_rect_surface      , (self.expert_rect.x + 5        , self.expert_rect.y + 5 ))  
            self.screen.blit(self.width_input_rect_surface , (self.width_input_rect.x + 5   , self.width_input_rect.y + 5 ))  
            self.screen.blit(self.height_input_rec_surface , (self.height_input_rec.x + 5   , self.height_input_rec.y + 5 ))  
            self.screen.blit(self.width_text_rect_surface  , (self.width_text_rect.x + 5    , self.width_text_rect.y + 5 ))  
            self.screen.blit(self.height_text_rec_surface  , (self.height_text_rec.x + 5    , self.height_text_rec.y + 5 ))  
            self.screen.blit(self.mine_text_rec_surface    , (self.mine_text_rec.x + 5      , self.mine_text_rec.y + 5 ))  
            self.screen.blit(self.mine_input_rec_surface   , (self.mine_input_rec.x + 5     , self.mine_input_rec.y + 5 ))  
            self.screen.blit(self.submit_rect_surface      , (self.submit_rect.x + 5        , self.submit_rect.y + 5 ))  

            pygame.display.flip()
        pygame.quit()


    def box_info(self, numBoxs, screenWidth, index, numRows, screenHeight, boxHeight, row):
        numBoxs = numBoxs+1
        
        
        buffer = screenWidth/((numBoxs)**2)
        boxWidth = (screenWidth - (buffer*numBoxs))/ (numBoxs-1)
        print(boxWidth)
        x = buffer*index + boxWidth*(index-1)

        y_buffer = ((screenHeight-3*boxHeight)/(numRows+1))
        y = y_buffer*row + boxHeight*(row-1)
        
        return pygame.Rect(x,y,boxWidth,boxHeight)

