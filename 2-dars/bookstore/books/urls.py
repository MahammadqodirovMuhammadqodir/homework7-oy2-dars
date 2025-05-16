from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import set_country, set_lang

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('set_country/', set_country),
    path('set_lang/', set_lang),
    path('', include(router.urls)),
]
