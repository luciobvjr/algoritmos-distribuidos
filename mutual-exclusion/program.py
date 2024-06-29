import zmq
import asyncio
from lamport_clock import LamportClock, Message

async def loop1():
    while True:
        print("Loop 1")
        await asyncio.sleep(1)

async def loop2():
    while True:
        print("Loop 2")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(loop1(), loop2())

# Run the main function
asyncio.run(main())
