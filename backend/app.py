from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Global variables
model = None
class_names = None
IMG_HEIGHT = 256
IMG_WIDTH = 256

# Plant disease class names (actual classes from your trained model)
CLASS_NAMES = [
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy'
]

def load_model():
    """Load the trained model"""
    global model, class_names
    try:
        model_path = os.path.join(os.path.dirname(__file__), '..', 'final_enhanced_plant_disease_model.h5')
        model = keras.models.load_model(model_path)
        class_names = CLASS_NAMES
        print(f"✅ Model loaded successfully with {len(class_names)} classes")
        return True
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False

def preprocess_image(image_file):
    """Preprocess the uploaded image"""
    try:
        # Read image
        image = Image.open(io.BytesIO(image_file.read()))
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Resize to model input size
        image = image.resize((IMG_WIDTH, IMG_HEIGHT))
        
        # Convert to numpy array and normalize
        img_array = np.array(image)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0
        
        return img_array
    except Exception as e:
        raise Exception(f"Error preprocessing image: {e}")

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Plant Disease Prediction API is running',
        'model_loaded': model is not None,
        'num_classes': len(class_names) if class_names else 0
    })

@app.route('/api/classes', methods=['GET'])
def get_classes():
    """Get all available plant disease classes"""
    if class_names is None:
        return jsonify({
            'status': 'error',
            'message': 'Model not loaded'
        }), 500
    
    return jsonify({
        'status': 'success',
        'classes': class_names,
        'count': len(class_names)
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    """Predict plant disease from uploaded image"""
    try:
        # Check if model is loaded
        if model is None:
            return jsonify({
                'status': 'error',
                'message': 'Model not loaded. Please restart the server.'
            }), 500
        
        # Check if image is in request
        if 'image' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No image file provided'
            }), 400
        
        image_file = request.files['image']
        
        # Check if file is empty
        if image_file.filename == '':
            return jsonify({
                'status': 'error',
                'message': 'Empty filename'
            }), 400
        
        # Preprocess image
        img_array = preprocess_image(image_file)
        
        # Make prediction
        predictions = model.predict(img_array, verbose=0)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = float(np.max(predictions[0]))
        
        # Get top 5 predictions
        top_5_idx = np.argsort(predictions[0])[-5:][::-1]
        top_5_predictions = [
            {
                'class': class_names[idx],
                'confidence': float(predictions[0][idx]),
                'percentage': f"{float(predictions[0][idx]) * 100:.2f}%"
            }
            for idx in top_5_idx
        ]
        
        # Parse the prediction to get plant and disease info
        predicted_class = class_names[predicted_class_idx]
        # Handle different separator patterns (_, __, ___)
        if '___' in predicted_class:
            parts = predicted_class.split('___')
        elif '__' in predicted_class:
            parts = predicted_class.split('__', 1)
        else:
            parts = predicted_class.split('_', 1)
        
        plant = parts[0].replace('_', ' ') if len(parts) > 0 else 'Unknown'
        disease = parts[1].replace('_', ' ') if len(parts) > 1 else 'Unknown'
        
        return jsonify({
            'status': 'success',
            'prediction': {
                'class': predicted_class,
                'plant': plant,
                'disease': disease,
                'confidence': confidence,
                'percentage': f"{confidence * 100:.2f}%",
                'is_healthy': 'healthy' in disease.lower()
            },
            'top_predictions': top_5_predictions,
            'confidence_threshold': 0.7,
            'reliable': confidence >= 0.7
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Detailed health check endpoint"""
    return jsonify({
        'status': 'success',
        'server': 'running',
        'model': {
            'loaded': model is not None,
            'classes': len(class_names) if class_names else 0,
            'input_shape': f"{IMG_HEIGHT}x{IMG_WIDTH}"
        }
    })

if __name__ == '__main__':
    print("🚀 Starting Plant Disease Prediction API...")
    print("📦 Loading model...")
    
    if load_model():
        print("✅ Server is ready!")
        print("🌐 API endpoints:")
        print("   - GET  /              : Home")
        print("   - GET  /api/health    : Health check")
        print("   - GET  /api/classes   : Get all classes")
        print("   - POST /api/predict   : Predict disease")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("❌ Failed to load model. Please check the model file.")
