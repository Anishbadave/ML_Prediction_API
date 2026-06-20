# ML Prediction API

## Overview

This project is a Machine Learning Prediction API built using FastAPI, Scikit-learn, and SQLite.

The API accepts input features, generates predictions using a trained machine learning model, stores prediction results in a database, and provides endpoints to retrieve prediction history and statistics.

---

## Technology Stack

* Python 3.12
* FastAPI
* Scikit-learn
* SQLite
* Uvicorn
* Pydantic

---

## Project Structure

```text
ML_PREDICTION_API/
│
├── api/
│   └── app.py
│
├── models/
│   ├── model.pkl
│   └── train_model.py
│
├── database/
│   ├── db.py
│   ├── schema.sql
│   └── predictions.db
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Features

* Predict using trained ML model
* Return confidence score
* Store prediction history
* Retrieve all predictions
* Retrieve prediction by ID
* Calculate average confidence
* Count total predictions
* Delete prediction records

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ML_PREDICTION_API
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run API

```bash
uvicorn api.app:app --reload
```

API will run at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```http
GET /health
```

### Create Prediction

```http
POST /predict
```

Sample Request:

```json
{
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2
}
```

Sample Response:

```json
{
  "id": 1,
  "prediction": 0,
  "confidence": 1.0
}
```

### Get All Predictions

```http
GET /predictions
```

### Get Prediction By ID

```http
GET /prediction/{prediction_id}
```

### Get Average Confidence

```http
GET /average-confidence
```

### Get Statistics

```http
GET /stats
```

### Delete Prediction

```http
DELETE /prediction/{prediction_id}
```

---

## Database Schema

Table: predictions

| Column     | Type      |
| ---------- | --------- |
| id         | INTEGER   |
| input_data | TEXT      |
| prediction | TEXT      |
| confidence | REAL      |
| created_at | TIMESTAMP |

---

## Machine Learning Model

* Dataset: Iris Dataset
* Algorithm: Scikit-learn Classification Model
* Model File: model.pkl

---

## Author

Anish Badave
