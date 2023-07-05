from django.urls import path
from ModelViewSet5.views import ModelViewSetBook5
from ModelViewSet5 import views

urlpatterns = [
    path('books5/', views.ModelViewSetBook5.as_view({'get': 'list', 'post': 'create'})),
    path('books5/<int:id>/', views.ModelViewSetBook5.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]