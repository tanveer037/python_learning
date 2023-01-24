import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored, COLORS

text_first = figlet_format("Dad Joke 3000")
print(colored(text_first, color="magenta"))

url = "https://icanhazdadjoke.com/search"

search_term = input("Let me tell you a joke! Give me a topic: ")


def dad_joke(given_item):
    response = requests.get(url,
                            headers={"accept": "application/json"},
                            params={"term": given_item
                                    }
                            )
    data = response.json()
    temp_list = data['results']
    while temp_list == []:
        return "No search result, please try again"
    joke = choice([item['joke'] for item in temp_list])
    joke_count = len(data['results'])
    return f"I have got {joke_count} jokes about {search_term}. Here's one: {joke} "


print(dad_joke(search_term))
