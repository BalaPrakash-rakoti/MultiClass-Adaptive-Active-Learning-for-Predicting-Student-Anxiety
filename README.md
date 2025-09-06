# Multi-Class Adaptive Active Learning for Predicting Student Anxiety
⚡ A Machine Learning framework to predict student anxiety levels (Low / Medium / High) using Adaptive Active Learning and Ensemble Models.
Helps educators with real-time analytics and early intervention for student mental health.

## 📌 Overview

🎓 Student anxiety is a critical issue that impacts academic performance and well-being.
This project introduces an adaptive multi-class classification system that:

- **Dynamically selects the most informative data points using Active Learning.**

- **Uses Ensemble methods (Stacking Classifier) for high accuracy.**

- **Provides real-time predictions for early intervention.**

## 🎯 Objectives

✔️ Improve accuracy & robustness of anxiety prediction.

✔️ Enable multi-class classification (Low, Medium, High).

✔️ Build a scalable & real-time solution for institutions.

✔️ Support data-driven educational decisions.

## 🧩 Methodology
Algorithm Accuracy
Logistic Regression      	0.60,
Naive Bayes              	0.52, 
K-Nearest Neighbors (KNN)	0.78, 
XGBoost	                   0.80, 
Random Forest	             0.82, 
Stacking Classifier       	0.86 ✅

## 🔑 Highlights:

- **Adaptive Active Learning → Iterative labeling for better accuracy.**

- **Stacking Ensemble → Combines multiple models into one strong classifier.**

- **Real-Time Analytics → Instant student anxiety insights.**

## ⚙️ System Requirements
💻 Hardware

Processor: Intel i3/i5+

RAM: 8 GB (minimum)

Storage: 128–160 GB

## 🛠️ Software

Language: Python 3.6+

Framework: Flask

Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, MySQL Connector

Frontend: HTML, CSS, Bootstrap, JavaScript

Database: MySQL (XAMPP)

## 📂 Project Structure
📦 student-anxiety-prediction

 ┣ 📂 static/         # CSS, JS, images
 
 ┣ 📂 templates/      # HTML templates
 
 ┣ 📂 model/          # Trained ML models
 
 ┣ 📂 dataset/        # Processed student dataset
 
 ┣ 📜 app.py          # Flask entry point
 
 ┣ 📜 requirements.txt# Dependencies
 
 ┗ 📜 README.md       # Documentation

## 🚀 How to Run the Project

1️⃣ Clone the repo

git clone https://github.com/yourusername/student-anxiety-prediction.git
cd student-anxiety-prediction


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Configure Database

Start XAMPP MySQL

Import dataset SQL file (if provided)

Update DB credentials in app.py

4️⃣ Run Flask app

python app.py


5️⃣ Open in Browser 🌐

http://127.0.0.1:5000/

## 📊 Results

🏆 Stacking Classifier achieved the best accuracy: 0.86

## 📈 Performance comparison:

Logistic Regression: 0.60

Naive Bayes: 0.52

KNN: 0.78

XGBoost: 0.80

Random Forest: 0.82

Stacking Classifier: 0.86 🎯

## ✨ Features

🔮 Multi-class prediction (Low, Medium, High)

⚡ Real-time analytics for early intervention

📊 Dashboard for educators & admins

🔒 Secure & scalable design

## 🔮 Future Enhancements

☁️ Cloud deployment for institutions

🤖 Deep Learning (LSTMs/Transformers) for better accuracy

📱 Mobile app for student self-assessment

⌚ IoT/Wearable integration for behavioral insights

## 🔥 This project demonstrates how AI can revolutionize education by supporting mental health through real-time, data-driven insights.
