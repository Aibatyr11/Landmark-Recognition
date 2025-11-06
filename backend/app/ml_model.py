# import torch
# from torchvision import transforms, models
# from PIL import Image
# import pandas as pd
# import os
#
# # --- Абсолютные пути ---
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../backend
# MODEL_PATH = os.path.join(BASE_DIR, "landmark_model.pth")
# META_PATH = os.path.join(BASE_DIR, "metadata.csv")
#
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#
# # --- Модель ---
# model = models.resnet18(weights=None)
# model.fc = torch.nn.Linear(model.fc.in_features, 20)  # число классов = 20 (под твой датасет)
# model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
# model.to(device)
# model.eval()
#
# # --- Преобразование изображений ---
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
# ])
#
# # --- Загрузка метаданных ---
# # Учитываем возможный разделитель `;` и BOM
# meta_df = pd.read_csv(META_PATH, sep=";", encoding="utf-8-sig")
# meta_df.columns = meta_df.columns.str.strip()  # Убираем лишние пробелы
#
# print("✅ CSV columns:", meta_df.columns.tolist())
#
# # Преобразуем в словарь id -> name
# label_map = dict(zip(meta_df["landmark_id"], meta_df["name"]))
#
# # --- Функция предсказания ---
# def predict(image: Image.Image):
#     tensor = transform(image).unsqueeze(0).to(device)
#     with torch.no_grad():
#         outputs = model(tensor)
#         _, pred = torch.max(outputs, 1)
#         pred_id = int(pred.item())
#         name = label_map.get(pred_id, f"Unknown (ID={pred_id})")
#     return name, pred_id
import torch
from torchvision import transforms, models
from PIL import Image
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "landmark_model.pth")
META_PATH = os.path.join(BASE_DIR, "metadata.csv")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Модель
model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, 20)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

# Преобразования
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Метаданные
meta_df = pd.read_csv(META_PATH, sep=";", encoding="utf-8-sig")
label_map = dict(zip(range(len(meta_df)), meta_df["name"]))  # ключ — индекс класса

def predict(image: Image.Image):
    tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(tensor)
        _, pred = torch.max(outputs, 1)
        pred_id = int(pred.item())
        name = label_map.get(pred_id, f"Unknown (ID={pred_id})")
    return name, pred_id
