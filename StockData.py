import yfinance as yf
from selenium.webdriver.common.devtools.v85.tracing import start

ticker = input("enter the ticker: ")
from_data = input("enter the start date (YYYY-MM-DD):")
to_date = input("enter the end date (YYYY-MM-DD):")


stock_data = yf.download(ticker, start=from_data, end=to_date)
stock_data.to_csv("stock_data.csv")
print("Stock data written to stock_data.csv")