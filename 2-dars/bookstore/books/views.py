from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserSetting
from .serializers import UserSettingSerializer

@api_view(['POST'])
def set_country(request):
    country = request.data.get('country')
    setting, _ = UserSetting.objects.get_or_create(id=1)
    setting.country = country
    setting.save()
    return Response({'message': 'Country set successfully'})

@api_view(['POST'])
def set_lang(request):
    lang = request.data.get('lang')
    setting, _ = UserSetting.objects.get_or_create(id=1)
    setting.lang = lang
    setting.save()
    return Response({'message': 'Language set successfully'})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'genre']
    ordering_fields = ['published_year']
