from app.models.model_loader import load_model

model, vectorizer = load_model()

def predict_news(text: str):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)
    return "Fake" if pred[0] == 1 else "Real"
