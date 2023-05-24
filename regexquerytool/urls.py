from django.contrib import admin
from django.urls import path

from regex_app.views import regexquery_home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regex/', regexquery_home_view, name='home')
]
