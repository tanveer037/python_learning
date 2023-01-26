#%%
import requests
from bs4 import BeautifulSoup
from random import choice
# %%
def flatten(l):
    return [item for sublist in l for item in sublist]
# %%
all_authors = []
all_quotes = []
all_bio = []
all_bio_links = []
for page in range(1, 11):
  url = f'https://quotes.toscrape.com/page/{page}/'
  html = requests.get(url)
  soup = BeautifulSoup(html.content, 'html.parser')
  author = soup.select('span .author')
  author_list = [item.get_text() for item in author]
  all_authors.append(author_list)
  quotes = soup.select('.quote .text')
  quotes_list = [item.get_text() for item in quotes]
  all_quotes.append(quotes_list)
  # # print( soup.find(class_ = 'author').find_next_sibling() )
  bio_link = soup.select('.quote span a')
  all_bio.append(bio_link)
    
for links in all_bio:
    for link in links:
        all_bio_links.append(link.get('href'))

flattened_list_of_authors = flatten(all_authors)
flattened_list_of_quotes = flatten(all_quotes)

info_list = list(zip(flattened_list_of_authors,flattened_list_of_quotes,all_bio_links))
# %%
def game_body(a_pick):
  guesses_remaining = 4
  # print(a_pick[0])
  print(a_pick[1])
  while guesses_remaining > 0:
    player_guess = input("Who said the above quote?\nAnswer: ")
    if player_guess in a_pick:
      print('Congratulations! You have guessed the right person.')
      break
    elif player_guess not in a_pick and guesses_remaining == 4:
      print('Wrong answer, please try again!')
      guesses_remaining -= 1
      url1 = f'https://quotes.toscrape.com{a_pick[2]}'
      html1 = requests.get(url1)
      soup1 = BeautifulSoup(html1.content, 'html.parser')
      b_date = soup1.find(class_ = "author-born-date").get_text()
      b_loc = soup1.find(class_ = "author-born-location").get_text()
      print(f'You have {guesses_remaining} guesses remaining! Here is the hint:')
      print(f'Author was born {b_date} {b_loc}')
    elif player_guess not in a_pick and guesses_remaining == 3:
      print('Wrong answer, please try again!')
      guesses_remaining -= 1
      print(f'You have {guesses_remaining} guesses remaining! Here is the hint:')
      print(f'The name starts with {a_pick[0][0]}')
    elif player_guess not in a_pick and guesses_remaining == 2:
      print('Wrong answer, please try again!')
      guesses_remaining -= 1
      print(f'You have {guesses_remaining} guesses remaining! Here is the hint:')
      print(f'Length of the name is {len(a_pick[0])}')
    elif player_guess not in a_pick:
      print('Game over')
      guesses_remaining -= 1
  
# %%
author_pick = choice(info_list)
game_body(author_pick)
while True:
  restart_game = input('Do you wanna play again? yes/no: ')
  if restart_game == 'no':
    print('Thanks for playing!')
    break
  elif restart_game == 'yes':
    author_pick = choice(info_list)
    game_body(author_pick)
  else:
    print('Please pick the correct option')
# %%
