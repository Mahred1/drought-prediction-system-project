from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Drought Prediction API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
try:
    model = joblib.load("backend/drought_model.joblib")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

class PredictionRequest(BaseModel):
    rainfall: float
    temperature: float
    soil_moisture: float
    ndvi: float

class PredictionResponse(BaseModel):
    drought_risk_level: str
    risk_score: int
    message: str

def get_risk_label(score):
    if score == 0: return "Low"
    if score == 1: return "Moderate"
    if score == 2: return "High"
    return "Severe"

@app.get("/")
def read_root():
    return {"message": "Drought Prediction API is running. use POST /predict"}

@app.post("/predict", response_model=PredictionResponse)
def predict_drought(request: PredictionRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    # Prepare input for model
    input_data = np.array([[
        request.rainfall, 
        request.temperature, 
        request.soil_moisture, 
        request.ndvi
    ]])
    
    try:
        prediction = model.predict(input_data)[0]
        # Since our synthetic model returns 0,1,2,3, we map it back
        risk_label = get_risk_label(prediction)
        
        # Simple message generation
        messages = {
            "Low": "Conditions stand favorable. Low risk of drought.",
            "Moderate": "Warning signs detected. Monitor conditions closely.",
            "High": "High likelihood of drought. Preparedness measures recommended.",
            "Severe": "Critical drought conditions predicted. Immediate action required."
        }
        
        return {
            "drought_risk_level": risk_label,
            "risk_score": int(prediction),
            "message": messages.get(risk_label, "Unknown status")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
