from django.urls import path
from ModelViewSet4.views import ModelViewSet44
from ModelViewSet4 import views

urlpatterns = [
    path('books4/', views.ModelViewSet44.as_view({'get': 'list', 'post': 'create'})),
    path('books4/<int:id>', views.ModelViewSet44.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]