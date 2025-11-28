@echo off
echo ========================================
echo   Plant Disease Predictor - Frontend
echo ========================================
echo.

echo Installing dependencies (if needed)...
call npm install

echo.
echo Starting React development server...
echo App will be available at http://localhost:3000
echo Press Ctrl+C to stop the server
echo.

call npm start
