import torch
from torchvision import transforms, models
from PIL import Image
import pandas as pd
import os

# --- Пути ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "landmark_model.pth")
META_PATH = os.path.join(BASE_DIR, "landmark_model.csv")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --- Загружаем метаданные ---
meta_df = pd.read_csv(META_PATH)
meta_df = meta_df.drop_duplicates(subset=["landmark_name"]).reset_index(drop=True)

# Список классов
class_names = meta_df["landmark_name"].tolist()
num_classes = len(class_names)
id2name = {i: name for i, name in enumerate(class_names)}

print(f"✅ Загружено {num_classes} классов из CSV")


model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

# --- Трансформации изображений ---
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# --- Функция предсказания ---
def predict(image: Image.Image):
    tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(tensor)
        _, pred = torch.max(outputs, 1)
        pred_id = int(pred.item())
        name = id2name.get(pred_id, f"Unknown (ID={pred_id})")
    return name, pred_id