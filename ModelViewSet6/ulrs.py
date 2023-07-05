from django.urls import path
from ModelViewSet6 import views


urlpatterns = [
    path('books6/', views.ModelViewSerBook6.as_view({'get': 'list', 'post': 'create'})),
    path('books6/<int:id>/', views.ModelViewSerBook6.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]