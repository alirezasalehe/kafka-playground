KAFKA_PRODUCER_CONFIG = {
    'bootstrap_servers': [
        'kafka:19092',
    ],
    'retries': 10,
    'client_id': 'Test',
    'value_serializer': lambda m: m.encode('utf-8'),
}

KAFKA_CONSUMER_CONFIG = {
    'bootstrap_servers': [
        'kafka:19092',
    ],
}
