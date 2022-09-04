import bs4
import requests
import re


# KEYWORDS = ['дизайн', 'фото', 'web', 'python']# Я проверял по своим кейвордам, но оставлю и эти т.к. в тз сказано чтоб были именно эти кейворды
KEYWORDS = ['живых', 'фото', 'web', 'python']

HEADERS = {
    'Accept': 'image/avif,image/webp,*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8',
    'Referer': 'http://www.google.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}

base_url = 'https://habr.com'
url_ru = base_url + '/ru/all/'
response = requests.get(url_ru, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")
for art in articles:
    preview_text = art.find(class_ = "tm-article-snippet").text
    check_word = str(preview_text)
    for key in KEYWORDS:
        if key in check_word:
            data_art = art.find("time")
            text_data = str(data_art)
            pattern = r"\d+\-\d+\-\d+\,\s\d+\:\d+"
            result_sub = re.search(pattern, text_data)
            title_art = art.find(class_ = "tm-article-snippet__title-link").text
            link_art = art.find(class_ = "tm-article-snippet__title-link").attrs
            link_piece = link_art['href']
            print(f'''{result_sub.group()} - {title_art} - {base_url}{link_piece}''')


