from bs4 import BeautifulSoup
import requests
import ipdb
import csv
from datetime import datetime

def get_crypto_prices():
    """Checks coinmarketcap.com for recent cryptocurrency prices

    Returns
    _______
    prices: dict
        A dict containing the name and price of cryptocurrencies
    """

    site = requests.get("https://coinmarketcap.com").content

    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(site, 'lxml')

    # Take out the <div> of name and get its value
    table_body=soup.find('tbody')
    title = table_body.find_all('tr')

    for i in title:
        names = i.find('a', attrs={'class': 'currency-name-container'})
        names = names.text.strip()
        prices = i.find('a', attrs={'class': 'price'})
        prices = prices.text.strip()

        with open('crypto.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([names, prices, datetime.now()])

