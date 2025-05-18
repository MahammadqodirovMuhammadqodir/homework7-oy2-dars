from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>World Religions API</h1>")

urlpatterns = [
    path('', home),  # Bosh sahifa
    path('admin/', admin.site.urls),
    path('api/', include('world_religions.urls')),  # API URL'lar shu yerda
]
