import asyncio
from aiokafka.admin import AIOKafkaAdminClient, NewTopic
from kafka.admin import KafkaAdminClient, NewTopic as OldNewTopic




async def start():
    admin = AIOKafkaAdminClient(
        bootstrap_servers=['localhost:9092','localhost:9093','localhost:9094'],
        security_protocol='SASL_PLAINTEXT',
        sasl_mechanism='PLAIN',
        sasl_plain_username='admin',
        sasl_plain_password='admin_password',
        api_version='2.4.0'
    )
    await admin.create_topics(
        [NewTopic(name='TEST',num_partitions=1,replication_factor=1)]
    )


def test():
    admin = KafkaAdminClient(
        bootstrap_servers=['localhost:9092','localhost:9093','localhost:9094'],
        security_protocol='SASL_PLAINTEXT',
        sasl_mechanism='PLAIN',
        sasl_plain_username='admin',
        sasl_plain_password='admin_password',
        api_version=(2,4,0)
    )

    admin.create_topics([
        OldNewTopic(name='TEST',num_partitions=1,replication_factor=1)
        ])

test()
#asyncio.run(start())