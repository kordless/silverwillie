from willie import module
from willie import web
from willie.module import commands, example

@commands('help')
def help(bot, trigger):
    say_string = "Usage: .<command> | Commands: .ticker, .diff, .calc <hashrate>"
    bot.say(say_string)

