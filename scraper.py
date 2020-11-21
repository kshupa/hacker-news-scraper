import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
links2 = soup2.select('.storylink')

subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

megalinks = links + links2
megasubtext = subtext + subtext2

def sorted_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def custom_news(links, subtext):
    titles = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                titles.append({'title': title, 'link': href, 'votes': points})
    return sorted_by_votes(titles)


pprint.pprint(custom_news(megalinks, megasubtext))