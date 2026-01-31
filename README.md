# 📉 Customer Churn Prediction App

An end-to-end **Machine Learning web application** that predicts whether a customer is likely to churn, built using **Scikit-learn** and **Streamlit**, and deployed on **Streamlit Cloud**.

This project demonstrates a **production-style ML workflow** — from preprocessing and modeling to inference, logging, and deployment.

## 🚀 Live Demo

👉 (Add your Streamlit Cloud URL here once deployed)

## 🧠 Problem Statement

Customer churn is a major challenge for subscription-based businesses.  
This application predicts the **probability of customer churn** and helps businesses take **data-driven retention actions**.

## ✅ Features

- 📊 Predicts **churn probability**
- 🎯 Adjustable **business risk threshold**
- 🟢🟠🔴 Risk classification (Low / Medium / Very High)
- 📈 Probability progress visualization
- 🧾 Logs predictions with timestamp
- ⚙️ Uses **Scikit-learn Pipeline** (safe preprocessing + inference)
- 🌍 Deployed using **Streamlit Cloud**

## 🧩 Tech Stack

- **Python**
- **Streamlit** (Web UI)
- **Pandas**
- **Scikit-learn**
- **Joblib**

## 🏗️ Project Structure

```

customer-churn-app/
│
├── app.py # Streamlit application
├── requirements.txt # Project dependencies
│
├── model/
│ └── churn_model.pkl # Trained ML pipeline
│
└── logs/
├── predictions.csv # Logged predictions
└── .gitkeep

```

## 🧪 Machine Learning Details

- Model trained using **Scikit-learn**
- Full preprocessing handled via **Pipeline & ColumnTransformer**
- Categorical encoding + scaling done inside pipeline
- `predict_proba()` used for probability-based decisions
- Business logic separated from ML logic

## 🎛️ Business Logic

- Adjustable churn threshold via sidebar
- Helps simulate different retention strategies:
    - **Lower threshold** → aggressive retention
    - **Higher threshold** → conservative retention

## 📁 Prediction Logging

Each prediction logs:

- Input features
- Churn probability
- Risk level
- Timestamp

This enables:

- Model monitoring
- Future retraining
- Business analytics

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/customer-churn-app.git
cd customer-churn-app
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

## 🌍 Deployment

The app is deployed using **Streamlit Cloud**:

- GitHub repository connected
- `app.py` as entry point
- Automatic CI/CD on push

## 📌 Future Improvements

- SHAP-based explainability
- Feature importance visualization
- Authentication & user roles
- Model drift monitoring
- Database-based logging

## 👤 Author

**Meet Darbar**
Aspiring Machine Learning Engineer

## ⭐ Acknowledgements

- Scikit-learn documentation
- Streamlit community

---

> This project reflects **real-world ML engineering practices**, not just model training.
