from django.urls import path
from . import views

urlpatterns = [
    path('linear/', views.linear_model),
    path('xgboost/', views.xgboost_model),
]
