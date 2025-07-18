House Price Prediction - Full Stack Web App
A complete full stack web application for predicting house prices using Machine Learning models. Built with:

 Backend: Django REST Framework
 Frontend: React.js
 ML Models: Linear Regression and XGBoost
 Features: Upload CSV, visualize predictions, view evaluation metrics, switch between models.
View:
Line plot of Actual vs Predicted values
Evaluation metrics (R², MSE, RMSE, MAPE, Accuracy)
Dropdown selector for:
Switching between Linear Regression and XGBoost models
Separate pages for each model's results
Tech Stack
Layer	Technology
Frontend	React.js, Axios
Backend	Django REST Framework
ML Models	scikit-learn, XGBoost
Plotting	Matplotlib
Others	CORS, Joblib

📂 Project Structure

house_price/
├── mlbackend/           # Django Backend
│   ├── mlapp/           # ML views, models
│   ├── media/plots/     # Stores generated plots
│   └── manage.py
├── mlfrontend/      # React Frontend
│   └── src/
│       ├── LinearPage.js
│       ├── XGBoostPage.js
│       └── App.js
⚙️ Installation & Run (Local)
Backend (Django)

cd mlbackend
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
Your backend will run at: http://127.0.0.1:8000/

Frontend (React)

cd mlfrontend
npm install
npm start
Your frontend will run at: http://localhost:3000/

Make sure CORS is enabled in Django to allow frontend-backend communication.

Evaluation Metrics
R² Score
Mean Squared Error (MSE)
Root MSE (RMSE)
Mean Absolute Percentage Error (MAPE)
Accuracy = 100 - MAPE

