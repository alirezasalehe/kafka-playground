import settings
from src.kafka.service import KafkaService


kafka_service = KafkaService(settings.KAFKA_PRODUCER_CONFIG, settings.KAFKA_CONSUMER_CONFIG)
