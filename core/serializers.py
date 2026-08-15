from rest_framework import serializers
from .models import Atay, Customer, Order, OrderItem


class AtaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Atay
        fields = ['id', 'name', 'description', 'price', 'stock', 'image', 'available', 'created_at']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'email', 'phone', 'address', 'city']


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price_at_purchase']


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'created_at', 'items']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        items_data = validated_data.pop('items')

        customer, _ = Customer.objects.get_or_create(
            email=customer_data['email'],
            defaults=customer_data
        )

        order = Order.objects.create(customer=customer, **validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order