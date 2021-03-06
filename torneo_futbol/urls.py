"""torneo_futbol URL Configuration"""

# Django Imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Prject Imports
from campeonato import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('campeonato.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)