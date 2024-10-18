import time

from src.kafka import kafka_service

counter = 0
while True:
    kafka_service.send_event(f'Number {counter}')
    counter += 1
    time.sleep(0.3)
