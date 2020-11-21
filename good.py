import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    'https://kr.indeed.com/취업?q=파이썬&limit=5&start=0')

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
pagination = indeed_soup.find('div', {'class': 'pagination'})
links = pagination.find_all('a')

pages = []

for link in links[:-1]:
    pages.append(int(link.string))

print(pages)
