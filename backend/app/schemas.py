from pydantic import BaseModel

class PredictionResponse(BaseModel):
    filename: str
    landmark_name: str
    landmark_id: int
