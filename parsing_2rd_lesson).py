import requests
from bs4 import BeautifulSoup

def get_html(url):
    responce = requests.get(url)
    #print(responce.status_code)
    return responce.text

def parse(html_code):
    soup = BeautifulSoup(html_code, 'lxml') #
    premiere_list = soup.find('div', class_= "prem_list").find_all('div', class_='premier_item')

    for movie in premiere_list:
        film_name = movie.find('div', class_= "text").find('span', class_="name_big").find('a').text
        film_description = movie.find('div', class_='text').find('span', class_="sinopsys").text
        #try:
            #rating = movie.find('span', class_="ajax_rating await_rating")
        #except:
           # rating = movie.find('span', class_="ajax_rating").find('i').find('u').text
        print(film_name)
        print(film_description)
        #print(rating)

if __name__ == '__main__':
    html = get_html('https://www.kinopoisk.ru/premiere/')
    parse(html)





