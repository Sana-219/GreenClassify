# GreenClassify: Deep Learning-Based Vegetable Image Classification

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10+-orange.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Project Overview

GreenClassify is a deep learning-based web application that accurately identifies and categorizes various types of vegetables using Convolutional Neural Networks (CNNs). The system analyzes input images of vegetables and classifies them into 15 predefined categories.

### 🎯 Key Features

- **Deep Learning Classification**: CNN model trained on 15,000+ vegetable images
- **15 Vegetable Categories**: Bean, Bitter Gourd, Bottle Gourd, Brinjal, Broccoli, Cabbage, Capsicum, Carrot, Cauliflower, Cucumber, Papaya, Potato, Pumpkin, Radish, Tomato
- **Web Interface**: User-friendly Flask-based web application
- **Real-time Prediction**: Instant classification results

## 🏗️ Technical Architecture

```
User → UI (Upload Image) → Flask App → CNN Model → Prediction → Display Result
```

### Model Architecture

| Layer | Type | Output Shape | Parameters |
|-------|------|--------------|------------|
| conv2d | Conv2D | (None, 150, 150, 32) | 896 |
| max_pooling2d | MaxPooling2D | (None, 75, 75, 32) | 0 |
| conv2d_1 | Conv2D | (None, 75, 75, 64) | 18,496 |
| max_pooling2d_1 | MaxPooling2D | (None, 37, 37, 64) | 0 |
| flatten | Flatten | (None, 87616) | 0 |
| dense | Dense | (None, 128) | 11,214,976 |
| dropout | Dropout | (None, 128) | 0 |
| dense_1 | Dense | (None, 128) | 16,512 |
| dense_2 | Dense | (None, 15) | 1,935 |

**Total Parameters**: 11,252,815

## 📁 Project Structure

```
Greenclassify/
├── flask/
│   ├── app.py                          # Flask application
│   ├── vegetable_classification.h5     # Trained model
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css              # Stylesheets
│   │   ├── js/
│   │   │   └── main.js                # JavaScript
│   │   └── img/                       # Images
│   ├── templates/
│   │   ├── index.html                 # Home page
│   │   ├── prediction.html            # Prediction page
│   │   └── logout.html                # Result page
│   └── uploads/                       # Uploaded images
├── notebooks/
│   └── vegetable_classification_training.ipynb  # Training notebook
├── requirements.txt                    # Dependencies
├── README.md                          # Documentation
└── LICENSE                            # License file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Anaconda Navigator (recommended)
- TensorFlow 2.10+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Greenclassify.git
   cd Greenclassify
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset** (for training)
   ```bash
   kaggle datasets download -d misrakahmed/vegetable-image-dataset
   ```

5. **Run the Flask application**
   ```bash
   cd flask
   python app.py
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 📊 Dataset

The model is trained on the [Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) from Kaggle:

- **Training Images**: 15,000
- **Validation Images**: 3,000
- **Test Images**: 3,000
- **Categories**: 15 vegetable types

## 🧠 Model Training

1. Open the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/vegetable_classification_training.ipynb
   ```

2. Follow the steps in the notebook:
   - Data Collection
   - Data Preprocessing
   - Model Building
   - Model Training
   - Model Evaluation
   - Save Model

## 🌐 Web Application

### Pages

1. **Home Page (index.html)**: Landing page with project information
2. **Prediction Page (prediction.html)**: Upload and classify vegetables
3. **Result Page (logout.html)**: Display classification results

### Usage

1. Navigate to the Prediction page
2. Click "Choose File" to select a vegetable image
3. Click "Submit" to classify
4. View the prediction result

## 📈 Use Cases

- **Automated Sorting**: Vegetable processing facilities can automate sorting
- **Quality Control**: Distributors can ensure consistent quality standards
- **Smart Inventory**: Retail stores can manage vegetable inventory efficiently

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Tejas**

## 🙏 Acknowledgments

- Kaggle for the Vegetable Image Dataset
- TensorFlow/Keras team for the deep learning framework
- Flask team for the web framework
