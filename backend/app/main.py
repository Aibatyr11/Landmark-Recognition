from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import ml_model

app = FastAPI(title="🏰 Landmark Recognition API")

# Разрешим фронту обращаться к API
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