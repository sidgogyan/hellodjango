from django.contrib import admin
from django.urls import path
from myapp.views import myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp)
]
