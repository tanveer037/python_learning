import random

while True:
    number = int( input("Guess a number between 1 and 10: ") )
    answer = random.randint(1,10)
    while number!= answer:
        if number < answer:
            print("Too low, try again")
            number = int( input() )
        else:
            print("Too high, try again")
            number = int( input() )
    print("You win!")
    
    cont = input("Another one? Y/n > ")
    while cont.lower() not in ("y","n"):
        cont = input("Another one? Y/n > ")
    if cont == "n":
        print("Thanks for playing!")
        break



