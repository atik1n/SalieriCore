from .fake import *
from kurisu.cogs.steins import SteinsGate as Cog
import kurisu.tips

name = "Tips & embeds"

async def run():
    log = []
    kurisu.tips.init()
    cog = Cog(client)

    async def search(log, word, correct, sg = 1):
        log += ['Ищем %s, будто у бота...' % word]
        try:
            if sg:
                await cog.tips(cog, ctx, word)
            else:
                await cog.tips0(cog, ctx, word)
            embed = ctx.messages[-1][1]['embed']
            found_word = embed.fields[0].name
            log += ['Успешно? True']
            log += ['Верно? %r (%s)' % (found_word == correct, found_word)]
        except:
            log += ['Успешно? False']
        log += ['']

        ctx.reset()

    await search(log, 'Alpaca', 'Альпака')
    await search(log, 'krr', 'Керровская чёрная дыра', 0)

    return log
