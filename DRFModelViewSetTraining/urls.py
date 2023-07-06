from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ModelViewSet1.urls')),
    path('api/v1/', include('ModelViewSet2.urls')),
    path('api/v1/', include('ModelViewSet3.urls')),
    path('api/v1/', include('ModelViewSet4.urls')),
    path('api/v1/', include('ModelViewSet5.urls')),
    path('api/v1/', include('ModelViewSet6.ulrs')),
    path('api/v1/', include('ModelViewSet7.urls')),
    path('api/v1/', include('ModelViewSet8.urls')),
    path('api/v1/', include('ModelViewSet9.urls')),
    path('api/v1/', include('ModelViewSet10.urls')),
    path('api/v1/', include('ModelViewSet11.urls')),
    path('api/v1/', include('ModelViewSet12.urls')),
    path('api/v1/', include('ModelViewSet13.urls')),
]

