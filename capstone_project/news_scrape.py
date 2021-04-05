import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','capstone_project.settings')
import django
django.setup()
import requests
from bs4 import BeautifulSoup
from news_app.models import Google, Bloomberg, Barron
requests.packages.urllib3.disable_warnings()

def news_scrape():
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.google.com/search?q=technology+stocks&tbm=nws&source=lnt&tbs=qdr:d&sa=X&ved=0ahUKEwjs8JXwpJ_vAhURLs0KHRryCsEQpwUIKQ&biw=1920&bih=937&dpr=1"
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    News = soup.find_all('div', attrs = {'class':'ZINbbc xpd O9g5cc uUPGi'})
    for article in News[0:3]:
        try:
            title = article.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).text
            raw_link = (article.find('a', href=True)['href'])
            link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
            description = article.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).text
            time = description.split(" · ")[0]
            google_headline = Google()
            google_headline.title = title
            google_headline.url = link
            google_headline.time = time
            google_headline.save()
        except:
            continue

    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.bloomberg.com/markets/sectors/information-technology"
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    News = soup.find_all('div', attrs={"class": "sector-related-content__item"})
    for article in News:
        try:
            main = article.find_all('a')[0]
            link = main['href']
            title = article.find('a').text
            time = article.find('time').text
            bloomberg_headline = Bloomberg()
            bloomberg_headline.title = title
            bloomberg_headline.url = link
            bloomberg_headline.time = time
            bloomberg_headline.save()
        except:
            continue

    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.barrons.com/topics/technology?mod=BOL_TOPNAV"
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, 'html.parser')
    News = soup.find_all('div', attrs={'class': 'style--grid--2cXhDDnR BarronsTheme--grid--2JEpTORq'})
    for item in News[1:4]:
        try:
            title = item.find('a').text
            time = item.find('div', attrs={'class': 'BarronsTheme--wrapper-1-0--2f3XwkpR'}).find('p', {'class': 'BarronsTheme--timestamp--3V5jp2-R BarronsTheme--TopicsArticle--1XIXBXRt BarronsTheme--zero-margin-timestamp--YIWqgHaW'}).text
            link = (item.find('a', href=True)['href'])
            barrons_headline = Barron()
            barrons_headline.title = title
            barrons_headline.url = link
            barrons_headline.time = time
            barrons_headline.save()
        except:
            continue
    return barrons_headline,bloomberg_headline,google_headline

if __name__ == '__main__':
    print('populating...')
    news_scrape()
    print('complete!')
