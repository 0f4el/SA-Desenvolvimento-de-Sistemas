from rest_framework import permissions, viewsets

from .models import Notebook, Rack, Sala
from .serializers import NotebookSerializer, RackSerializer, SalaSerializer


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all().order_by("nome")
    serializer_class = SalaSerializer
    permission_classes = [permissions.IsAuthenticated]


class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.select_related("sala").all().order_by("identificador")
    serializer_class = RackSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.select_related("rack", "rack__sala").all().order_by("rack", "numero_slot")
    serializer_class = NotebookSerializer
    permission_classes = [permissions.IsAuthenticated]
