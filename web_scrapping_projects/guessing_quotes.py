import requests
from bs4 import BeautifulSoup
from random import choice

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
    bio_link = soup.select('.quote span a')
    all_bio.append(bio_link)

for links in all_bio:
    for link in links:
        all_bio_links.append(link.get('href'))

info_list = [(all_authors[i][j], all_quotes[i][j], all_bio_links[i])
             for i in range(len(all_authors)) for j in range(len(all_authors))]


# print(all_authors)
# print('\n\n')
# print(all_quotes)
# print('\n\n')
# print(all_bio_links)
# print(info_list)

pick = choice(info_list)
print(pick[1])

guesses_remaining = 4
while guesses_remaining > 0:
  player_guess = input("Who said the above quote?\nAnswer: ")
  if player_guess in pick:
    print('Congratulations! You have guessed the right person.')
    break
  elif guesses_remaining >= 2:
    print('Wrong answer, try again!')
    guesses_remaining -= 1
  else: 
    print('Game over!')
    break