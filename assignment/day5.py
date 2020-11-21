import requests
import os
from bs4 import BeautifulSoup

os.system('cls')


URL = "https://www.iban.com/currency-codes"


def extract_countries():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    table = soup.find('table', {'class': 'tablesorter'})
    tr_list = table.findAll('tr')[1:]
    return tr_list


def append_country_list():
    toBeReturned = []
    for tr in extract_countries():
        if str(tr.findAll('td')[1].string) != 'No universal currency':
            toBeReturned.append(
                [str(tr.findAll('td')[0].string), str(tr.findAll('td')[2].string)])
    return list(enumerate(toBeReturned))


def req_by_num():
    try:
        req = int(input('#: '))

        if req > len(country_currency) or req < 0:
            print('Choose a number from the list.')
            req_by_num()
        else:
            COUNTRY = country_currency[req][1][0]
            CURRENCY = country_currency[req][1][1]
            print(f'You chose {COUNTRY[0]+COUNTRY[1:].lower()}')
            print(f'The currency code is {CURRENCY}')

    except:
        print('That wasn\'t a number.')
        req_by_num()


def main():

    print('Hello! Please choose select a country by number:')

    for index, country in country_currency:
        print(f"# {index} {country[0]}")

    req_by_num()


country_currency = append_country_list()

main()
