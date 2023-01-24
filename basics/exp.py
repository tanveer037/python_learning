suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values =  ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

d = {}

for suit in suits:
   d.update( {suit:values} )

print(d)