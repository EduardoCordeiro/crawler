FROM python:3.9.0-slim

WORKDIR /cybsafe

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app"]