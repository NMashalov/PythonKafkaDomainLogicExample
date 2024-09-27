from aiokafka.admin import AIOKafkaAdminClient, NewTopic



async def start():
    admin = AIOKafkaAdminClient(
        bootstrap_servers=['localhost:9092','localhost:9093','localhost:9094'],
        security_protocol='SASL_PLAINTEXT',
        sasl_mechanism='PLAIN',
        sasl_plain_username='admin',
        sasl_plain_password='admin_password',
    )
    await admin.create_topic(NewTopic(name='TEST',num_partitions=1,replication_factor=1))
