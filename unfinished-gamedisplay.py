import pygame
from chatAPI import prompt
from random import randint

class main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720),)
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
                            if self.themeCheck(tb.user_text):
                                self.theme[1]=tb.user_text;self.theme[0]=True
                            else:
                                print("Try again")
                
                else:
                    if submitQ.input_rect.collidepoint(event.pos):
                        submitQ.active = True
                    else: 
                        submitQ.active = False
            if mainLoop.gameInProgress==True and submitQ !=None:
                if submitQ.active==True:
                    print("t")
                    if event.type == pygame.KEYDOWN:
                        print("t1")

                        if event.key == pygame.K_BACKSPACE: 
                            # get text input from 0 to -1 i.e. end. 
                            submitQ.user_text = submitQ.user_text[:-1] 
        
                        else: 
                            submitQ.user_text += event.unicode


            if tb.active==True:
                if event.type == pygame.KEYDOWN: 

                    if event.key == pygame.K_BACKSPACE: 
                        # get text input from 0 to -1 i.e. end. 
                        tb.user_text = tb.user_text[:-1] 
    
                    else: 
                        tb.user_text += event.unicode
    def themeCheck(self,theme):
        return True



class game():
    def __init__(self,no):
        self.players=[]
        self.theme=mainLoop.theme
        self.answers=[]
        for i in range(no):
            self.players.append(player(i))
        self.curPlayer=0

    def gamePlayLoop(self):
        mainLoop.screen.fill("black")
        self.players[self.curPlayer].drawPlayer()
        guess="cow"
        # if self.checkAnswer(guess):
        #     print("Correct")
        #     self.answers.append(guess)
        #     self.curPlayer+=1
        #     if self.curPlayer>len(self.players)-1:
        #         self.curPlayer=0
        # else:
        #     print("Try Again")
    
    def checkAnswer(self,guess):
        if guess in self.answers:
            return False
        else:
            if prompt("Theme: "+ self.theme[1] + "Guess: "+ guess) == "true":
                return True
            else:
                return False
        


class player():
    def __init__(self,no):
        self.name=str(no)
        self.alive=True
        self.colour=(randint(0,255),randint(0,255),randint(0,255))
        self.rect=pygame.Rect(300,200,400,400)

    def drawPlayer(self):
        pygame.draw.rect(mainLoop.screen, self.colour, self.rect)
        


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
        self.rect.x=tb.input_rect.x+tb.input_rect.w+5

        

class textBox():
    def __init__(self,pos):
        self.base_font = pygame.font.Font(None, 32) 
        self.user_text = ''
        self.width=140
        self.height=32
        if pos == None:
            self.pos=(mainLoop.screen.get_width()//2-(self.width//2),mainLoop.screen.get_height()//2-100)
        else:
            self.pos=(mainLoop.screen.get_width()//2,mainLoop.screen.get_height()-100)
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
        self.input_rect.x = mainLoop.screen.get_width()//2-(self.input_rect.w//2)
  
submitQ=None  



tb=textBox(None)
tbS=textBoxSubmit()
mainTime=game(4)
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
            mainTime.gamePlayLoop()
            if submitQ==None:
                # print("DONE")
                submitQ=textBox("question")
            else:
                # print("ok")
                submitQ.isActive()
                submitQ.draw()
                print(submitQ.user_text)
            


        pygame.display.flip()
        mainLoop.dt = mainLoop.clock.tick(60) / 1000
