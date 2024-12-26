import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(int(round(1 / power, 2) * 10))
        print(f'Силач {name} поднял {i + 1} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    hercules_1 = asyncio.create_task(start_strongman('Ivan Muromets', 4))
    hercules_2 = asyncio.create_task(start_strongman('Alesha Popovich', 2))
    hercules_3 = asyncio.create_task(start_strongman('Dobryna Nikitich', 3))
    await hercules_1
    await hercules_2
    await hercules_3


asyncio.run(start_tournament())
