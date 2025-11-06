# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# # from sqlalchemy.orm import Session
# import ml_model
# # import models, schemas, database
# from PIL import Image
# import io
#
# app = FastAPI(title="🏰 Landmark Recognition API")
#
# # Разрешим доступ фронту
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# # models.Base.metadata.create_all(bind=database.engine)
#
# @app.post("/predict")  # убрали response_model
# async def predict_landmark(file: UploadFile = File(...)):
#     try:
#         print("📥 Получен файл:", file.filename)
#         image = Image.open(io.BytesIO(await file.read())).convert("RGB")
#         print("🖼 Изображение успешно открыто")
#         name, landmark_id = ml_model.predict(image)
#         print("✅ Предсказание:", name, landmark_id)
#
#         # Временно не сохраняем в базу
#         # record = models.Prediction(filename=file.filename, landmark_name=name)
#         # db.add(record)
#         # db.commit()
#         # db.refresh(record)
#
#         return {"filename": file.filename, "landmark_name": name, "landmark_id": landmark_id}
#
#     except Exception as e:
#         import traceback
#         print("❌ Ошибка:", e)
#         traceback.print_exc()
#         return {"error": str(e)}


from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import ml_model
from PIL import Image
import io

app = FastAPI(title="🏰 Landmark Recognition API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict_landmark(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")
        name, landmark_id = ml_model.predict(image)
        return {"filename": file.filename, "landmark_name": name, "landmark_id": landmark_id}
    except Exception as e:
        return {"error": str(e)}
