from pyfiglet import figlet_format
from termcolor import colored, COLORS


def art(given_string, given_color):
    if given_color not in COLORS:
        given_color = 'magenta'
    text_first = figlet_format(given_string)
    return colored(text_first, color= given_color)

print( art(input("What message do you want to print? "), input("What color? ")) )