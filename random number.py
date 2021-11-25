import random

top_of_range = input("Type a number: ") #Number Input for upper range

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:                                  #checking the input number
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)  #generate random number
guesses = 0   #count numbetr of gueses

while True:
    guesses += 1
    user_guess = input("Make a guess: ")   #input to guess a number
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:       #guessing the input number
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses") # final output