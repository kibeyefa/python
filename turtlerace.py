from turtle import *
import random

start_y = -200
# draw finish line
line = Turtle()
line.penup()
line.goto(-250, 200)
line.pendown()
line.forward(500)

# Create players
player_1 = Turtle()
player_1.penup()
player_1.goto(-200, start_y)
player_1.color("red")
player_1.shape("turtle")
player_1.setheading(90)
player_1.pendown()

player_2 = Turtle()
player_2.penup()
player_2.color("yellow")
player_2.shape("turtle")
player_2.setheading(90)
player_2.goto(-150, start_y)
player_2.pendown()

player_3 = Turtle()
player_3.penup()
player_3.color("green")
player_3.shape("turtle")
player_3.setheading(90)
player_3.goto(-100, start_y)
player_3.pendown()

player_4 = Turtle()
player_4.penup()
player_4.color("blue")
player_4.shape("turtle")
player_4.setheading(90)
player_4.goto(-50, start_y)
player_4.pendown()

player_5 = Turtle()
player_5.penup()
player_5.color("purple") 
player_5.shape("turtle")
player_5.setheading(90)
player_5.goto(0, start_y)
player_5.pendown()

green = 0
blue = 0
red = 0
yellow = 0
purple = 0
winner = []
players = [player_1, player_2, player_3, player_4, player_5]

def score(color):
	global green, red, blue, yellow, purple

	if winner[0] == "green":
		green += 1

	if winner[0] == "red":
		red += 1

	if winner[0] == "blue":
		blue += 1

	if winner[0] == "purple":
		purple += 1

	if winner[0] == "yellow":
		yellow += 1



while True:
	player_2.forward(random.randint(1, 3))
	player_1.forward(random.randint(1, 3))
	player_3.forward(random.randint(1, 3))
	player_4.forward(random.randint(1, 3))
	player_5.forward(random.randint(1, 3))

	for player in players:
		if player.ycor() >= 200:
			if player.color() not in winner:
				winner.append(player.color())

	if player_1.ycor() >= 200 and player_2.ycor() >= 200 and player_3.ycor() >= 200 and player_4.ycor() >= 200 and player_5.ycor() >= 200:
		break









