from flask import Flask, request, render_template
import pandas as pd
import pickle
from app.utils.data_preprocessing import preprocess_input

app = Flask(__name__)

# Load the trained model
with open('app/model/iris_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # Preprocess the input data
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                               columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    processed_data = preprocess_input(input_data)

    # Make prediction
    prediction = model.predict(processed_data)
    predicted_class = prediction[0]

    return render_template('index.html', prediction=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)