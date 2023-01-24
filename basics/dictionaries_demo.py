from traceback import print_tb


game =  { "name": "Red Dead Redemptions 2", "hours": 88.6 }
print(game)
game2 = dict( name = "Conan Exiles", hours = 24.7 )
print(game2)
print(game["name"], game2["name"])
for value in game.values():
    print(value)
for key in game.keys():
    print(key)
for item in game.items():
    print(item)
for key,value in game.items():
    print(f"Key = {key}, Value = {value} ")

artist = {
    "first": "Tanveer",
    "last": "Tayeb",
}

full_name = f"{artist['first']} {artist['last']}"
print(full_name)

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = 0
for donations in donations.values():
    total_donations += donations
print(total_donations)
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print( f"{bakery_stock.get(f'{food}')} left ")
else:
    print("We don't make that")