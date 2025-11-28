@echo off
echo ========================================
echo   Plant Disease Predictor - Backend
echo ========================================
echo.

echo Activating virtual environment...
call ..\venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Flask server...
echo Server will be available at http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python app.py
