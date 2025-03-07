import faker
import time
import psycopg2
from datetime import datetime
from confluent_kafka import SerializingProducer
import random
import json

fake = faker.Faker()


def generate_transaction():
    user = fake.simple_profile()

    return {
        "transactionId": fake.uuid4(),
        "userId": user['username'],
        "timestamp": datetime.utcnow().timestamp(),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(['USD', 'GBP']),
        'city': fake.city(),
        "country": fake.country(),
        "merchantName": fake.company(),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer']),
        "ipAddress": fake.ipv4(),
        "voucherCode": random.choice(['', 'DISCOUNT10', '']),
        'affiliateId': fake.uuid4()
    }

def delivery_report(err, msg):
    if err is not None:
        print(f'message delivery failed {err}')
    else:
        print(f'message delivered to {msg.topic} {msg.partition()}')

if __name__ == '__main__':
    topic = "transaction-data"

    producer = SerializingProducer({
        'bootstrap.servers': 'localhost:9092'
    })

    for i in range(100):
        try:
            trx = generate_transaction()
            print(trx)

            producer.produce(
                topic=topic,
                key=trx['transactionId'],
                value=json.dumps(trx),
                on_delivery=delivery_report,
            )
            time.sleep(5)
        except Exception as e:
            print(e)