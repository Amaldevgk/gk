from bs4 import BeautifulSoup
import requests

def get_rate(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    request = requests.get(url).content