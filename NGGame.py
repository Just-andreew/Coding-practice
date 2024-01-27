import random

def game():
    print ('Welcome to my number guessing game')
    print ('Im thinking of a number between 1 and 100')
    print ('You have ten tries to guess the number else...')
    print ('You get ...ELIMINATED.')

random_number = random.randint(1, 100)
guess = None
tries = 10

game()

while tries > 0:
    try:
        guess = int(input('Enter your guess : ')) 
        if guess < 1 or guess > 100:
            raise  ValueError       
        elif guess > random_number:
            print ("Your guess is too high, try lower.")
        elif guess < random_number:
            print ("Your guess is too low, try higher.")        
        else:
            print("\nCongratulations! You guessed it right!\nThe number was ",random_number,".\nWell done!")
            break
            
        tries -= 1
        if tries == 0:
            print ("You have run out of tries and will thus be eliminated .")
            print ("Dumb player ELIMINATED!")
        if  tries > 1:
            print("You have %s more tries." % tries)

    except ValueError as ve:
        print ("Invalid input",ve,"\nPlease enter a number between 1 and 100\nTry again.")
    


