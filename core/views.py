from rest_framework import viewsets, permissions
from .models import Atay
from .serializers import AtaySerializer


class AtayViewSet(viewsets.ModelViewSet):
    queryset = Atay.objects.all()
    serializer_class = AtaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]