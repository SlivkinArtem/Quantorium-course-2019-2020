"""Парсинг табличных данных (+ пагинация)"""
import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    """Получение HTML-кода"""
    responce = requests.get(url)
    return responce.text


def refined(string):
    """Ex: $33,896.66 -> 33896.66"""
    return string.replace('$', '').replace(',', '')


def write_csv(dictionary):
    """Запись в csv"""
    with open('coinmarket.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((dictionary['name'],
                         dictionary['price'],
                         dictionary['market cap'],))


def get_data(html):
    """Получение данных с сайта"""
    soup = BeautifulSoup(html, 'lxml')
    table_rows = soup.find('tbody').find_all('tr')

    for row in table_rows:
        row_data = row.find_all('td')
        currency = row_data[2].find('a').find('p').text
        price = row_data[3].find('a').text
        market_cap = row_data[6].find('p').text

        data = {
            'name': currency,
            'price': refined(price),
            'market cap': refined(market_cap),
        }
        write_csv(data)


if __name__ == '__main__':
    get_data(get_html('http://coinmarketcap.com'))

