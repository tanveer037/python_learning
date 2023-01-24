from random import randint


print("  ..ROCK..  \n ...PAPER... \n....SCISSORS....")


player_wins = 0
computer_wins = 0
player1 = input("Enter player1 name: ")
player2 = "Computer"

while player_wins < 2 and computer_wins < 2:

    player1_bet = input(f"Enter your bet, {player1} : ").lower()
    while not(player1_bet == "rock" or player1_bet == "paper" or player1_bet == "scissors"):
        player1_bet = input(
            f"Invalid input, enter your bet, {player1} : ").lower()

    value = randint(1, 3)

    if value == 1:
        player2_bet = "rock"
    elif value == 2:
        player2_bet = "paper"
    else:
        player2_bet = "scissors"

    if player1_bet == "rock":
        if player2_bet == "paper":
            computer_wins += 1
            print(f" {player2} wins the round ! ")
            print(f" Player = {player_wins} Computer = {computer_wins} ")
        if player2_bet == "scissors":
            player_wins += 1
            print(f" {player1} wins the round! ")
            print(f" Player = {player_wins} Computer = {computer_wins} ")
        if player2_bet == "rock":
            print(f"It's a tie!")
            print(f" Player = {player_wins} Computer = {computer_wins} ")

    elif player1_bet == "paper":
        if player2_bet == "scissors":
            computer_wins += 1
            print(f" {player2} wins the round! ")
            print(f" Player = {player_wins} Computer = {computer_wins} ")
        if player2_bet == "rock":
            player_wins += 1
            print(f" {player1} wins the round! ")
            print(f" Player = {player_wins} Computer = {computer_wins} ")
        if player2_bet == "paper":
            print(f"It's a tie")
            print(f" Player = {player_wins} Computer = {computer_wins} ")

    elif player1_bet == "scissors":
        if player2_bet == "rock":
            computer_wins += 1
            print(f" {player2} wins the round! ")
            print(f" Player = {player_wins} Computer = {computer_wins} ")
        if player2_bet == "paper":
            player_wins += 1
            print(f" {player1} wins the round! ")
            print(f" Player = {player_wins} Computer = {computer_wins} ")
        if player2_bet == "scissors":
            print(f"It's a tie!")
            print(f" Player = {player_wins} Computer = {computer_wins} ")

if player_wins == 2:
    print(f" {player1} wins the game! ")
else:
    print(f" {player2} wins the game! ")
