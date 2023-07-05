from django.urls import path
from ModelViewSet8 import views





urlpatterns = [
    path('books8/', views.ModelViewSetBook8.as_view({'get': 'list', 'post': 'create'})),
    path('books8/<int:id>/', views.ModelViewSetBook8.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]