from django.urls import path
from ModelViewSet11 import views



urlpatterns = [
    path('books11/', views.ModelViewSetBook11.as_view({'get': 'list', 'post': 'create'})),
    path('books11/<int:id>/', views.ModelViewSetBook11.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]