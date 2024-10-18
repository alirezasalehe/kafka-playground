FROM python:3.9.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ARG MODE

RUN chmod +x ./docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]
