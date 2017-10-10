import random
random_number = random.randint(0,10)

def guessed_number():
    number = input("Guess a number: ")
    number = int(number)
    return number

for guess in range(0,5):
    returned_number = guessed_number()
    if returned_number > random_number:
        print("Too high!")

    elif returned_number < random_number:
        print("Too low!")

    else:
        print("You guessed right!")
        break

