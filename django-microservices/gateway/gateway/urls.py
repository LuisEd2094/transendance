from django.contrib import admin
from django.urls import path
from .views import create_user, send_message, test_logging 
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', create_user, name='create_user'),
    path('send_message/', send_message, name='send_message'),
    path('create_conversation/', send_message, name='create_conversation'),
    path('test_logging/', test_logging, name='test_logging'),
    path('', include('django_prometheus.urls')),
]
