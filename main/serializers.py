from rest_framework.serializers import ModelSerializer
from .models import Item, Order


class ItemSerializer(ModelSerializer):
    class Meta:
        # Работаем с моделью Item
        model = Item
        # Выбираем все поля из базы данных
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        # Работаем с моделью Order
        model = Order
        # Выбираем все поля из базы данных
        fields = '__all__'




