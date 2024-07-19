from django.contrib import admin
from django.urls import path
from .views import create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', create_user, name='create_user'),
]
