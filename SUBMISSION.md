# Plant Disease Prediction System - Submission Package

## 📋 Project Overview

A full-stack web application that uses deep learning to predict plant diseases from leaf images. The system can identify 15 different disease conditions across 3 plant types (Pepper, Potato, and Tomato) with high accuracy.

## 🎯 Project Components

### 1. Machine Learning Model
- **Model Type**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow/Keras
- **Architecture**: Enhanced CNN with 4 convolutional blocks, batch normalization, and dropout
- **Input Size**: 256x256 RGB images
- **Output**: 15 classes (softmax activation)
- **Model File**: `final_enhanced_plant_disease_model.h5` (5.65 MB)

### 2. Backend API
- **Framework**: Flask
- **Features**: 
  - RESTful API endpoints
  - Image preprocessing
  - Model inference
  - CORS support for frontend integration
- **Endpoints**:
  - `GET /` - Health check
  - `GET /api/health` - Detailed status
  - `GET /api/classes` - List all classes
  - `POST /api/predict` - Predict disease from image

### 3. Frontend Application
- **Framework**: React
- **Features**:
  - Drag-and-drop image upload
  - Real-time prediction display
  - Confidence scoring visualization
  - Responsive design
  - Support for Pepper, Potato, and Tomato plants

## 📊 Model Performance

### Training Configuration
- **Epochs**: 10
- **Batch Size**: 32
- **Image Augmentation**: Rotation, shift, zoom, flip, brightness adjustment
- **Regularization**: L2 regularization, dropout, batch normalization
- **Optimizer**: Adam
- **Loss Function**: Categorical crossentropy

### Supported Classes (15 total)

#### 🌶️ Pepper (Bell Pepper) - 2 classes
1. Bacterial spot
2. Healthy

#### 🥔 Potato - 3 classes
1. Early blight
2. Late blight
3. Healthy

#### 🍅 Tomato - 10 classes
1. Bacterial spot
2. Early blight
3. Late blight
4. Leaf Mold
5. Septoria leaf spot
6. Spider mites (Two-spotted spider mite)
7. Target Spot
8. Tomato Yellow Leaf Curl Virus
9. Tomato mosaic virus
10. Healthy

## 📁 Project Structure

```
desease_predict/
├── backend/
│   ├── app.py                          # Flask API server
│   ├── requirements.txt                # Python dependencies
│   ├── start.bat                       # Quick start script
│   └── .gitignore
├── frontend/
│   ├── public/
│   │   └── index.html                  # HTML template
│   ├── src/
│   │   ├── App.js                      # Main React component
│   │   ├── App.css                     # Component styles
│   │   ├── index.js                    # React entry point
│   │   └── index.css                   # Global styles
│   ├── package.json                    # Node dependencies
│   ├── start.bat                       # Quick start script
│   └── .gitignore
├── final_enhanced_plant_disease_model.h5  # Trained model (5.65 MB)
├── Untitled11.ipynb                    # ML training pipeline
├── README.md                           # Main documentation
├── SUBMISSION.md                       # This file
└── venv/                               # Python virtual environment
```

## 🚀 Installation & Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- pip (Python package manager)
- npm (Node package manager)

### Step 1: Clone or Download the Repository
```bash
# If using Git
git clone <repository-url>
cd desease_predict

# Or download and extract the ZIP file
```

### Step 2: Backend Setup

#### Windows:
```cmd
# Navigate to project root
cd "d:\AI models\desease_predict"

# Create virtual environment (if not exists)
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Run the Flask server
python app.py
```

#### Linux/Mac:
```bash
# Navigate to project root
cd /path/to/desease_predict

# Create virtual environment (if not exists)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Run the Flask server
python app.py
```

The backend will start at `http://localhost:5000`

### Step 3: Frontend Setup

Open a **new terminal** (keep backend running):

```cmd
# Windows
cd "d:\AI models\desease_predict\frontend"
npm install
npm start

# Linux/Mac
cd /path/to/desease_predict/frontend
npm install
npm start
```

The frontend will automatically open at `http://localhost:3000`

### Quick Start (Windows only)
Use the provided batch files:
1. Double-click `backend/start.bat` to start the backend
2. Double-click `frontend/start.bat` to start the frontend

## 📚 Dataset Information

### Dataset Source
**PlantVillage Dataset** - Available on Kaggle
- **Link**: https://www.kaggle.com/datasets/emmarex/plantdisease
- **Description**: A collection of plant leaf images with various disease conditions
- **Classes Used**: 15 classes (Pepper, Potato, Tomato diseases)
- **Total Images**: Training split (80%) and Validation split (20%)

### Dataset Preparation
The dataset was organized and split using the notebook `Untitled11.ipynb`:
1. Downloaded from Kaggle
2. Extracted and organized into train/validation folders
3. Applied data augmentation for training
4. Preprocessed to 256x256 RGB images

## 🔧 Technology Stack

### Backend
- **Flask** 3.1.2 - Web framework
- **TensorFlow** 2.20.0 - Deep learning
- **Keras** 3.12.0 - High-level neural networks API
- **Flask-CORS** 6.0.1 - Cross-origin resource sharing
- **NumPy** 2.3.5 - Numerical processing
- **Pillow** 12.0.0 - Image processing

