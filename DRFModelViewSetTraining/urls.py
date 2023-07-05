from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ModelViewSet1.urls')),
    path('api/v1/', include('ModelViewSet2.urls')),
    path('api/v1/', include('ModelViewSet3.urls')),
    path('api/v1/', include('ModelViewSet4.urls')),
    path('api/v1/', include('ModelViewSet5.urls'))
]

