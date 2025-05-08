FROM python:3.9-slim

RUN apt-get update && apt-get install -y gcc libssl-dev libffi-dev wget unzip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "read.py"]

