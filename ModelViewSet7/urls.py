from django.urls import path
from ModelViewSet7 import views




urlpatterns = [
    path('books7/', views.ModelViewSetBook7.as_view({'get': 'list', 'post': 'create'})),
    path('books7/<int:id>/', views.ModelViewSetBook7.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
