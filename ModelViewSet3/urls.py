from rest_framework.urls import path
from django.contrib.auth import views
from ModelViewSet3 import views


urlpatterns = [
    path('books3/', views.ModelViewSetBooks33.as_view({'get': 'list', 'post': 'create'})),
    path('books3/<int:id>/', views.ModelViewSetBooks33.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]