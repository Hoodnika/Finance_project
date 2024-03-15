from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from finance.views import home

urlpatterns = [
                  path('', home),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)