import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    NUM_OF_BALLS = 5
    for n in range(1, NUM_OF_BALLS + 1):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {n} шар")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Алёша Попович", 3))
    task2 = asyncio.create_task(start_strongman("Добрыня Никитич", 4))
    task3 = asyncio.create_task(start_strongman("Илья Муромец", 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
