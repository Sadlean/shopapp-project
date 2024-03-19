from rest_framework.routers import SimpleRouter
from .views import ItemsPage, OrderAdd
from django.urls import path

router = SimpleRouter()
# При переходе пользователя по url 'api/items' будет вызван класс ItemsPage из файла views (приложение main)
router.register('api/items', ItemsPage)
# При работе с APIview все URL адресы записываются в стандартном формате в urlpatterns
urlpatterns = [
    path('api/order-add/', OrderAdd.as_view())
]
urlpatterns += router.urls




