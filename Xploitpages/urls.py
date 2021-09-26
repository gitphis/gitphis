from django.contrib import admin
from django.urls import path,re_path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("ngrok_url/",views.ngrok_url),
    re_path('\d{1}',views.hunt_page)
]
