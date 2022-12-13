FROM python:3.10-alpine

EXPOSE 5001

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY EmailForwarder/ .

CMD ["python", "./main.py"]