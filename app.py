from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and category encoder
model = joblib.load("nb_model2.pkl")
categories = joblib.load("Category_nb.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Extract form values
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        # Make prediction
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(features)[0]
        predicted_species = categories[int(prediction)]

        return render_template("predict.html", prediction=predicted_species)
    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)