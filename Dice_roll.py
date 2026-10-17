import random

count = 0
while True:
    choice = input("Do you want to roll the dice? (y/n) : ").lower()
    if choice == 'y':
        n = int(input("Enter the number of dies you would like to roll !"))
        for i in range(0, n):
            a = random.randint(1,6)
            b = random.randint(1,6)
            print(f'({a}, {b})')
        count += n

    elif choice == 'n':
        print(count)
        print("Thank you for playing !")
        break

    else:
        print("invalid choice try again !")