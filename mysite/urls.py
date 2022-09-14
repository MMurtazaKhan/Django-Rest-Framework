
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api_two/',include('api_two.urls')),
    path('mixin/',include('mixin.urls')),
]
