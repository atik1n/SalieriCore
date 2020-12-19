import kurisu.tips

name = "Tips"

def run():
    log = []
    kurisu.tips.init()

    log += ['Ищем слово Alpaca, ожидаем точное попадаение...']
    tip = kurisu.tips.search('Alpaca')
    log += ['Успешно? %r (Точно: %r, шанс: %.2f%%, дистанция: %s)' % (tip[0][0] == 1, *tip[0])]
    log += ['Верно? %r (%s)\n' % (tip[1] == "Альпака", tip[1])]

    log += ['Ищем слово krr, ожидаем неточное попадаение...']
    tip = kurisu.tips.search('krr', 0)
    log += ['Успешно? %r (Точно: %r, шанс: %.2f%%, дистанция: %s)' % (tip[0][0] == 0, *tip[0])]
    log += ['Верно? %r (%s)\n' % (tip[1] == "Керровская чёрная дыра", tip[1])]
    return log
