📌 Overview

This project introduces a multi-class adaptive active learning framework for predicting student anxiety levels. Traditional models struggle with limited labeled data and static learning, which reduces their accuracy and usefulness in real-world educational settings. Our adaptive framework dynamically selects informative samples for labeling, integrates multiple machine learning classifiers, and provides real-time anxiety prediction with higher accuracy.

By differentiating between multiple levels of anxiety (low, medium, high), this system can support early interventions, enhance student well-being, and contribute to educational data mining and mental health analytics.

🎯 Objectives

Improve accuracy and robustness of student anxiety prediction.

Address limitations of static models by leveraging adaptive active learning.

Enable multi-class classification for nuanced anxiety level detection.

Provide a scalable and real-time solution for educational environments.

🧩 Methodology

The framework integrates multiple algorithms and ensemble learning:

K-Nearest Neighbors (KNN) – Accuracy: 0.78

Logistic Regression – Accuracy: 0.60

XGBoost (XGBClassifier) – Accuracy: 0.80

Naive Bayes – Accuracy: 0.52

Random Forest – Accuracy: 0.82

Decision Tree Classifier – Baseline classifier

Stacking Classifier (Ensemble) – Best Accuracy: 0.86

Key Features:

Adaptive Active Learning: Iteratively selects most informative unlabeled data points.

Stacking Ensemble: Combines multiple models for robust performance.

Real-time analytics: Predictions can be generated instantly for intervention.

Comprehensive Data Integration: Incorporates academic, behavioral, and psychometric data.

⚙️ System Requirements
Hardware

Processor: Intel i3/i5+

RAM: 8 GB

Storage: 128–160 GB

Software

Language: Python 3.6+

Libraries: Flask, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, MySQL Connector, OS

IDE: PyCharm / VS Code

Database: MySQL (via XAMPP)

Frontend: HTML, CSS, Bootstrap, JavaScript

📂 Project Structure
├── /static/           # CSS, JS, images  
├── /templates/        # HTML templates for UI  
├── app.py             # Flask application entry point  
├── model/             # Trained models and ML pipeline  
├── dataset/           # Student data (processed)  
├── requirements.txt   # Python dependencies  
└── README.md          # Project documentation  

🚀 How to Run the Project

Clone the repository

git clone https://github.com/yourusername/student-anxiety-prediction.git
cd student-anxiety-prediction


Install dependencies

pip install -r requirements.txt


Configure the Database

Set up MySQL using XAMPP.

Import the provided SQL file (if available).

Update credentials in app.py.

Run the Flask app

python app.py


Open in Browser

http://127.0.0.1:5000/

📊 Results

Logistic Regression: 0.60

Naive Bayes: 0.52

KNN: 0.78

XGBoost: 0.80

Random Forest: 0.82

Stacking Classifier: 0.86 (Best)

📌 Features

Multi-class prediction (Low, Medium, High anxiety).

Real-time analytics for interventions.

Educator/Admin dashboard for insights.

Secure and scalable design.

🔮 Future Enhancements

Deploy as a cloud-based service for institutions.

Integrate deep learning models for improved performance.

Incorporate wearable/IoT data for richer behavioral insights.

Mobile application for student self-assessment.

👉 This project demonstrates the potential of AI in education, combining machine learning and adaptive frameworks to support student mental health proactively.
