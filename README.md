# 🏠 AI House Rent Prediction System

<p align="center">
An end-to-end Machine Learning web application that predicts monthly house rent based on multiple property features using a Scikit-learn Pipeline, Flask, and Python.
</p>

---

## 🌐 Live Demo

🚀 **Live Website:** https://ai-rent-predictor.onrender.com/

---

## 📌 Project Overview

Finding the estimated rent for a property can be difficult because it depends on multiple factors such as location, property size, furnishing status, number of bedrooms, bathrooms, and floor details.

This project uses a Machine Learning model trained on real-world housing data to estimate monthly house rent based on user inputs. The trained model is integrated with a Flask web application and deployed on Render for real-time predictions.

---

## ✨ Features

- 🏠 Predict monthly house rent instantly
- 📊 Machine Learning based prediction
- 🌆 City-wise rent estimation
- 🛋 Furnishing status support
- 📐 Property size based prediction
- 🚿 Bathroom and BHK support
- 🏢 Current Floor & Total Floors support
- 🌐 Clean and responsive web interface
- 🚀 Live deployment on Render

---

## 🧠 Machine Learning Workflow

- Data Cleaning & Preprocessing
- Feature Engineering
- One-Hot Encoding for categorical features
- Pipeline using Scikit-learn
- Linear Regression Model
- Model Serialization using Joblib
- Flask Integration
- Deployment on Render

---

## 📊 Input Features

The model predicts rent using the following property details:

| Feature | Description |
|---------|-------------|
| BHK | Number of Bedrooms |
| Size | Property Size (sq ft) |
| Area Type | Super Area / Carpet Area / Built Area |
| City | Property Location |
| Furnishing Status | Furnished / Semi-Furnished / Unfurnished |
| Bathrooms | Number of Bathrooms |
| Current Floor | Floor on which property is located |
| Total Floors | Total floors in the building |

---

## 🛠 Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Backend
- Flask

### Frontend
- HTML5
- CSS3

### Deployment
- Render

### Model Serialization
- Joblib

---

## 📂 Project Structure

```
AI-Rent-Predictor
│
├── app.py
├── rent_prediction_model.pkl
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── images/
├── notebook/
│   └── Professional_Rent_Predictor_V2.ipynb
└── README.md
```

---

## 🚀 Run Locally

### Clone the repository

```bash
git clone https://github.com/SnehaVerma16/AI-Rent-Predictor.git
```

### Move into the project directory

```bash
cd AI-Rent-Predictor
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📈 Future Improvements

- 📍 Location-based price prediction using latitude & longitude
- 🗺 Integration with Maps API
- 🤖 Experiment with XGBoost and CatBoost models
- 📊 Prediction confidence score
- 📱 Mobile-first responsive UI
- ☁ Cloud database for storing prediction history

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- End-to-End Machine Learning Workflow
- Data Preprocessing
- Feature Encoding
- Scikit-learn Pipelines
- Linear Regression
- Model Deployment
- Flask Web Development
- Render Deployment
- Git & GitHub

---

## 👩‍💻 Author

**Sneha Verma**

Aspiring AI & Machine Learning Engineer

- GitHub: https://github.com/SnehaVerma16
- LinkedIn: *(Add your LinkedIn profile here)*

---

### ⭐ If you found this project interesting, consider giving it a star!
