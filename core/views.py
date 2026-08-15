from rest_framework import viewsets, permissions
from .models import Atay, Customer, Order
from .serializers import AtaySerializer, CustomerSerializer, OrderSerializer


class AtayViewSet(viewsets.ModelViewSet):
    queryset = Atay.objects.all()
    serializer_class = AtaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAdminUser]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]