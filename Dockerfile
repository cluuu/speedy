FROM python:3

WORKDIR /usr/src/speedy

RUN apt-get update -o Acquire::Check-Valid-Until=false

RUN apt-get install -y cron

COPY requirements.txt /usr/src/speedy/requirements.txt
COPY speedy.py /usr/src/speedy/speedy.py

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "speedy.py"]