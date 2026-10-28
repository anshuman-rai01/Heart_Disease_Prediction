# Heart Disease Prediction API

Machine learning case study using the Kaggle heart disease dataset. The included notebook trains and evaluates a Random Forest classifier; `model.joblib` and `scaler.joblib` are the saved prediction artifacts.

## Run with Docker

```bash
docker build -t heart-disease-api .
docker run --rm -p 8000:8000 heart-disease-api
```

Open `http://localhost:8000/docs` to try the API interactively. The health route is `GET /`; predictions use `POST /predict` with all 13 input features (`age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`).

## GitHub Actions

The workflow in `.github/workflows/ci.yml` builds the Docker image, starts the API, and checks the health and prediction endpoints for pushes and pull requests to `master`.

## Training

Open `Heart_Dieses_Prediction.ipynb` in Jupyter or Google Colab. Keep the dataset CSV in the notebook's working directory when training. The notebook saves `model.joblib` and `scaler.joblib` for the API.
