# 🌸 Iris Species Classifier Application

This is a simple and interactive Flask web app that predicts the species of an Iris flower — *Setosa*, *Versicolor*, or *Virginica* — based on user-provided measurements. The app uses a trained machine learning model built with `scikit-learn` and is deployed on [Render](https://render.com).

---

## 🚀 Demo

🌐 **Live App**: [https://iris-classification-9rka.onrender.com](https://iris-classification-9rka.onrender.com)

---

## 🧠 Objective

The goal of this project is to demonstrate a complete machine learning workflow from data preprocessing and model training to deployment as a user-friendly web application. It serves as a beginner-friendly example of how to combine machine learning with web development.

---

## 🔧 Tools & Technologies

- **Frontend**: HTML, CSS (inline styling)
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn
- **Deployment**: Render
- **Others**: Jupyter Notebook (for model training), joblib (for model serialization)

---

## 📁 Dataset

- **Name**: Iris Flower Dataset
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
- **Kaggle**: [Iris dataset](https://www.kaggle.com/datasets/ishiigoswami/iris-flower-specifications/data)
- **Features**:
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- **Target**: Species (Setosa, Versicolor, Virginica)

---

## 📊 Features

✅ Predicts Iris flower species from user inputs  
✅ Clean and responsive web form  
✅ Uses a pre-trained ML model  
✅ Lightweight, fast, and easy to deploy  
✅ Hosted live with minimal setup on Render

---

## 💻 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/iris-species-classifier.git](https://github.com/ishiigos/iris_classification.git)
   cd iris-species-classifier
   python app.py
   ```
iris-species-classifier/
│
├── static/
│   └── background.jpg            # Optional background image (if used)
│
├── templates/
│   └── predict.html              # Frontend form for user input
│
├── irisClassification.ipynb      # Jupyter notebook for model training
├── app.py                        # Flask app file (core backend logic)
├── Procfile             
├── nb_model2.pkl                 # ML trained Model
├── Category_nb.pkl               # ML trained Model
├── requirements.txt              # Dependencies for running the app
└── README.md                     # Project documentation
