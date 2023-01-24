print("  ..ROCK..  \n ...PAPER... \n....SCISSORS....")

player1 = input("Enter player1 name: ")
player2 = input("Enter player2 name: ")
player1_bet = input(f"Enter your bet, {player1} : ")

while not(player1_bet == "rock" or player1_bet == "paper" or player1_bet == "scissors"):
    player1_bet = input(f"Invalid input, enter your bet, {player1} : ")

print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")
print("No cheating!\n")

player2_bet = input(f"Enter your bet, {player2} : ")
player2_bet = input(f"Enter your bet, {player2} : ").lower()
while not(player2_bet == "rock" or player2_bet == "paper" or player2_bet == "scissors"):
    player2_bet = input(f"Invalid input, enter your bet, {player2} : ").lower()

if player1_bet == "rock" and player2_bet == "scissors":
    print( f" {player1} wins! " )
    
elif player1_bet == "rock" and player2_bet == "paper":
    print( f" {player2} wins! " )
    
elif player1_bet == "rock" and player2_bet == "rock":
    print( f"It's a tie!" )
    
elif player1_bet == "paper" and player2_bet == "rock":
    print( f" {player1} wins! " )
    
elif player1_bet == "paper" and player2_bet == "scissors":
    print( f" {player2} wins! " )
    
elif player1_bet == "paper" and player2_bet == "paper":
    print( f"It's a tie!" )
    
elif player1_bet == "scissors" and player2_bet == "paper":
    print( f" {player1} wins! " )
    
elif player1_bet == "scissors" and player2_bet == "rock":
    print( f" {player2} wins! " )
    
elif player1_bet == "scissors" and player2_bet == "scissors":
    print( f"It's a tie!" )
        