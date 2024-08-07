from time import sleep
import asyncio
async def ac():
    print("你好")
    for i in range(1,299):
        await print(i)

if __name__ == "__main__":
    asyncio(ac())