from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReligionViewSet

router = DefaultRouter()
router.register(r'religions', ReligionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
