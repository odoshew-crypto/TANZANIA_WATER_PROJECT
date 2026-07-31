# Tanzania Water Pump Status Prediction API
# IT RUNS PUBLICLY HERE ==> Available at your primary URL https://tanzania-water-project.onrender.com

A Machine Learning-powered REST API built with **FastAPI** to predict the operational status of water pumps in Tanzania. The project uses a trained classification model to determine whether a water point is:

- Functional
- Functional Needs Repair
- Non Functional

The API accepts water point characteristics and returns the predicted `status_group`.

---

## Project Structure

```
TANZANIA_WATER_PROJECT/
│
├── Models/
│   ├── best_model.joblib
│   └── label_encoder.joblib
│
├── Notebook/
│   └── o1_data.ml.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Dataset

This project is based on the **Tanzania Water Pumps Dataset**, which contains information about water points across Tanzania.

Target Variable:

- `status_group`

Possible predictions:

- Functional
- Functional Needs Repair
- Non Functional

---

## Technologies Used

- Python 3.12
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Uvicorn
- Pydantic

---

## Model Development

The machine learning workflow is implemented in:

```
Notebook/o1_data.ml.ipynb
```

The notebook includes:

- Data loading
- Data cleaning
- Feature engineering
- Exploratory Data Analysis (EDA)
- Feature selection
- Data preprocessing
- Model training
- Model evaluation
- Model selection
- Saving the trained model and label encoder

---

## Features Used

The API expects the following input features:

| Feature | Type |
|----------|------|
| amount_tsh | float |
| region | string |
| gps_height | integer |
| basin | string |
| population | integer |
| scheme_management | string |
| permit | boolean |
| extraction_type_class | string |
| payment_type | string |
| quantity | string |
| quality_group | string |
| source_type | string |
| waterpoint_type_group | string |
| month_recorded | integer |
| age | integer |

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/TANZANIA_WATER_PROJECT.git
```

Navigate to the project

```bash
cd TANZANIA_WATER_PROJECT
```

Create a virtual environment

```bash
python -m venv tzwater
```

Activate it

Windows

```bash
tzwater\Scripts\activate
```

Linux / macOS

```bash
source tzwater/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the FastAPI server

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoint

### POST `/predict`

Predicts the operational status of a water pump.

### Example Request

```json
{
  "amount_tsh": 5000,
  "region": "Kilimanjaro",
  "gps_height": 1390,
  "basin": "Pangani",
  "population": 350,
  "scheme_management": "VWC",
  "permit": true,
  "extraction_type_class": "gravity",
  "payment_type": "monthly",
  "quantity": "enough",
  "quality_group": "good",
  "source_type": "spring",
  "waterpoint_type_group": "communal standpipe",
  "month_recorded": 7,
  "age": 12
}
```

---

### Example Response

```json
{
  "status": "success",
  "predicted_status_group": "functional"
}
```

---

## Saved Models

The project saves two files after training:

### `best_model.joblib`

Contains the trained machine learning pipeline used for prediction.

### `label_encoder.joblib`

Used to convert encoded model outputs back into their original `status_group` labels.

---

## Model Evaluation

The notebook evaluates multiple classification algorithms, including:

- Logistic Regression
- Random Forest
- Decision Tree
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gradient Boosting
- XGBoost

The best-performing model is saved as `best_model.joblib`.

---

## Future Improvements

- Docker containerization
- Cloud deployment (Railway, Render, Azure, or AWS)
- Batch prediction endpoint
- Model monitoring
- Authentication and authorization
- CI/CD pipeline
- Automated retraining

---

## Author

**Wickliff Odoyo**

Data Analyst | Machine Learning Engineer | Backend Developer

---

## License

This project is intended for educational and research purposes.
