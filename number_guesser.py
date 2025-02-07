import random

top_of_range=input("Type a number: ")

# check if the typed is a digit then convert to int
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    # check if range is larger than 0
    if top_of_range <= 0:
        print("Please type a number larger than 0!")
        print("Exiting...")
        quit()

# if not digit exit app
else:
    print("Please type in a digit next time!")
    print("Exiting...")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0

while True:
    guesses+=1                       
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue

    if user_guess == random_number:
        print("Correct!You are winning!")
        break
    elif user_guess > random_number:
            print("You were above the number.")
    else:
        print("You were below the number.")

print("You got", guesses,"guesses")
