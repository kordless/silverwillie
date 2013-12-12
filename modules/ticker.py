from willie import module
from willie import web
from willie.module import commands, example
import urllib2
import math

@commands('ticker')
@example('.ticker')
def ticker(bot, trigger):
    import btceapi
    connection = btceapi.BTCEConnection()
    ticker = btceapi.getTicker("ltc_usd", connection)
    avg = getattr(ticker, "avg")
    last = getattr(ticker, "last")
    vol = getattr(ticker, "vol_cur")
    say_string = "LTC/USD Average: $%s | LTC/USD Last Trade: $%s | Current LTC/USD Volume: %s | via http://btc-e.com" % (avg, last, vol)
    bot.say(say_string)

