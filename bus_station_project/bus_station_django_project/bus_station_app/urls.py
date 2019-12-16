from django.urls import path
from . import views

urlpatterns = [
    #path('', views.base, name='index'),
    path('', views.show_map, name='show-map')
]
