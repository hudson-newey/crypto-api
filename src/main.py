from flask import Flask, request, Response
import requests
import re

from static import BASE_URL, PRICE_RE, VOLUME_RE, CHANGE_RE, INIT_MESSAGE
from util import getDate, getTimeHour, getTimeMinute

app = Flask(__name__)

def toJSON(coin = None, price = None, volume = None, change = None) -> str:
  return (
          "{ \"coin\": \"" +
          str(coin) +
          "\", \"date\": \"" +
          getDate() + "\", \"timeHour\": \"" +
          getTimeHour() +
          "\", \"timeMinute\": \"" +
          getTimeMinute() +
          "\", \"price\": \"" +
          str(price) +
          "\", \"volume\": \"" +
          str(volume) +
          "\", \"change\": \"" +
          str(change) +
          "\" }"
        )

@app.route('/')
def root() -> str:
  requestedCrypto = request.args.get("v")

  if requestedCrypto == None: return "Malformed GET Request"

  requestURL = f"{BASE_URL}{requestedCrypto}"

  try:
    exchange = requests.get(requestURL)
  except:
    return "Failed to fetch remote exchange website"

  htmlContent = exchange.text

  exchangePrice = re.findall(PRICE_RE, htmlContent)[0].replace("Bitcoin is USD $", "").replace(",", "")
  exchangeVolume = re.findall(VOLUME_RE, htmlContent)[0].replace("volume of $", "").replace(",", "")
  exchangeChange = re.findall(CHANGE_RE, htmlContent)[0].replace("% in the last 24 hours", "").replace(",", "")

  returnContent = toJSON(requestedCrypto, exchangePrice, exchangeVolume, exchangeChange)
  returnType = "application/json"

  return Response(returnContent, mimetype=returnType)

if __name__ == "__main__":
  print(INIT_MESSAGE)
  app.run()
