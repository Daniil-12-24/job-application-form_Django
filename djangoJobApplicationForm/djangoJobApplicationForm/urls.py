from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('job_application.urls')),
    path('admin/', admin.site.urls),
]