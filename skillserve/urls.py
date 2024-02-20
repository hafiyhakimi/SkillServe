from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path ('', include('dashui.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('service/', include('service.urls')),
    path('report/', include('report.urls')),
    path('payment/', include('payment.urls')),
    path('inventory/', include('inventory.urls')),
    path('dashui/', include('dashui.urls')),
    path('API/', include('API.urls')),
]
