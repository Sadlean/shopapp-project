from django.db import models


class Item(models.Model):
    # Уникальное название товара
    slug = models.SlugField('Уникальное название', unique=True)
    # Название товара
    title = models.CharField('Название товара', max_length=200)
    # Изображение товара
    image = models.CharField('Фото товара', max_length=50)
    # Описание товара
    description = models.TextField('Описаие товара')
    # Цена товара
    price = models.DecimalField('Цена товара', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


# Модель хранения заказов в базе данных
class Order(models.Model):
    name = models.CharField('Имя клиента', max_length=200)
    surname = models.CharField('Фамилия клиента', max_length=200)
    email = models.CharField('Email', max_length=200)
    phone = models.CharField('Номер телефона', max_length=200)
    basket = models.TextField('Корзина товаров')

    def __str__(self):
        return self.name + ' ' + self.surname + '(' + self.phone + ')'



