import requests
from bs4 import BeautifulSoup as bs

def get_meaning(word):
    url = 'https://dictionary.cambridge.org/dictionary/english/'

    # https://stackoverflow.com/questions/63648752/requests-exceptions-connectionerror-connection-aborted-remotedisconnected
    header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }

    resp = requests.get(url + word, headers=header)

    soup = bs(resp.text, 'html.parser')
    div = soup.find(class_='entry-body')

    pos = div.find(class_='pos dpos').text
    meaning = div.find(class_='def ddef_d db').text

    return pos, meaning

if __name__ == '__main__':
    word = input('Enter a word: ')
    pos, meaning = get_meaning(word)
    print(f'{word} ({pos})')
    print(meaning)