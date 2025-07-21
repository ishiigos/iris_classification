// script.js
document.getElementById('iris-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = {
        sepal_length: form.sepal_length.value,
        sepal_width: form.sepal_width.value,
        petal_length: form.petal_length.value,
        petal_width: form.petal_width.value
    };
    // Change this URL to your Flask backend endpoint
    const apiUrl = 'https://your-flask-app-url.com/predict';
    document.getElementById('result').textContent = 'Predicting...';
    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        const result = await response.json();
        document.getElementById('result').textContent = 'Prediction: ' + result.prediction;
    } catch (err) {
        document.getElementById('result').textContent = 'Error: Could not get prediction.';
    }
});