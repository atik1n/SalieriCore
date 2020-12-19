import salieri.integration as integration
import asyncio


async def main():
    print('\n---------\n'.join(await integration.run_all()))

if (__name__ == "__main__"):
    asyncio.run(main())
