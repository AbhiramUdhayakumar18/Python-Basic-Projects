import random

count = 0
min = int(input("Enter the lower value : "))
max = int(input("Enter the higher value : "))
print("You have 5 tries to find the number !")
number = random.randint(min,max)

while True:

    try:
        guess = int(input('Enter the guess : '))
        if guess < number & count < 4:
            count += 1
            print("Too low! Try Again")
        elif guess > number & count < 4:
            count += 1
            print("Too High! Try Again")
        elif guess == number & count < 4:
            count += 1
            print("Congrats, you guessed it in",count,"tries !")
            break
        else:
            print("You loose !")
            break

    except ValueError:
        print("Invalid Number Try Again !")