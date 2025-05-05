from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description='Скрипт выводит внутренние и внешних ссылки с указанной страницы на глубину 2')
parser.add_argument('-w','--write', action='store_true', help='Записать результат в файл')
parser.add_argument('--site', default='vesti53.com', help='Укажите сайт без https://, например vesti53.com')
args = parser.parse_args()

START_URL='https://'+args.site
INSIDE_URLS=[]
OUTSIDE_URLS=[]


def make_soup(URL):
    try:
        response = requests.get(URL)
    except:
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_url(soup):
    for i in soup.find_all('a'):
        if i.get('href','').startswith('http'):
            if START_URL[START_URL.find('//')+2:] not in i.get('href'):
                if i.get('href') not in OUTSIDE_URLS: OUTSIDE_URLS.append(i.get('href'))
            else:
                if START_URL+i.get('href','') not in INSIDE_URLS: INSIDE_URLS.append(i.get('href',''))
        elif i.get('href','').startswith('/'):
            if START_URL+i.get('href','') not in INSIDE_URLS: INSIDE_URLS.append(START_URL+i.get('href',''))

soup = make_soup(START_URL)
if soup:
    get_url(soup)
ALL_URLS=INSIDE_URLS+OUTSIDE_URLS
i_count=len(INSIDE_URLS)
o_counts=len(OUTSIDE_URLS)
print(f'Найдено уникальных внутренних ссылок на глубине 1 - {i_count}')
print(f'Найдено уникальных внешних ссылок на глубине 1 - {o_counts}')
for u in ALL_URLS:
    soup = make_soup(u)
    if soup:
        get_url(soup)

print(f'Найдено уникальных внутренних ссылок на глубине 2 - {len(INSIDE_URLS)-i_count}')
print(f'Найдено уникальных внешних ссылок на глубине 2 - {len(OUTSIDE_URLS)-o_counts}')

if args.write:
    with open(f'{START_URL[START_URL.find('//') + 2:]}.txt', 'w') as f:
        for i in OUTSIDE_URLS+INSIDE_URLS:
            f.write(i + '\n')
else:
    for i in OUTSIDE_URLS+INSIDE_URLS:
        print(i)



