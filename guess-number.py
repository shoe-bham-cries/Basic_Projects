import random
target = random.randint(1,100)
def game():
	logo = """

  _______  __    __   _______     _______.     _______.   .___________. __    __   _______    .__   __.  __    __  .___  ___. .______    _______ .______      
 /  _____||  |  |  | |   ____|   /       |    /       |   |           ||  |  |  | |   ____|   |  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \     
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`   `---|  |----`|  |__|  | |  |__      |   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |    
|  | |_ | |  |  |  | |   __|     \   \        \   \           |  |     |   __   | |   __|     |  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /     
|  |__| | |  `--'  | |  |____.----)   |   .----)   |          |  |     |  |  |  | |  |____    |  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.
 \______|  \______/  |_______|_______/    |_______/           |__|     |__|  |__| |_______|   |__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____|
                                                                   """                                                                                           


	global target
	print(logo)

	if(input("Choose a game mode \'easy\' or \'hard\': ")) == 'easy':
		guesses = 9
		print('You have 10 guesses')
	else:
		guesses = 4
		print('You have 5 guesses')

	def checker(user_guess,no):
		global target
		if user_guess == target:
			print(f"You win! The number was: {target}")
			return 0
		else: 
			if user_guess > target:
				print(f"Too high! try again You have {no} guesses left")
			else:
				print(f"Too low, Try again! You have {no} guesses left")
			return (no-1)

	while(guesses>-1):
		user = int(input('Enter your guess: '))
		guesses = checker(user,guesses)

	print(f"Correct Number was = {target}")


while(input("Do you want to play the game? Enter \'y\': ")) == 'y':
	game()
else:
	print("Goodbye!") 
