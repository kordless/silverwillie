from willie import module
from willie import web
from willie.module import commands, example

@commands('power')
@example('.power 3000')
def power(bot, trigger):
    # grab intended power rate
    try:
        power = int(trigger.group(2))
    except:
        power = 1000

    # do the math
    power_ok = power/1000 * .08 * 24 * 30
    power_ca = power/1000 * .35 * 24 * 30

    # print
    say_string = "Estimated power costs per month | OK@$0.08: $%s | CA@$0.35: $%s" % (power_ok, power_ca)
    if power > 100000:
        say_string = "Mules gives %s a blank stare." % trigger.nick
    bot.say(say_string)
