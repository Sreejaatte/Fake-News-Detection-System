from fastapi import APIRouter
from app.schemas.request import NewsRequest
from app.services.prediction_service import predict_news

router = APIRouter()

@router.post("/predict")
def predict(req: NewsRequest):
    return {"prediction": predict_news(req.text)}
