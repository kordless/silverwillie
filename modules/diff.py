from willie import module
from willie import web
from willie.module import commands, example
import urllib2
import math

@commands('diff')
@example('.diff')
def diff(bot, trigger):
    content = urllib2.urlopen("http://litecoinscout.com/chain/Litecoin/q/nethash/1/-1")
    data = content.readlines()[-1].split(",")
    diff = float(data[4])
    say_string = "LTC Current Difficulty: %s | via http://litecoinscount.com" % (diff)
    bot.say(say_string)
