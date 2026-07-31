from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI(title="Tanzania Water Project")

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Model paths
MODEL_PATH = BASE_DIR / "Models" / "best_model.joblib"
LABEL_ENCODER_PATH = BASE_DIR / "Models" / "label_encoder.joblib"

# Load model and encoder
model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(LABEL_ENCODER_PATH)


class PredictionInput(BaseModel):
    amount_tsh: float
    region: str
    gps_height: int
    basin: str
    population: int
    scheme_management: str
    permit: bool
    extraction_type_class: str
    payment_type: str
    quantity: str
    quality_group: str
    source_type: str
    waterpoint_type_group: str
    month_recorded: int
    age: int


@app.get("/")
def home():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(status: PredictionInput):
    try:
        input_data = pd.DataFrame([{
            "amount_tsh": status.amount_tsh,
            "region": status.region,
            "gps_height": status.gps_height,
            "basin": status.basin,
            "population": status.population,
            "scheme_management": status.scheme_management,
            "permit": status.permit,
            "extraction_type_class": status.extraction_type_class,
            "payment_type": status.payment_type,
            "quantity": status.quantity,
            "quality_group": status.quality_group,
            "source_type": status.source_type,
            "waterpoint_type_group": status.waterpoint_type_group,
            "month_recorded": status.month_recorded,
            "age": status.age
        }])

        prediction = model.predict(input_data)

        predicted_status = label_encoder.inverse_transform(
            prediction.astype(int)
        )[0]

        return {
            "status": "success",
            "predicted_status_group": str(predicted_status)
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(error)}"
        )