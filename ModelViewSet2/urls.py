from django.urls import path
from ModelViewSet2 import views

urlpatterns = [
    path('books2/', views.Book2ModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('books2/<int:id>/', views.Book2ModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]