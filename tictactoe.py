from numpy import *

rows = 3
columns = 3
def create_board():
   board = zeros((rows, columns))
   return board

def is_valid_location(board, columnm, row):
   global spot
   spot = board[row][column]
   return board[row][columnm] == 0

 
def drop_piece(piece):
      board[row][column] = piece
      
def win_check(board, piece):
## Horizontal wins 
   for c in range(columns - 1):
      for r in range(rows):
         if  board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece:
            return True

## Vertical wins 
   for c in range(columns):
      for r in range(rows -1):
         if  board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece:
            return True
 
## Positive slopped winning
   if board[1][1] != 0:
      if board[1][1] and board[0][0] and board[2][2] == piece:
         return True
      
      elif board[1][1] and board[0][2] and board[2][0] == piece:
         return True


board = create_board()
game_over =  False
turn = 0

while not game_over:
   print(board)

   if turn == 0: #Player 1
      place = input("Player 1 Enter column(0-2) and row(0-2) you wish to select as (row column): ")
      place = place.split(" ")
      row = int(place[0])
      column = int(place[1])
      if not is_valid_location:
         replay = True
         drop_piece(spot)
      elif is_valid_location:
         replay = False
         drop_piece(1)

      if win_check(board, 1):
         print("Player 1 wins")
         game_over =  True

      

   else: #Player 2
      place = input("Player 2 Enter column(0-2) and row(0-2) you wish to select as (row column): ")
      place = place.split(" ")
      row = int(place[0])
      column = int(place[1])
      if not is_valid_location:
         replay = True
         drop_piece(spot)
      elif is_valid_location:
         replay = False
         drop_piece(2)

      if win_check(board, 2):
         print("Player 2 wins")
         game_over = False
         

   if replay == True:
      turn += 2
   else:
      turn += 1

   turn = turn % 2
   
print(board)

   

