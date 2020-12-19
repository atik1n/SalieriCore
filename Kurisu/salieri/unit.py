from .units import *

def run(test):
    log = []
    log += ['Тест "%s"' % test.name]
    log += test.run()
    return '\n'.join(log)

def run_all():
    res = []
    res += [run(tips)]
    res += [run(nyaa)]
    res += [run(embeds)]
    return res