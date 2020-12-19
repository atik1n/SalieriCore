from .integrations import *

async def run(test):
    log = []
    log += ['Тест "%s"' % test.name]
    log += await test.run()
    return '\n'.join(log)

async def run_all():
    res = []
    res += [await run(tips)]
    res += [await run(info)]
    return res