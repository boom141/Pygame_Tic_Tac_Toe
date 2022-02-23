
import pygame
from random import seed, randint
import os


# initialize all imported pygame modules.
pygame.init()

# declare surface with the set wisth and height.
Width, Height = 500, 500 
Window  = pygame.display.set_mode((Width,Height))

# list of combination row and columns to check the winner.
Combi_ = [ [0,1,2], [3,4,5], [6,7,8],  
[0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6],]

# constant/global variables.
FPS = 60
Image_Width, Image_Height = 90 ,90
Turn_ = True

# initialize Images for the game: Xs ,Os and board.
X_Image = pygame.image.load(os.path.join('Asset', 'X_2.png'))
X_ = pygame.transform.scale(X_Image, (Image_Width,Image_Height))

O_Image = pygame.image.load(os.path.join('Asset', 'O_2.png'))
O_ = pygame.transform.scale(O_Image, (Image_Width, Image_Height))

Table_Image = pygame.image.load(os.path.join('Asset', 'Table2.png'))

# function for the versus computer
def Versus_AI(Container_List, Board_List):
    seed(1)
    Computer_ = O_
    while True:
        Rand_index = randint(0,9)
        if(Board_List[Rand_index] is not X_ or 
            Board_List[Rand_index] is not O_):
            
             Window.blit(Computer_,(Container_List[Rand_index].x + 5,
              Container_List[Rand_index].y + 5))
        
# function for declaring the winner.
def Declare_Winner(Player_Winner, Board_):
    Font_ = pygame.font.Font(os.path.join('Asset/font', 'ChalkFont.ttf'), 30)
    Text_Winner = Font_.render(Player_Winner, False, 'white')
    Font_ = pygame.font.Font(os.path.join('Asset/font', 'ChalkFont.ttf'), 30)
    Text_Reset = Font_.render('Press Space Key To Reset', False, 'white')
    
    Window.blit(Text_Winner, (130, 30))
    Window.blit(Text_Reset, (62, 430))

# algorithm for making the board unclikable when the game ends.
    for i in range(9):
        if Board_[i] == O_ or Board_ == X_:
           pass
        else:
            Board_[i] = 0

# function to check if there is already a winner
def Check_Winner(Board_):
    Winner = None
    for i in range(8):    
      if(Board_[Combi_[i][0]] == Board_[Combi_[i][1]] == Board_[Combi_[i][2]]):
               Winner = Board_[Combi_[i][0]]
    
    if Winner == X_:
        Declare_Winner('Player One Won', Board_)
    elif Winner == O_:
        Declare_Winner('Player Two Won', Board_)
    else:
        pass

# function for the user action when clicking
def User_Action(Logic_Data, Container_List, Board_List):
    global Turn_

    if Turn_:
        Player_ = X_
        Turn_ = False
    else:
        Player_ = O_
        Turn_ = True

# Algorithm to avoid multiple clicks on the same container
    for con in Container_List:
        if (Logic_Data and con.collidepoint(pygame.mouse.get_pos()) and 
            isinstance(Board_List[Container_List.index(con)], str)):

            Window.blit(Player_,(con.x + 5, con.y + 5))
            Board_List[Container_List.index(con)] = Player_
            Versus_AI(Container_List,Board_List)
            Check_Winner(Board_List)
        else:
            Turn_ = not Turn_
    pygame.display.update()

# funtion for displaying the board in the game
def Draw_Grid(Container_List, Dimension):
    Window.fill((0,0,0))
    for y in range(3):
        for x in range(3):
            Container = pygame.draw.rect(Window, 'black', Dimension, 1)
            Container_List.append(Container)
            Dimension.x += 102  
        
        Dimension.y += 102
        Dimension.x = 98
    Window.blit(Table_Image, (60,60))
    pygame.display.update()

# main funtion of the game 
def main():
    global Turn_
    run = True
    clock = pygame.time.Clock()

    Container_List = []
    Board_List = ['O', 'X', 'O', 'X', 'O', 'O','X', 'O', 'X']

    Dimension = pygame.Rect(98, 98, 100, 100)

    Draw_Grid(Container_List, Dimension)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
     
            if event.type == pygame.MOUSEBUTTONDOWN:
                User_Action(True, Container_List, Board_List)

# alorothm to reset the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Turn_ = not Turn_
                    main()
                
if __name__ == "__main__":
    main()
