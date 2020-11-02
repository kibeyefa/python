from numpy import *
import pygame
import sys


rows = 3
columns = 3
# color = (0, 0, 0)
player_1_color = (255,0,0)
player_2_color = (255,255,0)
# light_green = (255,255,255)
green = (0, 255, 0)
light_green = (0, 95, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)


def create_board():
   board = zeros((rows, columns))
   return board

def not_valid_location(board, columnm, row):
   return board[column][row] != 0


def drop_piece(piece):
   global row, column
   board[column][row] = piece
      
def win_check(board, piece):
   # Horizontal wins 
   if board[0][0] and board[0][1] and board[0][2] == piece or board[0][0] and board[1][0] and board[2][0]:
      return True
   
   elif board[2][2] and board[1][2] and board[0][2] == piece or board[2][2] and board[2][1] and board[2][0]:
      return True

   if board[1][0] and board[1][1] and board[1][2] == piece:
      return True
 
   ## Diagonal winning
   if board[1][1] != 0:
      if board[1][1] and board[0][0] and board[2][2] == piece:
         return True
      
      elif board[1][1] and board[0][2] and board[2][0] == piece:
         return True

   
def draw_board():
   pygame.draw.line(screen, light_green, (200 , 10), ( 200,HIEGHT - 10), 20)
   pygame.draw.line(screen, light_green, (420 , 10), ( 420,HIEGHT - 10), 20)
   pygame.draw.line(screen, light_green, (10 , 200), ( WIDTH - 10, 200), 20)
   pygame.draw.line(screen, light_green, (10 , 420), ( WIDTH - 10, 420), 20)
   pygame.display.update()

board = create_board()
turn = 0
running = True
WIDTH, HIEGHT = 640, 640
pygame.init()
screen = pygame.display.set_mode((WIDTH, HIEGHT)) 
screen.fill(green)
clock =  pygame.time.Clock()
FPS =  60
clock.tick(FPS)


while running:
   yellow = (255,255, 0)
   red = (255,0,0)
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
         running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
         row_pos = event.pos[1]
         column_pos = event.pos[0]

         def create_circle(color):
            if row_pos < 201:
               if column_pos < 201:
                  pygame.draw.circle(screen, color, (95, 95), 90, 0)
               elif column_pos > 220 and column_pos < 421:
                  pygame.draw.circle(screen, color, (310, 95), 90, 0) #[0,1]
               elif column_pos > 440:
                  pygame.draw.circle(screen, color, (530, 95), 90, 0) #[0,2]

            if row_pos > 220 and row_pos < 421:
               if column_pos < 201:
                  pygame.draw.circle(screen, color, (95, 310), 90, 0) #[1,0]
               elif column_pos > 220 and column_pos < 421:
                  pygame.draw.circle(screen, color, (310, 310), 90, 0)#[1,1]
               elif column_pos > 440:
                  pygame.draw.circle(screen, color, (530, 310), 90, 0)#[1,2]

            if row_pos > 440:
               if column_pos < 201:
                  pygame.draw.circle(screen, color, (95, 530), 90, 0)#[2,0]
               elif column_pos > 220 and column_pos < 421:
                  pygame.draw.circle(screen, color, (310, 530), 90, 0)#[2,1]
               elif column_pos > 440:
                  pygame.draw.circle(screen, color, (530, 530), 90, 0)#[2,1]

         def draw_circle():
            global piece
            if piece == 1:
               create_circle(red)
            
            if piece == 2:
               create_circle(yellow)
            
         if turn == 0: #Player 1
            print("player 1")
            piece = 1
            if column_pos < 201:
               row = 0
            if column_pos > 220 and column_pos < 440:
               row = 1
            if column_pos > 440:
               row = 2

            if row_pos < 201:
               column = 0
            if row_pos > 220 and row_pos < 440:
               column = 1
            if row_pos > 440:
               column = 2
            
            if not_valid_location:
               spot = board[column][row]
               drop_piece(1)
               draw_circle()
               
            else:
               drop_piece(spot)
               

            if win_check(board, piece):
               print("Player 1 wins")
            
            # print(event.pos)

         if turn == 1:
            print("player 2")
            piece = 2
            if column_pos < 201:
               row = 0
            if column_pos > 220 and column_pos < 440:
               row = 1
            if column_pos > 440:
               row = 2

            if row_pos < 201:
               column = 0
            if row_pos > 220 and row_pos < 440:
               column = 1
            if row_pos > 440:
               column = 2
            
            if not_valid_location:
               spot = board[column][row]
               drop_piece(2)
               draw_circle()
            else:
               drop_piece(spot)
               

            if win_check(board, piece):
               print("Player 2 wins")

            
         turn += 1  
         turn = turn % 2
         print(board)
   draw_board()

   
pygame.quit()