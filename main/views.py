from django.shortcuts import render
from .serializers import ItemSerializer, OrderSerializer
# ModelViewSet служит для выборки всех или некоторых элементов
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
# Импортируем модель Item для работы с ней


class ItemsPage(ModelViewSet):
    # Указываем, что выбираем все объекты
    # Можно использовать функцию filter, чтобы получить по определенной выборке (например, price < 30; )
    queryset = Item.objects.all().order_by('id')
    # Указываем класс сериализации
    serializer_class = ItemSerializer


class OrderAdd(APIView):
    # def put(self, req): - при передачи данных из формочки, но для обновления существующего элемента
    # def delete(self, req): - при передачи данных из формочки, но для удаления существующего элемента
    def post(self, request):
        # В data будет записан JSON объект, который получаем со стороны пользователя
        order = OrderSerializer(data=request.data)
        #  Возвращения определенных данных на сторону клиента

        if order.is_valid():
            order.save()
            return Response({'result': 'Пару секунд'})

        return Response({'result': 'Ошибка в форме'})






