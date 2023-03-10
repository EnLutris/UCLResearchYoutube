FROM python:3.10

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn app:app --host 0.0.0.0 
