import logging
import time

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable


class KafkaService:
    def __init__(self, producer_config, consumer_config):
        self.topic = 'test_topic'

        while True:
            try:
                self.producer = KafkaProducer(**producer_config)
                self.consumer = KafkaConsumer(**consumer_config)
            except NoBrokersAvailable:
                logging.warning("No kafka brokers available. retrying in 1 second...")
                time.sleep(1)
            else:
                break

    def send_event(self, message):
        future = self.producer.send(topic=self.topic, value=message)
        future.add_callback(self.__callback)
        future.add_errback(self.__errback)

    def consume(self):
        self.consumer.subscribe(topics=[self.topic,])
        try:
            while True:
                msg = self.consumer.poll(timeout_ms=1000)
                if not msg:
                    continue
                else:
                    logging.warning(f"Processing Kafka message: {msg}")
        finally:
            self.consumer.close()

    def __callback(self, value):
        logging.warning(f'Message send to kafka: {value}')

    def __errback(self, exception):
        logging.warning(f'Failed to send message to kafka: {exception}')
