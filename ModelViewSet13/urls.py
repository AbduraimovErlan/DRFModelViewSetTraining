from django.urls import path
from ModelViewSet13 import views



urlpatterns = [
    path('books13/', views.ModelViewSetBook13.as_view({'get': 'list', 'post': 'create'})),
    path('books13/<int:id>/', views.ModelViewSetBook13.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]