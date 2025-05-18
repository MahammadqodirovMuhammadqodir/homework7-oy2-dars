from rest_framework import viewsets, filters
from .models import Religion
from .serializers import ReligionSerializer

class ReligionViewSet(viewsets.ModelViewSet):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'founder', 'origin_place']
    ordering_fields = ['name', 'origin_date']
