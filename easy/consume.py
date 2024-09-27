
from aiokafka import AIOKafkaConsumer
import asyncio



async def start():
    consumer = AIOKafkaConsumer(
        'Why',
        bootstrap_servers='localhost:9092'
    )
    async with consumer as c:
        async for message in c:
            print(message.value)




asyncio.run(start())
