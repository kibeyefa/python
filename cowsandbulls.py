import random

digit_1 = random.randint(0, 9)
digit_2 = random.randint(0, 9)
digit_3 = random.randint(0, 9)
digit_4 = random.randint(0, 9)
cows = 0
bulls = 0
digits = [digit_1, digit_2, digit_3, digit_4]

user_guess = input("Enter 4 digit number (eg: 0-0-0-0): ")
match_list = user_guess.split("-")
user_guess = []

for i in match_list:
	user_guess.append(int(i))

for x in range(4):
	if user_guess[x] in digits:
		if user_guess[x] == digits[x]:
			cows += 1
		if user_guess[x] != digits[x]:
			bulls += 1

print(f"Cows = {cows}, Bulls = {bulls}")