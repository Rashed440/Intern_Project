from django.urls import path
from . import views

urlpatterns = [
    path('', views.financial_data_list, name='financial_data_list'),
    path('data/<int:pk>/', views.financial_data_detail, name='financial_data_detail'),
    path('data/new/', views.financial_data_new, name='financial_data_new'),
    path('data/<int:pk>/edit/', views.financial_data_edit, name='financial_data_edit'),
    path('data/<int:pk>/delete/', views.financial_data_delete, name='financial_data_delete'),
]
