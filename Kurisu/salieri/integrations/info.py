from .fake import *
from kurisu.cogs.fgl import FGL as Cog

name = "User info"

async def run():
    log = []
    cog = Cog(client)

    log += ['Передаём в бота ложное сообщение с установленными данными']
    await cog.info(cog, ctx)
    embed = ctx.messages[-1][1]['embed']

    log += ['Верно?']
    log += ['ID: %r' % (embed.fields[0].value == FakeUser.id)]
    log += ['Title: %r' % (embed.title == FakeUser.name)]
    log += ['Color: %r' % (str(embed.color) == "#ffffff")]

    return log
