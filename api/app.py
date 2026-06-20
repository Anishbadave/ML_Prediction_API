import sqlite3
import json

from fastapi import FastAPI
import joblib
from pydantic import BaseModel

model = joblib.load("models/model.pkl")

app = FastAPI()

class IrisInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float


@app.get("/")
def home():
    return {"message": "ML Prediction API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: IrisInput):

    features = [[
        data.feature1,
        data.feature2,
        data.feature3,
        data.feature4
    ]]

    prediction = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0])

    conn = sqlite3.connect("database/predictions.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions
        (input_data, prediction, confidence)
        VALUES (?, ?, ?)
        """,
        (
            json.dumps(data.dict()),
            str(prediction),
            float(confidence)
        )
    )

    conn.commit()
    prediction_id = cursor.lastrowid
    conn.close()

    return {
        "id": prediction_id,
        "prediction": int(prediction),
        "confidence": float(confidence)
    }


@app.get("/predictions")
def get_predictions():

    conn = sqlite3.connect("database/predictions.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions")

    rows = cursor.fetchall()

    conn.close()

    return rows


@app.get("/average-confidence")
def average_confidence():

    conn = sqlite3.connect("database/predictions.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(confidence) FROM predictions"
    )

    avg_conf = cursor.fetchone()[0]

    conn.close()

    return {
        "average_confidence": avg_conf
    }
@app.get("/prediction/{prediction_id}")
def get_prediction(prediction_id: int):

    conn = sqlite3.connect("database/predictions.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM predictions WHERE id = ?",
        (prediction_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row 
@app.get("/stats")
def get_stats():

    conn = sqlite3.connect("database/predictions.db")
    cursor = conn.cursor()

    # Total predictions
    cursor.execute(
        "SELECT COUNT(*) FROM predictions"
    )
    total = cursor.fetchone()[0]

    # Count predictions by class
    cursor.execute(
        """
        SELECT prediction, COUNT(*)
        FROM predictions
        GROUP BY prediction
        """
    )

    class_counts = {
        row[0]: row[1]
        for row in cursor.fetchall()
    }

    conn.close()

    return {
        "total_predictions": total,
        "prediction_counts": class_counts
    }