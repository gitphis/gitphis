from django.contrib import admin
from django.urls import path,re_path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("ngrok_urls/",views.ngrok_urls),
    re_path(r'^short2/(?P<slug>[\w-]+)',views.short2),
    re_path(r'^short/(?P<slug>[\w-]+)',views.short),
    re_path(r'^clock/(?P<slug>[\w-]+)',views.clock),


    re_path('\d{1}',views.hunt_page)
]
