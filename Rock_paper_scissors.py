import random

def Main():
    print("\n \n \n WELCOME TO ROCK PAPER SCISSORS ! \n")
    print("1. Single Player \n2. Two player \n3. exit \n")

    choice_menu = int(input('Enter the choice number : '))
    if choice_menu == 1:
        single_player()
    elif choice_menu == 2:
        two_player()
    elif choice_menu == 3:
        exit()
    else:
        print("Wrong choice! Choose a number from the choices ")
        Main()

def single_player():

    valid_choices = ('rock','paper','scissor')
    no_wins = 0
    no_loses = 0
    no_ties = 0

    while True:
        try:
            choice = input(("Rock, paper, or scissors? (rock/paper/scissor) : ")).lower()
            comp_choice = random.choice(valid_choices)

            print(f'You Chose {choice}')
            print(f'System Chose {comp_choice}')
            
            if choice not in valid_choices:
                print("Invalid choice! Try Again !")

            elif choice == comp_choice:
                ties += 1
                print('Tie !')

            elif (
                (choice == 'rock' and comp_choice == 'scissor' ) or 
                (choice == 'paper' and comp_choice == 'rock') or 
                (choice == 'scissor' and comp_choice == 'paper')):

                no_wins += 1
                print('You Win !')

            else:
                no_loses += 1
                print('You Loose !')

            c = input('Continue? (y/n): ').lower()
            if c == 'n':
                print('Wins :',no_wins)
                print('Loses :',no_loses)
                print('Ties :',no_ties)
                Main()
            
        except ValueError:
            print("Invalid choice! Try Again" )

def two_player() :
    no_wins_player_1 = 0
    no_loses_player_1 = 0
    
    no_ties = 0

    no_wins_player_2 = 0
    no_loses_player_2 = 0

    while True:
        try:
            choice_player_1 = input(("Player 1 \nRock, paper, or scissors? (rock/paper/scissor) : ")).lower()
            print()
            choice_player_2 = input(("Player 2 \nRock, paper, or scissors? (rock/paper/scissor) : ")).lower()
            print()
            
            print(f'Player 1 Chose {choice_player_1}')
            print(f'Player 2 Chose {choice_player_2} \n')
            
            if choice_player_1 and choice_player_2 not in valid_choices:
                print("Invalid choice! Try Again !")

            elif choice_player_1 == choice_player_2:
                ties += 1
                print('Tie ! \n')

            elif (
                (choice_player_1 == 'rock' and choice_player_2 == 'scissor' ) or 
                (choice_player_1 == 'paper' and choice_player_2 == 'rock') or 
                (choice_player_1 == 'scissor' and choice_player_2 == 'paper')):

                no_wins_player_1 += 1
                no_loses_player_2 += 1
                print('Player 1 wins ! \n')

            elif (
                (choice_player_2 == 'rock' and choice_player_1 == 'scissor' ) or 
                (choice_player_2 == 'paper' and choice_player_1 == 'rock') or 
                (choice_player_2 == 'scissor' and choice_player_1 == 'paper')):

                no_wins_player_2 += 1
                no_loses_player_1 += 1
                print('Player 2 wins ! \n')

            c = input('Continue? (y/n): ').lower()
            if c == 'n':
                print('Number of wins - Player 1 :',no_wins_player_1, '\n')
                print('Number of wins - Player 2 :',no_wins_player_2, '\n')
                print('Ties :',no_ties)
                Main()
            
        except ValueError:
            print("Invalid choice! Try Again" )    

valid_choices = ('rock','paper','scissor')
Main()