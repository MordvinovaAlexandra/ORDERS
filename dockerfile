FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y git gunicorn3 postgresql nano \ 
    && pip3 install --upgrade pip \
    && pip3 install poetry
    
WORKDIR /usr/orders

COPY . .

RUN poetry install

EXPOSE 5000

CMD ["poetry", "run", "warehouse-ddd"]
