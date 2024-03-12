import pygame
class main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        self.running = True
        self.gameInProgress=False
        self.dt = 0
        self.startGame=pygame.image.load("startGame.png")
        self.startGamePos=((self.screen.get_width()//2-128),(self.screen.get_height()//2+50))
        self.theme= [False,""]


    def mainMenu(self): 
        self.screen.fill("purple")
        
        self.screen.blit(self.startGame,self.startGamePos)


    def withinBorders(self,x,y,checkPosX,checkPosY):
        if (x>checkPosX and x < checkPosX+256) and (y>checkPosY and y<checkPosY+128):
            return True
        else:
            return False
            
    def game(self):
        self.screen.fill("black")
    def eventCheck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if self.gameInProgress != True:
                    if self.theme[0] == True:
                        if self.withinBorders(x,y,self.startGamePos[0],self.startGamePos[1]):
                            self.gameInProgress=True
                    else:
                        if tb.input_rect.collidepoint(event.pos):
                            tb.active = True
                        else: 
                            tb.active = False
                        if tbS.rect.collidepoint(event.pos):
                            mainLoop.theme[1]=tb.user_text;mainLoop.theme[0]=True
            if tb.active==True:
                if event.type == pygame.KEYDOWN: 

                    if event.key == pygame.K_BACKSPACE: 
                        # get text input from 0 to -1 i.e. end. 
                        tb.user_text = tb.user_text[:-1] 
    
                    else: 
                        tb.user_text += event.unicode
            
mainLoop=main()

class textBoxSubmit():
    def __init__(self):
        self.colour="black"
        self.pos=(tb.pos[0]+tb.input_rect.w+5,tb.pos[1])
        self.width=50
        self.height=32
        self.rect=pygame.Rect(self.pos[0],self.pos[1],self.width,self.height)
    def draw(self):
        pygame.draw.rect(mainLoop.screen, self.colour, self.rect)
        self.rect.x=tb.pos[0]+tb.input_rect.w+5

        

class textBox():
    def __init__(self):
        self.base_font = pygame.font.Font(None, 32) 
        self.user_text = ''
        self.pos=(200,200)
        self.width=140
        self.height=32
        self.input_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height) 
        self.color_active = pygame.Color('lightskyblue3')   

        self.color_passive = pygame.Color('chartreuse4') 
        self.color = self.color_passive
        self.active = False
    def isActive(self):
        if self.active: 
            self.color = self.color_active 
        else: 
            self.color = self.color_passive 
    def draw(self):
        pygame.draw.rect(mainLoop.screen, self.color, self.input_rect) 
  
        self.text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        mainLoop.screen.blit(self.text_surface, (self.input_rect.x+5, self.input_rect.y+5)) 
   
        self.input_rect.w = max(100, self.text_surface.get_width()+10)
    


class mainGame():
    def __init__(self):
        pass

tb=textBox()
tbS=textBoxSubmit()

while mainLoop.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        mainLoop.eventCheck()


        


        if mainLoop.gameInProgress != True:
             mainLoop.mainMenu()
             tb.isActive()
             tb.draw()
             tbS.draw()
        else:
             mainLoop.game()


        pygame.display.flip()
        mainLoop.dt = mainLoop.clock.tick(60) / 1000
