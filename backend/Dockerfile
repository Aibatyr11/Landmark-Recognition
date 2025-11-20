FROM python:3.10-slim

WORKDIR /app

# Установим зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЮ папку app/ внутрь контейнера
COPY app ./app

# Копируем ML файлы
COPY landmark_model.pth .
COPY landmark_model.csv .

# Запускаем FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
