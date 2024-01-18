from rest_framework import viewsets
from .models import PlayList
from .serializer import PlayListSerializer

# Create your views here.
class PlayListViewSet(viewsets.ModelViewSet):
    queryset=PlayList.objects.all()
    serializer_class = PlayListSerializer