from django.conf.urls.static import static
from rest_framework import routers
from django.conf import settings
from .api import UserViewSet


router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'user')

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
