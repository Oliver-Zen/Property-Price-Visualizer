# visualization/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualization_view, name='visualization'),
<<<<<<< HEAD
    path('visualization/', views.visualization_view, name='visualization'),
    path('choropleth/', views.choropleth_view, name='choropleth'),
    path('price_query/', views.price_query_view, name='price_query'),
=======
    path('choropleth/', views.choropleth_view, name='choropleth'),
    path('data/', views.get_data, name='get_data'),
    path('price-query/', views.price_query_view, name='price_query'),
>>>>>>> eab1542 (integrate django)
]
