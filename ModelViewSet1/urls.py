from . import views
from django.urls import path





urlpatterns =[
    path('books/', views.BookAPIViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:id>/', views.BookAPIViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]