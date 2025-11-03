FROM python:3.10-slim

WORKDIR /app

# Copy requirements from root now
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from app directory
COPY app/ .

EXPOSE 5001

CMD ["python", "app.py"]