import time
import requests
import redis
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
pricekey = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
averagekey = "https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10"
pricedata = requests.get(pricekey)  
pricedata = pricedata.json() #here we got the live price of bitcoin in dollars

averagedata = requests.get(averagekey)  
avgminutes= averagedata.json()['Data']['Data']
sum = 0
average = 0
for min in avgminutes:
    sum += min['close']
average = sum / 10

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    cache.set('price', pricedata['price'])
    cache.set('average', average)
    return f"the live price of bitcoin is:  {pricedata['price']} and the average of the last 10 minutes is {average}"