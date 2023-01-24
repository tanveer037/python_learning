import random
import re
def hello_world():
    print("Hello World")
# hello_world()
def coin_toss():
    coin = [ 'Head', 'Tail' ]
    return random.choice(coin)
# winner = coin_toss()
# print(winner)
def generate_evens():
    numbers = list(range(1,50))
    return [ num for num in numbers if num%2==0 ]
# print(generate_evens())
def yell(speech):
    return '{}'.format(speech).upper()
# print( yell('moron!') )
def speak(animal = 'dog'):
    if animal == 'pig':
        return 'oink'
    if animal == 'duck':
        return 'quack'
    if animal == 'cat':
        return 'meow'
    if animal == 'dog':
        return 'woof'
    return '?'
