FROM python:3.8-slim
USER root
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 22 8080
CMD ["python", "backend/api.py"]
