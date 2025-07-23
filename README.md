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
## 💻 Project structure
<pre>
iris-species-classifier/
│
├── static/
│   └── background.jpg            # Optional background image used in the UI
│
├── templates/
│   └── predict.html              # HTML form for user input and prediction display
│
├── irisClassification.ipynb     # Jupyter notebook for training the classification model
├── app.py                        # Flask app with route and prediction logic
├── Procfile                      # Required for deploying on platforms like Render/Heroku
├── nb_model2.pkl                 # Serialized scikit-learn model (Naive Bayes or similar)
├── Category_nb.pkl               # Label encoder or category encoder used with the model
├── requirements.txt              # List of Python dependencies
└── README.md                     # Project documentation (this file)
</pre>

## 🛠️ Future Enhancements
<ul>
  <li>Add prediction confidence scores</li>
  <li>Support batch uploads (CSV input)</li>
  <li>Improve UI/UX with CSS frameworks like Bootstrap or Tailwind</li>
  <li>Enable logging and error tracking</li>
  <li>Convert to a REST API with JSON input/output support</li>
  <li>Integrate model explainability with SHAP or LIME</li>
  <li>Dockerize for scalable deployment</li>
</ul>

## 🙏 Acknowledgements
<ul>
  <li>
    <strong>Dataset:</strong> 
    <a href="https://archive.ics.uci.edu/dataset/53/iris" target="_blank">
      UCI Machine Learning Repository – Iris Data Set
    </a> (Public Domain)
  </li>
  <li><strong>Author:</strong> R.A. Fisher, 1936</li>
  <li><strong>Tools Used:</strong> Flask, Scikit-learn, Jupyter, Render</li>
  <li><strong>Deployed with:</strong> <a href="https://render.com" target="_blank">Render</a></li>
</ul>
