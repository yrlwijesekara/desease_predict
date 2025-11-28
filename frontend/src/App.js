import React, { useState, useRef } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:5000';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    if (file) {
      // Validate file type
      if (!file.type.startsWith('image/')) {
        setError('Please select a valid image file');
        return;
      }

      setSelectedFile(file);
      setError(null);
      setPrediction(null);

      // Create preview URL
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreviewUrl(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handlePredict = async () => {
    if (!selectedFile) {
      setError('Please select an image first');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('image', selectedFile);

      const response = await axios.post(`${API_URL}/api/predict`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.status === 'success') {
        setPrediction(response.data.prediction);
      } else {
        setError(response.data.message || 'Prediction failed');
      }
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to connect to server. Make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setSelectedFile(null);
    setPreviewUrl(null);
    setPrediction(null);
    setError(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const getHealthStatusColor = (isHealthy) => {
    return isHealthy ? '#10b981' : '#ef4444';
  };

  const getConfidenceColor = (confidence) => {
    if (confidence >= 0.8) return '#10b981';
    if (confidence >= 0.6) return '#f59e0b';
    return '#ef4444';
  };

  return (
    <div className="App">
      <div className="container">
        <header className="header">
          <h1>🌿 Plant Disease Predictor</h1>
          <p>Upload leaf images to detect diseases</p>
          <div className="supported-plants">
            <span>Supports: 🌶️ Pepper • 🥔 Potato • 🍅 Tomato</span>
          </div>
        </header>

        <div className="main-content">
          <div className="upload-section">
            <div className="upload-area">
              {!previewUrl ? (
                <div className="upload-placeholder">
                  <svg
                    className="upload-icon"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                    />
                  </svg>
                  <p>Click to upload or drag and drop</p>
                  <p className="upload-hint">Pepper, Potato, or Tomato leaf images</p>
                  <p className="upload-hint">PNG, JPG, JPEG (Max 10MB)</p>
                </div>
              ) : (
                <div className="image-preview">
                  <img src={previewUrl} alt="Preview" />
                </div>
              )}
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                onChange={handleFileSelect}
                className="file-input"
              />
            </div>

            <div className="button-group">
              <button
                onClick={handlePredict}
                disabled={!selectedFile || loading}
                className="btn btn-primary"
              >
                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Analyzing...
                  </>
                ) : (
                  '🔍 Predict Disease'
                )}
              </button>
              <button onClick={handleReset} className="btn btn-secondary">
                🔄 Reset
              </button>
            </div>
          </div>

          {error && (
            <div className="alert alert-error">
              <span>⚠️ {error}</span>
            </div>
          )}

          {prediction && (
            <div className="results-section">
              <h2>Prediction Results</h2>
              
              <div className="result-card main-result">
                <div className="result-header">
                  <h3>
                    {prediction.plant === 'Pepper' && '🌶️ '}
                    {prediction.plant === 'Potato' && '🥔 '}
                    {prediction.plant === 'Tomato' && '🍅 '}
                    {prediction.plant}
                  </h3>
                  <span
                    className="health-badge"
                    style={{ backgroundColor: getHealthStatusColor(prediction.is_healthy) }}
                  >
                    {prediction.is_healthy ? '✓ Healthy' : '✗ Disease Detected'}
                  </span>
                </div>
                
                <div className="disease-info">
                  <p className="disease-label">Disease:</p>
                  <p className="disease-name">{prediction.disease}</p>
                </div>

                <div className="confidence-bar">
                  <div className="confidence-label">
                    <span>Confidence</span>
                    <span className="confidence-value">{prediction.percentage}</span>
                  </div>
                  <div className="progress-bar">
                    <div
                      className="progress-fill"
                      style={{
                        width: prediction.percentage,
                        backgroundColor: getConfidenceColor(prediction.confidence)
                      }}
                    ></div>
                  </div>
                </div>

                {!prediction.reliable && (
                  <div className="warning-message">
                    ⚠️ Low confidence prediction. Consider retaking the image with better lighting.
                  </div>
                )}
              </div>

              <div className="full-class-name">
                <strong>Full Classification:</strong> {prediction.class}
              </div>
            </div>
          )}
        </div>

        <footer className="footer">
          <p>Powered by TensorFlow & React | Trained on 15 disease classes</p>
          <p style={{fontSize: '0.85rem', marginTop: '5px', opacity: '0.8'}}>
            Supports: Bell Pepper, Potato, and Tomato plants
          </p>
        </footer>
      </div>
    </div>
  );
}

export default App;
