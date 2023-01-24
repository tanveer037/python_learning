from random import randint


print("  ..ROCK..  \n ...PAPER... \n....SCISSORS....")

player1 = input("Enter player1 name: ")
player2 = "Computer"
player1_bet = input(f"Enter your bet, {player1} : ").lower()

while not(player1_bet == "rock" or player1_bet == "paper" or player1_bet == "scissors"):
    player1_bet = input(f"Invalid input, enter your bet, {player1} : ").lower()

value = randint(1,3)

if value == 1:
    player2_bet = "rock"
elif value == 2:
    player2_bet = "paper"
else: player2_bet = "scissors"



if player1_bet == "rock":
    if player2_bet == "paper":
        print( f" {player2} wins! " )
    if player2_bet == "scissors":
        print( f" {player1} wins! " )
    if player2_bet == "rock":
        print( f"It's a tie!" )
elif player1_bet == "paper":
    if player2_bet == "scissors":
        print( f" {player2} wins! " )
    if player2_bet == "rock":
        print( f" {player1} wins! " )
    if player2_bet == "paper":
        print( f"It's a tie" )
elif player1_bet == "scissors":
    if player2_bet == "rock":
        print( f" {player2} wins! " )
    if player2_bet == "paper":
        print( f" {player1} wins! " )
    if player2_bet == "scissors":
        print( f"It's a tie!" )
