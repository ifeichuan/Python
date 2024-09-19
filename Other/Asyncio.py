import asyncio

async def hello(str):
    print('泥嚎~'+str)
    await asyncio.sleep(1) #模拟耗时操作
    print("你吃不吃火龙果？")

async def main():
    await asyncio.gather(
        hello("XS"),
        hello("猫猫"),
    )

asyncio.run(main())