from django.urls import path
from ModelViewSet9 import views



urlpatterns = [
    path('books9/', views.ModelViewSetBook9.as_view({'get': 'list', 'post': 'create'})),
    path('books9/<int:id>/', views.ModelViewSetBook9.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]