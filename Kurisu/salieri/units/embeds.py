import kurisu.prefs
import discord

name = "Embeds"

def run():
    log = []

    log += ['Берём эмбед для ошибок...']
    embed = kurisu.prefs.Embeds.new('error')
    log += ["Успешно? %r" % (embed != False)]
    if embed != False:
        log += ["Верно? %r" % (embed.colour == discord.Colour.red())]

    log += ['\nБерём эмбед для предупреждений...']
    embed = kurisu.prefs.Embeds.new('alert')
    log += ["Успешно? %r" % (embed != False)]
    if embed != False:
        log += ["Верно? %r" % (embed.colour == discord.Colour.gold())]

    log += ['\nБерём эмбед для сообщений...']
    embed = kurisu.prefs.Embeds.new('normal')
    log += ["Успешно? %r" % (embed != False)]
    if embed != False:
        log += ["Верно? %r" % (embed.colour == discord.Colour.dark_red())]
    return log
