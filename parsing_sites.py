import requests
from bs4 import BeautifulSoup


def get_html(url):
    html_code = requests.get(url)
    return html_code.text


def get_data(code):
    soup = BeautifulSoup(code, 'lxml')
    content = soup.find('div', class_="site-branding")
    kartoshka = content.find_all('p')
    header = kartoshka[1].text
    print(header)

get_data(get_html('https://ru.wordpress.org'))



# print(get_html('https://ru.wordpress.org'))
