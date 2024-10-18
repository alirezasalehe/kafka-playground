#!/bin/bash

echo ${MODE}

if [[ ${MODE} == "PRODUCER" ]]
then
  python /producer.py
elif [[ ${MODE} == "CONSUMER" ]]
then
  python /consumer.py
fi
