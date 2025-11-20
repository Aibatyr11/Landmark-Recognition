from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from app import ml_model
from app.auth_routes import router as auth_router


app = FastAPI(title="🏰 Landmark Recognition API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # можно ограничить ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)

@app.post("/predict")
async def predict_landmark(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    name, landmark_id = ml_model.predict(image)
    return {"filename": file.filename, "landmark_name": name, "landmark_id": landmark_id}
