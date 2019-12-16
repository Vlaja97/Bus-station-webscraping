from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('bus_station_app/', include('bus_station_app.urls')),
    path('admin/', admin.site.urls),
]
