from django.urls import path
from ModelViewSet12 import views



urlpatterns = [
    path('books12/', views.ModelViewSetBook12.as_view({'get': 'list', 'post': 'create'})),
    path('books12/<int:id>/', views.ModelViewSetBook12.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]