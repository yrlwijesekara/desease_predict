# Screenshots Guide

## Required Screenshots for Submission

Please capture the following screenshots and save them in this folder:

### 1. Frontend UI - Before Prediction
**Filename**: `01_frontend_before_prediction.png`

**How to capture**:
1. Start the React frontend (`npm start`)
2. Open browser to `http://localhost:3000`
3. Make sure NO image is uploaded yet
4. Take a full-screen screenshot showing:
   - Header with "Plant Disease Predictor" title
   - Supported plants badge (🌶️ Pepper • 🥔 Potato • 🍅 Tomato)
   - Upload area with cloud icon
   - "Predict Disease" and "Reset" buttons
   - Footer information

---

### 2. Frontend UI - After Successful Prediction
**Filename**: `02_frontend_after_prediction.png`

**How to capture**:
1. Keep the frontend running
2. Upload a plant leaf image (Pepper, Potato, or Tomato)
3. Click "🔍 Predict Disease"
4. Wait for results to display
5. Take a full-screen screenshot showing:
   - Uploaded image preview
   - Plant name with icon (🌶️/🥔/🍅)
   - Health status badge (Healthy or Disease Detected)
   - Disease name
   - Confidence percentage and progress bar
   - Full classification at bottom
   - Ideally show a prediction with >70% confidence

**Recommended test images**:
- Use clear, well-lit leaf images
- Ensure the leaf fills most of the frame
- Use images from the validation dataset for accurate results

---

### 3. ML Pipeline Evaluation Metrics
**Filename**: `03_ml_pipeline_metrics.png`

**How to capture**:
1. Open `Untitled11.ipynb` in Jupyter Notebook or VS Code
2. Run all cells (or just the evaluation cells)
3. Scroll to the evaluation section
4. Capture screenshot(s) showing:
   - Training history plots (loss and accuracy curves)
   - Confusion matrix (both versions if possible)
   - Per-class accuracy bar chart
   - Classification report with precision/recall/F1-scores

**Multiple screenshots option**:
If the metrics don't fit in one screenshot, you can create:
- `03a_training_history.png` - Training curves
- `03b_confusion_matrix.png` - Confusion matrices
- `03c_classification_report.png` - Per-class metrics

---

## Screenshot Tips

### Quality Guidelines
- Use **full-screen** mode for best results
- Ensure **high resolution** (at least 1920x1080)
- Use **PNG format** for better quality
- Make sure **all text is readable**
- Capture **entire browser window** including address bar

### Tools for Capturing
**Windows**:
- Press `Windows + Shift + S` for Snipping Tool
- Or use `PrtScn` button and paste into Paint
- Or use Snagit/Greenshot

**Mac**:
- Press `Cmd + Shift + 4` then `Space` to capture window
- Or `Cmd + Shift + 3` for full screen

**Linux**:
- Use Screenshot tool or `gnome-screenshot`

### File Naming
- Use exactly these names for submission:
  - `01_frontend_before_prediction.png`
  - `02_frontend_after_prediction.png`
  - `03_ml_pipeline_metrics.png`

---

## After Capturing Screenshots

1. ✅ Save all screenshots in this `screenshots/` folder
2. ✅ Verify all images are clear and readable
3. ✅ Check file sizes (should be reasonable, < 5MB each)
4. ✅ Review PROJECT_REPORT.md and update if needed
5. ✅ Ready for submission!

---

## Quick Checklist

- [ ] Backend is running (`python app.py`)
- [ ] Frontend is running (`npm start`)
- [ ] Screenshot 1: Before prediction captured
- [ ] Screenshot 2: After prediction captured (with good confidence)
- [ ] Screenshot 3: Notebook metrics captured
- [ ] All screenshots saved in this folder
- [ ] File names match exactly
- [ ] Images are clear and high quality

---

**Note**: These screenshots are REQUIRED for your project submission. Make sure to capture them before submitting your project!
