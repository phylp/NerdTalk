#bisection search
import math

print('Please think of a number between 0 and 100!')

low = 0
high = 100
correct = False

print('Please think of a number between 0 and 100!')

while not correct:
	guess = math.floor((low + high)/2)
	user_response = input("Is your secret number " + str(guess) + "? \n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly.")
	if user_response == 'l':
		low = guess 
	elif user_response == 'h':
		high = guess
	elif user_response == 'c':
		correct = True
		print('Game over. Your secret number was: ' + str(guess))
	else:
		print('Sorry, I did not understand your input')