from flask import Flask, request
import requests
import re

from static import *

app = Flask(__name__)

def toJSON(coin = None, price = None, volume = None, change = None):
  return "{ coin: \"" + str(coin) + "\", price: " + str(price) + ", volume: " + str(volume) + ", change: " + str(change) + " }"

@app.route('/')
def root():
  requestedCrypto = request.args.get("v")

  if requestedCrypto == None: return "Malformed GET Request"

  requestURL = f"{BASE_URL}{requestedCrypto}"

  try:
    exchange = requests.get(requestURL)
  except:
    return "Failed to fetch remote exchange website"
  
  htmlContent = exchange.text
  print(htmlContent)

  exchangePrice = re.findall(PRICE_RE, htmlContent)[0].replace("Current price of Bitcoin is USD $", "")
  exchangeVolume = re.findall(VOLUME_RE, htmlContent)[0].replace("24-hour trading volume of $", "")
  exchangeChange = re.findall(CHANGE_RE, htmlContent)[0].replace("price is up ", "").replace("% in the last 24 hours.", "")

  return toJSON(requestedCrypto, exchangePrice, exchangeVolume, exchangeChange)

if __name__ == "__main__":
  app.run()
