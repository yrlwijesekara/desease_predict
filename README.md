# Plant Disease Prediction System

A full-stack application for predicting plant diseases using deep learning. Built with Flask backend and React frontend.

## 🌟 Features

- **Deep Learning Model**: CNN model trained on 15 plant disease classes
- **Real-time Prediction**: Upload plant leaf images for instant disease detection (supports Pepper, Potato, and Tomato plants)
- **Confidence Scoring**: Get confidence levels for predictions
- **Beautiful UI**: Modern, responsive React interface
- **REST API**: Easy-to-use Flask API endpoints

## 📁 Project Structure

```
desease_predict/
├── backend/
│   ├── app.py                 # Flask API server
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js            # Main React component
│   │   ├── App.css           # Styles
│   │   ├── index.js          # React entry point
│   │   └── index.css         # Global styles
│   └── package.json          # Node dependencies
├── final_enhanced_plant_disease_model.h5  # Trained model
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 14+
- Virtual environment (venv)

### Backend Setup

1. **Activate your virtual environment:**
   ```cmd
   cd "d:\AI models\desease_predict"
   venv\Scripts\activate
   ```

2. **Install Python dependencies:**
   ```cmd
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the Flask server:**
   ```cmd
   python app.py
   ```
   
   The API will be available at `http://localhost:5000`

### Frontend Setup

1. **Open a new terminal and navigate to frontend:**
   ```cmd
   cd "d:\AI models\desease_predict\frontend"
   ```

2. **Install Node dependencies:**
   ```cmd
   npm install
   ```

3. **Start the React development server:**
   ```cmd
   npm start
   ```
   
   The app will open at `http://localhost:3000`

## 🔌 API Endpoints

### GET `/`
Health check endpoint
- **Response**: Server status and model info

### GET `/api/health`
Detailed health check
- **Response**: Server and model status

### GET `/api/classes`
Get all plant disease classes
- **Response**: List of 15 disease classes

### POST `/api/predict`
Predict plant disease from image
- **Request**: `multipart/form-data` with `image` file
- **Response**: 
  ```json
  {
    "status": "success",
    "prediction": {
      "class": "Tomato___Early_blight",
      "plant": "Tomato",
      "disease": "Early_blight",
      "confidence": 0.95,
      "percentage": "95.00%",
      "is_healthy": false
    },
    "top_predictions": [...],
    "reliable": true
  }
  ```

## 🎯 Supported Plants and Diseases

The model can detect diseases in **3 types of plants** with **15 total classes**:

### 🌶️ **Pepper (Bell Pepper)** - 2 classes
- Bacterial spot
- Healthy

### 🥔 **Potato** - 3 classes
- Early blight
- Late blight
- Healthy

### 🍅 **Tomato** - 10 classes
- Bacterial spot
- Early blight
- Late blight
- Leaf Mold
- Septoria leaf spot
- Spider mites (Two-spotted spider mite)
- Target Spot
- Tomato Yellow Leaf Curl Virus
- Tomato mosaic virus
- Healthy

**Note**: The model is specifically trained for these 3 plant types only. Upload clear images of Pepper, Potato, or Tomato leaves for best results.

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework
- **TensorFlow/Keras**: Deep learning model
- **Flask-CORS**: Cross-origin resource sharing
- **NumPy**: Numerical processing
- **Pillow**: Image processing

### Frontend
- **React**: UI framework
- **Axios**: HTTP client
- **CSS3**: Modern styling

## 📊 Model Information

- **Architecture**: Enhanced CNN with 4 convolutional blocks
- **Input Size**: 256x256 RGB images
- **Output**: 15 classes (Pepper, Potato, Tomato diseases)
- **Training**: Augmented dataset with regularization
- **Confidence Threshold**: 70% for reliable predictions

## 🔧 Troubleshooting

### Backend Issues

1. **Import errors**: Make sure virtual environment is activated and all packages are installed
   ```cmd
   venv\Scripts\activate
   pip install -r backend\requirements.txt
   ```

2. **Model not found**: Ensure `final_enhanced_plant_disease_model.h5` is in the root directory

3. **Port already in use**: Change the port in `backend/app.py`

### Frontend Issues

1. **Cannot connect to server**: Verify backend is running on port 5000

2. **CORS errors**: Check that Flask-CORS is installed in backend

3. **Module not found**: Delete `node_modules` and reinstall
   ```cmd
   rmdir /s /q node_modules
   npm install
   ```

## 📝 Usage Example

1. Start both backend and frontend servers
2. Open browser to `http://localhost:3000`
3. Click the upload area or drag and drop a plant leaf image
4. Click "🔍 Predict Disease"
5. View the prediction results with confidence score

## 🎨 Screenshots

The application features:
- Gradient purple background
- Clean white card-based interface
- Image preview before prediction
- Confidence bars with color coding
- Health status badges
- Responsive design for mobile devices

## 📄 License

This project is for educational purposes.

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests!

## ⚡ Performance Tips

- **Supported plants only**: The model works ONLY with Pepper (Bell), Potato, and Tomato plants
- Use clear, well-lit images for best results
- Ensure the leaf is the main subject of the image
- Avoid blurry or heavily edited images
- Images should show disease symptoms clearly
- For best accuracy, upload images similar to the training dataset

---

Made with ❤️ using TensorFlow & React
