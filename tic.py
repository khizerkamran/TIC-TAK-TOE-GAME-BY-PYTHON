import pygame
import sys
import time
import random


class GridCell():
    ocqupied = False
    def __init__(self,x,y,width,height, pos, text='', color=(255,255,255)):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.pos = pos


    def draw(self,screen,text_size):
        pygame.draw.rect(screen, (0,0,0), (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', text_size)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
 

class Game():
    letter = "O"
    previous_moves =[0,0,0,0,0,0,0,0,0]
    game_over = False
    x_score=0
    o_score=0

    def game_over_screen(self, message):
        pygame.draw.rect(screen, (255,255,0), (40,120,240,80),0)
        font = pygame.font.SysFont('comicsans', 72)
        text = font.render(message, 1, (0,0,0))
        screen.blit(text, (60 + (200/2 - text.get_width()/2), 140 + (50/2 - text.get_height()/2)))

    def move(self,pos,screen):
        self.previous_moves[pos]=self.letter
        if self.isWin(self.previous_moves,self.letter) == 1:
            pygame.draw.line(screen, (0,0,0), (15,55), (305,55), 5)
            message = f'{self.letter} Wins'
            self.game_over_screen(message)

            if self.letter == 'X':
                self.x_score +=1
            else:
                self.o_score +=1
            
            self.game_over=True
        elif self.isWin(self.previous_moves,self.letter) == 2:
            pygame.draw.line(screen, (0,0,0), (15,155), (305,155), 5)
            message = f'{self.letter} Wins'
            self.game_over_screen(message)
            if self.letter == 'X':
                self.x_score +=1
            else:
                self.o_score +=1
            self.game_over=True       
        elif self.isWin(self.previous_moves,self.letter) == 3:
            pygame.draw.line(screen, (0,0,0), (15,255), (305,255), 5)
            message = f'{self.letter} Wins'
            self.game_over_screen(message)
            if self.letter == 'X':
                self.x_score +=1
            else:
                self.o_score +=1
            
            self.game_over=True
        elif self.isWin(self.previous_moves,self.letter) == 4:
            pygame.draw.line(screen, (0,0,0), (60,15), (60,305), 5)
            message = f'{self.letter} Wins'
            self.game_over_screen(message)
            if self.letter == 'X':
                self.x_score +=1
            else:
                self.o_score +=1
            
            self.game_over=True
        elif self.isWin(self.previous_moves,self.letter) == 5:
            pygame.draw.line(screen, (0,0,0), (160,15), (160,305), 5)
            message = f'{self.letter} Wins'
            self.game_over_screen(message)
            if self.letter == 'X':
                self.x_score +=1
            else:
                self.o_score +=1
            
            self.game_over=True
        elif self.isWin(self.previous_moves,self.letter) == 6:
            pygame.draw.line(screen, (0,0,0), (260,15), (260,305), 5)
            message = f'{self.letter} Wins'
            self.game_over_screen(message)
            if self.letter == 'X':
                self.x_score +=1
            else:
                self.o_score +=1
            
            self.game_over=True
        elif self.isWin(self.previous_moves,self.letter) == 7:
            pygame.draw.line(screen, (0,0,0), (20,20), (300,300), 5)
            message = f'{self.letter} Wins'
            self.game_over_screen(message)
            if self.letter == 'X':
                self.x_score +=1
            else:
                self.o_score +=1
            
            self.game_over=True
        elif self.isWin(self.previous_moves,self.letter) == 8:
            pygame.draw.line(screen, (0,0,0), (20,295), (300,20), 5)
            message = f'{self.letter} Wins'
            self.game_over_screen(message)
            if self.letter == 'X':
                self.x_score +=1
            else:
                self.o_score +=1
            
            self.game_over=True
        elif self.previous_moves.count(0) ==0:
            message = 'It is a Tie'
            self.game_over_screen(message)
            self.game_over=True
        else:
            if self.letter=='X':
                self.letter = 'O'
            else:
                self.letter = 'X'


    def isWin(self,previous_moves, letter):
        if (previous_moves[0] == letter and previous_moves[1] == letter and previous_moves[2] == letter):
            return 1
        elif (previous_moves[3] == letter and previous_moves[4] == letter and previous_moves[5] == letter):
            return 2
        elif (previous_moves[6] == letter and previous_moves[7] == letter and previous_moves[8] == letter):
            return 3
        elif (previous_moves[0] == letter and previous_moves[3] == letter and previous_moves[6] == letter):
            return 4
        elif (previous_moves[1] == letter and previous_moves[4] == letter and previous_moves[7] == letter):
            return 5
        elif (previous_moves[2] == letter and previous_moves[5] == letter and previous_moves[8] == letter):
            return 6
        elif (previous_moves[0] == letter and previous_moves[4] == letter and previous_moves[8] == letter):
            return 7
        elif (previous_moves[2] == letter and previous_moves[4] == letter and previous_moves[6] == letter):
            return 8


pygame.init()
screen = pygame.display.set_mode((320,360))
pygame.display.set_caption("Tic Tac Toe")

#game icon
programIcon = pygame.image.load('icon.ico')
pygame.display.set_icon(programIcon)

clock = pygame.time.Clock()

game = Game()

#define cells for the grid
cell1 = GridCell(10,10,100,100,0)
cell2 = GridCell(110, 10, 100, 100,1)
cell3 = GridCell(210, 10, 100, 100,2)
cell4 = GridCell(10, 110, 100, 100,3)
cell5 = GridCell(110, 110, 100, 100,4)
cell6 = GridCell(210, 110, 100, 100,5)
cell7 = GridCell(10, 210, 100, 100,6)
cell8 = GridCell(110, 210, 100, 100,7)
cell9 = GridCell(210, 210, 100, 100,8)
cells = [cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9]

def draw_grid(screen,cells,scores):
    screen.fill(board_color)
    for cell in cells:
        cell.draw(screen,60)
    
    font = pygame.font.SysFont('comicsans', 36)
    text = font.render(scores, 1, (0,0,0))
    screen.blit(text, (100, 320))


def start_menu(screen,scores):
    start_game = GridCell(60, 50, 200, 40,5,'START NEW GAME',color=(255,0,0))
    exit_game = GridCell(60, 100, 200, 40,5,'EXIT THE GAME',color=(255,0,0))
    intro = True
    while intro:
        screen.fill((255,255,255))
        #exit from the game
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game.isOver(pos):
                    intro = False
                    
                if exit_game.isOver(pos):
                    intro = False
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.MOUSEMOTION:
                if start_game.isOver(pos):
                    start_game.color = (0,255,0)
                else:
                    start_game.color = (255, 0, 0)

                if exit_game.isOver(pos):
                    exit_game.color = (0,255,0)
                else:
                    exit_game.color = (255, 0, 0)

        start_game.draw(screen,25)
        exit_game.draw(screen,25)
        font = pygame.font.SysFont('comicsans', 36)
        text = font.render(scores, 1, (0,0,0))
        screen.blit(text, (100, 320))
        #update the screen
        pygame.display.update()

delay_loop=1
board_color = (0,0,255)
scores = f"X: {game.x_score} - {game.o_score} :O"
#draw_grid(screen,cells,scores)
pygame.display.update()

start_menu(screen,scores)
run = True
start = 0
while run:
    clock.tick(30)
    if delay_loop > 0:
        delay_loop +=1
    if delay_loop > 8:
        delay_loop = 0
    
    if start == 0:
        draw_grid(screen,cells,scores)
        letter = random.choice(["X","O"])
        game.letter=letter
        game.game_over_screen(f"{letter} starts")
        pygame.display.update()
        time.sleep(2)
        draw_grid(screen,cells,scores)
        pygame.display.update()
        start = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #print(pos)
            for cell in cells:
                if cell.isOver(pos) and cell.ocqupied==False and not game.game_over and delay_loop == 0:
                    cell.color = (0,255,0)
                    cell.text = game.letter
                    cell.ocqupied = True
                    draw_grid(screen,cells,scores)
                    game.move(cell.pos,screen)
                    pygame.display.update()
                    delay_loop =1
                    

    if game.game_over:
        scores = f"X: {game.x_score} - {game.o_score} :O"
        game.game_over = False
        game.letter="O"
        time.sleep(2)
        start = 0
        for cell in cells:
            cell.ocqupied=False
            cell.text = ''
            game.previous_moves=[0,0,0,0,0,0,0,0,0]
            cell.color = (255,255,255)
        start_menu(screen,scores)
                    
                

    
    