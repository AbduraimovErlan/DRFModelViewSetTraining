from django.urls import path
from ModelViewSet10 import views



urlpatterns = [
    path('books10/', views.ModelViewSetBook10.as_view({'get': 'list', 'post': 'create'})),
    path('books10/<int:id>/', views.ModelViewSetBook10.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]