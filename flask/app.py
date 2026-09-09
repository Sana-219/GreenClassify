import os
import tempfile

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Loading the model
model = None
model_path = os.path.join(os.path.dirname(__file__), "vegetable_classification.h5")
model_api_url = os.getenv("MODEL_API_URL", "").rstrip("/")

if os.getenv("LOAD_LOCAL_MODEL", "0") == "1":
    from keras.models import load_model

    if os.path.exists(model_path):
        model = load_model(model_path, compile=False)
        print("Model loaded successfully!")
    else:
        print(f"Warning: Model file not found at {model_path}")
        print("Please train the model using the Jupyter notebook first.")

class_names = {
    0: 'Bean', 1: 'Bitter_Gourd', 2: 'Bottle_Gourd', 3: 'Brinjal',
    4: 'Broccoli', 5: 'Cabbage', 6: 'Capsicum', 7: 'Carrot',
    8: 'Cauliflower', 9: 'Cucumber', 10: 'Papaya', 11: 'Potato',
    12: 'Pumpkin', 13: 'Radish', 14: 'Tomato'
}

# Default home page or route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction.html')
def prediction():
    return render_template('prediction.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/logout.html')
def logout():
    return render_template('logout.html')


@app.route('/health')
def health():
    return jsonify({"status": "ok", "model_loaded": model is not None})


@app.route('/predict', methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 503

    image = request.files.get('image')
    if image is None:
        return jsonify({"error": "An image file is required"}), 400

    from keras.utils import img_to_array, load_img
    import numpy as np

    with tempfile.NamedTemporaryFile(suffix=os.path.splitext(image.filename or "image.jpg")[1]) as uploaded:
        image.save(uploaded.name)
        img = load_img(uploaded.name, target_size=(224, 224))
        img_input = np.expand_dims(img_to_array(img), axis=0)
        pred = int(np.argmax(model.predict(img_input, verbose=0)))

    return jsonify({"prediction": class_names[pred]})

@app.route('/result', methods=["GET", "POST"])
def res():
    if request.method == "POST":
        image = request.files.get('image')
        if image is None:
            return render_template('prediction.html', pred="Please select an image.")

        if model_api_url:
            import requests

            response = requests.post(
                f"{model_api_url}/predict",
                files={"image": (image.filename, image.stream, image.mimetype)},
                timeout=60,
            )
            result = response.json().get("prediction", "Prediction unavailable") if response.ok else "Model service unavailable"
        elif model is None:
            result = "Model not loaded! Please train the model first."
        else:
            response = predict()
            result = response[0].get_json()["prediction"] if isinstance(response, tuple) else response.get_json()["prediction"]

        return render_template('prediction.html', pred=result)

""" Running our application """
if __name__ == "__main__":
    app.run(debug=True)