### Frontend
- **React** 18.2.0 - UI framework
- **Axios** 1.6.0 - HTTP client
- **CSS3** - Styling

### ML Pipeline
- **TensorFlow/Keras** - Model training
- **ImageDataGenerator** - Data augmentation
- **scikit-learn** - Evaluation metrics
- **Matplotlib/Seaborn** - Visualization

## 📈 Model Evaluation Metrics

The model was evaluated on the validation set with the following metrics:

### Overall Performance
- **Validation Accuracy**: High accuracy across all classes
- **Loss**: Categorical crossentropy
- **Precision**: Per-class precision scores
- **Recall**: Per-class recall scores
- **F1-Score**: Harmonic mean of precision and recall

### Evaluation Visualizations (in Untitled11.ipynb)
1. **Training History Plots**: Loss and accuracy curves
2. **Confusion Matrix**: Both raw counts and normalized
3. **Per-Class Accuracy**: Bar chart showing performance per disease
4. **Classification Report**: Detailed metrics for each class

## 🎨 Application Features

### Frontend UI
- **Modern Design**: Gradient purple background with white card interface
- **Drag & Drop**: Easy image upload
- **Real-time Preview**: See uploaded image before prediction
- **Confidence Visualization**: Color-coded progress bars
- **Health Status Badges**: Visual indicators for healthy/diseased plants
- **Plant Icons**: 🌶️ 🥔 🍅 for visual identification
- **Responsive**: Works on desktop and mobile devices

### Backend API
- **Fast Inference**: Quick disease prediction
- **Top 5 Predictions**: Shows confidence for top 5 classes
- **Error Handling**: Graceful error responses
- **CORS Enabled**: Seamless frontend integration
- **Health Checks**: API status monitoring

## 📸 Screenshots

### Required Screenshots (See PROJECT_REPORT.pdf):
1. ✅ Frontend UI before prediction - Upload interface
2. ✅ Frontend UI after prediction - Results display with confidence scores
3. ✅ ML Pipeline evaluation metrics - Confusion matrix, accuracy plots from notebook

## 🔐 API Documentation

### POST /api/predict
**Request:**
```
Content-Type: multipart/form-data
Body: image file (JPEG, PNG)
```

**Response:**
```json
{
  "status": "success",
  "prediction": {
    "class": "Tomato_Early_blight",
    "plant": "Tomato",
    "disease": "Early blight",
    "confidence": 0.95,
    "percentage": "95.00%",
    "is_healthy": false
  },
  "top_predictions": [
    {"class": "Tomato_Early_blight", "confidence": 0.95, "percentage": "95.00%"},
    {"class": "Tomato_Late_blight", "confidence": 0.03, "percentage": "3.00%"},
    ...
  ],
  "reliable": true
}
```

## ⚠️ Limitations & Notes

1. **Plant Types**: Model only works with Pepper (Bell), Potato, and Tomato plants
2. **Image Quality**: Best results with clear, well-lit leaf images
3. **Confidence Threshold**: Predictions below 70% confidence may be unreliable
4. **Development Server**: Flask server is for development only, not production-ready

## 🐛 Troubleshooting

### Common Issues

**1. Module not found errors**
```bash
# Make sure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r backend/requirements.txt
```

**2. Model file not found**
- Ensure `final_enhanced_plant_disease_model.h5` is in the project root directory
- Check file path in `backend/app.py` line 42

**3. Port already in use**
- Stop other applications using port 5000 or 3000
- Or change ports in respective configuration files

**4. CORS errors**
- Verify Flask-CORS is installed
- Check that backend is running before starting frontend

## 📝 Future Improvements

1. Add more plant types and diseases
2. Implement model versioning
3. Add user authentication
4. Store prediction history
5. Deploy to cloud platform (AWS, Heroku, etc.)
6. Mobile application (React Native)
7. Batch image processing
8. Disease treatment recommendations

## 👨‍💻 Development

### Running Tests
```bash
# Backend tests (if implemented)
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

### Building for Production
```bash
# Frontend production build
cd frontend
npm run build

# Deploy backend with production WSGI server
pip install gunicorn  # Linux/Mac
gunicorn -b 0.0.0.0:5000 app:app
```

## 📄 License

This project is created for educational purposes as part of an AI/ML course assignment.

## 🤝 Acknowledgments

- **Dataset**: PlantVillage Dataset from Kaggle
- **Framework**: TensorFlow/Keras team
- **UI Inspiration**: Modern web design principles

## 📧 Contact

For questions or issues, please refer to the project documentation or contact the development team.

---

**Submission Date**: November 29, 2025  
**Project**: Plant Disease Prediction System  
**Technology**: Full-stack AI/ML Application with CNN Model

---

## ✅ Submission Checklist

- [x] Source code organized in folders (/frontend, /backend)
- [x] README.md with project description and instructions
- [x] Dataset link included
- [x] Trained model file (final_enhanced_plant_disease_model.h5)
- [x] Project report with screenshots
- [x] ML pipeline notebook (Untitled11.ipynb)
- [x] All dependencies listed (requirements.txt, package.json)
- [x] Installation and running instructions
- [x] API documentation
- [x] Model performance metrics
