from willie import module
from willie import web
from willie.module import commands, example
import urllib2
import math

@commands('calc')
@example('.calc 3000')
def calc(bot, trigger):
    # price
    import btceapi
    try:
        connection = btceapi.BTCEConnection()
        ticker = btceapi.getTicker("ltc_usd", connection)
        last = getattr(ticker, "last")
        avg = getattr(ticker, "avg")

        # diff and block count
        content = urllib2.urlopen("http://litecoinscout.com/chain/Litecoin/q/nethash/1/-1")
        data = content.readlines()[-1].split(",")
        diff = float(data[4])
        blockscount = float(data[0])
    except:
        say_string = "Either litecoinscount.com or BTC-e is ignoring my requests. Wait a few and try again."
        bot.say(say_string)
        return

    # grab intended hash rate
    parms = trigger.group(2)
    parms = parms.split("@")
      
    try:
        hashrate = int(parms[0]) * 1000
    except:
        hashrate = 1000*1000 # 1000KH/s

    try:
        diff = int(parms[1])
    except:
        pass
  
    # do the math
    target = 0x00000000ffff0000000000000000000000000000000000000000000000000000 / diff
    time_per_block = math.pow(2,256)/(target*hashrate)
    secsinyear = 86400 * 365
    time_per_block = math.pow(2,256)/(target*hashrate)
    coinsperblock = 50.0 / (2 ** int((blockscount + 1) / 840000))
    revenue = secsinyear / time_per_block * coinsperblock

    # clean up and convert
    yrrevenue = revenue
    yrinusdollars = int(revenue) * last

    # print
    say_string = "Calculating return with %sKH/s with %s difficulty using last trade of LTC: US$%s | US$%s/yr (%s LTC) | US$%s/month (%s LTC) | US$%s/week (%s LTC) | US$%s/day (%s LTC) | This calculation brought to you by kordless: BF4 promo codes for 2 LTC: http://goo.gl/zRrmTT" % (hashrate/1000, diff, round(last, 2), round(yrinusdollars,2), round(yrrevenue,4), round(yrinusdollars/12,2), round(yrrevenue/12,4), round(yrinusdollars/52,2), round(yrrevenue/52,4), round(yrinusdollars/365,2), round(yrrevenue/365,4))

    if hashrate/1000 > 100000:
        say_string = "Mules gives %s a blank stare." % trigger.nick

    bot.say(say_string)
