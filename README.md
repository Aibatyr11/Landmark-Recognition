# 🏰 Landmark Recognition

## 🌍 Описание проекта

**Landmark Recognition** — это ML-проект, который определяет достопримечательность по фотографии.  
Модель обучена на сокращённой версии **Google Landmark Dataset v2 Micro**, содержащей ~26 000 изображений и ~3 000 классов.  

Пользователь загружает фото — и модель сообщает, **что это за достопримечательность**.  
Проект полностью реализован: от обучения модели в Google Colab до веб-интерфейса с **FastAPI + React + PostgreSQL**.
---
## 🚀 Функционал

- 🧠 Обучение нейросети (**ResNet18**) на изображениях достопримечательностей  
- 🗺️ Распознавание landmarks по загруженному фото  
- 🏷️ Отображение реального названия из `metadata.csv`  
- 💾 Сохранение и повторное использование модели (`landmark_model.pth`)  
- 🌐 Веб-интерфейс (React + Vite + TypeScript)  
- ⚙️ Бэкенд на FastAPI (Python)  
- 🧾 MongoDB для хранения истории и метаданных  

---


## ⚙️ Стек технологий

### 🧠 Machine Learning
- **PyTorch** — обучение модели  
- **TorchVision** — ResNet18, аугментации  
- **Pandas / NumPy** — анализ данных  
- **PIL / Matplotlib** — работа с изображениями  
- **Kaggle API** — загрузка датасета  

### 🧾 Backend
- **FastAPI** — REST API сервер  
- **Uvicorn** — ASGI сервер  
- **Python-Multipart** — приём файлов  
- **PostgreSQL** — база данных  

### 💻 Frontend
- **React + Vite + TypeScript** — быстрый интерфейс  
- **TailwindCSS** — стилизация  
- **Axios** — запросы к API  
- **React Dropzone / Input** — загрузка изображений  

---

