import numpy as np
import os
from flask import Flask, request, render_template
from keras.models import load_model
from keras.utils import load_img, img_to_array

app = Flask(__name__)

# Loading the model
model = None
model_path = os.path.join(os.path.dirname(__file__), "vegetable_classification.h5")
if os.path.exists(model_path):
    model = load_model(model_path, compile=False)
    print("Model loaded successfully!")
else:
    print(f"Warning: Model file not found at {model_path}")
    print("Please train the model using the Jupyter notebook first.")

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

@app.route('/result', methods=["GET", "POST"])
def res():
    if request.method == "POST":
        if model is None:
            return render_template('prediction.html', pred="Model not loaded! Please train the model first.")
        
        f = request.files['image']
        basepath = os.path.dirname(__file__)  # Getting the current path i.e where app.py is present
        filepath = os.path.join(basepath, 'uploads', f.filename)  # Store anywhere in the system we can give image but we want that in uploads folder
        f.save(filepath)
        
        # Reading Image
        img = load_img(filepath, target_size=(299, 299))
        img_arr = img_to_array(img)
        
        # Expanding Dimensions
        img_input = np.expand_dims(img_arr, axis=0)
        
        # Predicting the higher probability index
        pred = np.argmax(model.predict(img_input))
        
        # Class mapping
        op = {
            0: 'Bean', 
            1: 'Bitter_Gourd', 
            2: 'Bottle_Gourd', 
            3: 'Brinjal', 
            4: 'Broccoli', 
            5: 'Cabbage', 
            6: 'Capsicum', 
            7: 'Carrot', 
            8: 'Cauliflower', 
            9: 'Cucumber', 
            10: 'Papaya', 
            11: 'Potato', 
            12: 'Pumpkin', 
            13: 'Radish', 
            14: 'Tomato'
        }
        
        result = op[pred]
        return render_template('prediction.html', pred=result)

""" Running our application """
if __name__ == "__main__":
    app.run(debug=True)
