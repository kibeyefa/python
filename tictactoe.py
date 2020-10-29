from numpy import *

def create_board():
   board = zeros((3,3))
   return board

def is_valid_location(board, columnm, row):
   global spot
   spot = board[row][column]
   return board[row][columnm] == 0

 
def drop_piece(piece):
      board[row][column] = piece
      


board = create_board()
game_over =  False
turn = 1

while not game_over:
   print(board)

   if turn == 1: #Player 1
      place = input("Player 1 Enter column(0-2) and row(0-2) you wish to select as (column row): ")
      place = place.split(" ")
      row = int(place[0])
      column = int(place[1])
      if not is_valid_location:
         drop_piece(spot)
      elif is_valid_location:
         drop_piece(1)
      

   else: #Player 2
      place = input("Player 2 Enter column(0-2) and row(0-2) you wish to select as (column row): ")
      place = place.split(" ")
      row = int(place[0])
      column = int(place[1])
      if not is_valid_location:
         drop_piece(spot)
      elif is_valid_location:
         drop_piece(1)

   turn += 1
   turn = turn % 2
   print(place)

   

