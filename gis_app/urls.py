from django.urls import path, include
from .views import *

urlpatterns = [
    path('location/', LocationCreateListView.as_view(), name='Location-data-list'),
    path('location/<int:pk>/', LocationRetrieveUpdateDeleteView.as_view(),
         name='Location-data-update-delete'),
]
