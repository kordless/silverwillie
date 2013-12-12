from willie import module
from willie import web
from willie.module import commands, example

@commands('blowjob')
def blowjob(bot, trigger):
    say_string = "I give the best blowjobs LTC can buy %s. Cum in my wallet today: LNxBAs7c4HaxSYJR21TxBEP5pjE2WS7Wbe" % trigger.nick
    bot.say(say_string)
