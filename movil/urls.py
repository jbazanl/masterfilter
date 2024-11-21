from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', movil, name="movil"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('upload', upload, name="upload"),
    path('reanude', reanude, name="reanude"),
    path('export', export, name="export"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)