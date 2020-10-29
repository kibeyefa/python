from random import *
from tkinter import *

# defining Window properties
root = Tk()
root.title("Rock Paper Scissors")


choices = ["rock", "paper", "scissors"]
messages = ["You Win", "Draw", "You Lose"]
player_score = 0
cpu_score = 0

def win_check(player_input):
   global messages, choices, player_score, cpu_score
   cpu_input = choice(choices)

   if player_input == choices[0] and cpu_input == choices[2] or player_input == choices[1] and cpu_input == choices[0] or  player_input == choices[2] and cpu_input == choices[1]:
      message.config(text=messages[0])
      cpu_choice = Label(root, text=cpu_input)
      message.grid(row=4, column=1)
      player_score += 1
      player_s.config(text=f"YOU: {player_score}")
      player_s.grid(row=4, column=0)
      cpu_s.config(text=f"CPU: {cpu_score}")
      cpu_s.grid(row=4, column=2)
   
   elif player_input == cpu_input:
      message.config(text=messages[1])
      message.grid(row=4, column=1)

   else:
      message.config(text=messages[2])
      message.grid(row=4, column=1)
      cpu_score += 1
      player_s.config(text=f"YOU: {player_score}")
      player_s.grid(row=4, column=0)
      cpu_s.config(text=f"CPU: {cpu_score}")
      cpu_s.grid(row=4, column=2)
         


game_label  = Label(root, text="Rock Paper Scissors", pady=20)
#label       = Label(root, text=cpu_input)
rock        = Button(root, text=choices[0].upper(), padx=40, pady= 40, activebackground='#00ff00', command= lambda: win_check(choices[0]))
paper       = Button(root, text=choices[1].upper(), padx=40, pady= 40, activebackground='#00ff00', command= lambda: win_check(choices[1]))
scissors    = Button(root, text=choices[2].upper(), padx=40, pady= 40, activebackground='#00ff00', command= lambda: win_check(choices[2]))
message     = Label(root, text="--", pady=20)
cpu_s       = Label(root,text=f"CPU: {cpu_score}",pady=20)
player_s    = Label(root,text=f"YOU: {player_score}",pady=20)



game_label.grid(row=0, column=1)
rock.grid(row=1, column=0)
paper.grid(row=1, column=1)
scissors.grid(row=1, column=2)
cpu_s.grid(row=4, column=2)
player_s.grid(row=4, column=0)
message.grid(row=4, column=1)










root.mainloop()