from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
import numpy as np

PLOTS_DIR = os.path.join(os.path.dirname(__file__), 'plots')
os.makedirs(PLOTS_DIR, exist_ok=True)

@api_view(['POST'])
def linear_model(request):
    file = request.FILES.get('file')
    df = pd.read_csv(file)
    X = df[['Area', 'Bedrooms', 'Age']]
    y = df['Price']

    model = LinearRegression()
    model.fit(X, y)
    pred = model.predict(X)

    mae = mean_absolute_error(y, pred)
    r2 = r2_score(y, pred)
    # ✅ Define Accuracy
    mape = np.mean(np.abs((y - pred) / y)) * 100
    accuracy = 100 - mape

    # Plot
    plt.figure()
    plt.plot(y.values, label='Actual')
    plt.plot(pred, label='Predicted')
    plt.legend()
    plot_path = os.path.join(PLOTS_DIR, 'linear_plot.png')
    plt.savefig(plot_path)
    plt.close()

    return Response({
        'mae': mae,
        'r2': r2,
        'accuracy': accuracy,
        'plot_url': f'/media/linear_plot.png'
    })

@api_view(['POST'])
def xgboost_model(request):
    file = request.FILES.get('file')
    df = pd.read_csv(file)
    X = df[['Area', 'Bedrooms', 'Age']]
    y = df['Price']

    model = XGBRegressor()
    model.fit(X, y)
    pred = model.predict(X)

    mae = mean_absolute_error(y, pred)
    r2 = r2_score(y, pred)
    # ✅ Define Accuracy
    mape = np.mean(np.abs((y - pred) / y)) * 100
    accuracy = 100 - mape

    # Plot
    plt.figure()
    plt.plot(y.values, label='Actual')
    plt.plot(pred, label='Predicted')
    plt.legend()
    plot_path = os.path.join(PLOTS_DIR, 'xgboost_plot.png')
    plt.savefig(plot_path)
    plt.close()

    return Response({
        'mae': mae,
        'r2': r2,
        'accuracy': accuracy,
        'plot_url': f'/media/xgboost_plot.png'
    })
