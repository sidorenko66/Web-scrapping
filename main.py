import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


if __name__ == "__main__":
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Python']
    headers = Headers(os="win", headers=True).generate()
    base_url = 'https://habr.com'
    text = requests.get(base_url + '/ru/all/', headers=headers).text
    soup = BeautifulSoup(text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        if list(filter(lambda x: x in article.text, KEYWORDS)):
            date = article.find('time')['title']
            title = article.find('h2').find('span').text
            link = article.find('h2').find('a')['href']
            print(f'{date} - {title} - {base_url + link}')
