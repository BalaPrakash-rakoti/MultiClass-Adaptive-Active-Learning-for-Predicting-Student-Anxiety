🌟 Multi-Class Adaptive Active Learning for Predicting Student Anxiety
📌 Overview

This project introduces a multi-class adaptive active learning framework for predicting student anxiety levels.
Traditional models struggle with limited labeled data and static learning, which reduces their accuracy in real-world educational settings.

Our framework:
✅ Dynamically selects informative samples for labeling
✅ Integrates multiple ML classifiers with an ensemble model
✅ Provides real-time anxiety predictions with higher accuracy
✅ Differentiates between low, medium, and high anxiety levels

🎯 Objectives

🔹 Improve accuracy and robustness of student anxiety prediction

🔹 Leverage adaptive active learning instead of static models

🔹 Enable multi-class classification for nuanced anxiety detection

🔹 Provide a scalable, real-time solution for educational institutions

🧩 Methodology

We tested several algorithms and compared their performance:

Algorithm	Accuracy
Logistic Regression	0.60
Naive Bayes	0.52
K-Nearest Neighbors (KNN)	0.78
XGBoost	0.80
Random Forest	0.82
Stacking Classifier	0.86 ✅ Best

✨ Key Highlights:

Adaptive Active Learning → Iteratively improves with new labeled data

Stacking Ensemble → Combines multiple models for stronger performance

Real-time analytics → Instant results for timely interventions

Comprehensive data → Uses academic, behavioral & psychometric info

⚙️ System Requirements
💻 Hardware

Processor: Intel i3/i5+

RAM: 8 GB (minimum)

Storage: 128–160 GB

🛠️ Software

Language: Python 3.6+

Frameworks/Libraries: Flask, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, MySQL Connector

IDE: PyCharm / VS Code

Database: MySQL (XAMPP)

Frontend: HTML, CSS, Bootstrap, JavaScript

📂 Project Structure
├── /static/           # CSS, JS, images  
├── /templates/        # HTML templates (Flask)  
├── app.py             # Main Flask app  
├── model/             # Trained ML models  
├── dataset/           # Processed student dataset  
├── requirements.txt   # Python dependencies  
└── README.md          # Documentation  

🚀 How to Run the Project

1️⃣ Clone the repo

git clone https://github.com/yourusername/student-anxiety-prediction.git
cd student-anxiety-prediction


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Configure Database

Start XAMPP MySQL

Import dataset SQL file (if provided)

Update DB credentials in app.py

4️⃣ Run the Flask app

python app.py


5️⃣ Open in Browser

http://127.0.0.1:5000/

📊 Results

✅ Logistic Regression: 0.60
✅ Naive Bayes: 0.52
✅ KNN: 0.78
✅ XGBoost: 0.80
✅ Random Forest: 0.82
🏆 Stacking Classifier: 0.86 (Best)

✨ Features

🎯 Multi-class prediction (Low, Medium, High anxiety)

⚡ Real-time analytics for early intervention

📊 Dashboard for educators & admins

🔒 Secure and scalable design

🔮 Future Enhancements

☁️ Cloud deployment for institutions

🤖 Deep learning integration for higher accuracy

📱 Mobile app for student self-assessment

⌚ IoT/Wearable data integration

🔥 This project showcases how AI + Education can work together to support student mental health proactively!
