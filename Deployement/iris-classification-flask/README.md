# Iris Classification Flask Project

This project is a Flask web application for classifying iris flowers based on their measurements. It utilizes a machine learning model trained on the Iris dataset to predict the species of iris flowers.

## Project Structure

```
iris-classification-flask
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── main.py              # Entry point for the application
│   ├── routes.py            # Defines the routes for the web application
│   ├── model
│   │   ├── iris_model.pkl    # Trained model for predictions
│   │   └── train_model.py    # Code for training the model
│   ├── utils
│   │   ├── data_preprocessing.py  # Functions for data preprocessing
│   │   ├── evaluation.py          # Functions for model evaluation
│   │   ├── exploration.py          # Functions for data exploration
│   │   └── tuning.py              # Functions for hyperparameter tuning
│   └── templates
│       ├── index.html             # HTML template for user input
│       ├── report_exploration.md   # Documentation for data exploration
│       ├── report_preprocessing.md  # Documentation for data preprocessing
│       ├── report_training.md       # Documentation for model training
│       ├── report_evaluation.md     # Documentation for model evaluation
│       └── report_tuning.md         # Documentation for hyperparameter tuning
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
└── Iris.csv                       # Dataset for training and testing
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd iris-classification-flask
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app/main.py
   ```

4. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage Guidelines

- Input the measurements of the iris flower (sepal length, sepal width, petal length, petal width) in the provided fields on the main page.
- Click the "Predict" button to get the predicted species of the iris flower.
- Explore the reports in the templates folder for detailed documentation on data exploration, preprocessing, model training, evaluation, and tuning.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.