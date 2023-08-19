from django.db import models


class Car(models.Model):

    model = models.CharField('модель автомобиля', max_length=100)
    make = models.CharField('марка автомобиля', max_length=100)
    year = models.IntegerField('год выпуска автомобиля')
    color = models.CharField('цвет автомобиля', max_length=50)
    mileage = models.IntegerField('пробег автомобиля')
    fuel_type = models.CharField('тип топлива', max_length=50)
    price_per_day = models.DecimalField('цена аренды в день',max_digits=10, decimal_places=2)
    avaibilaty_status =models.BooleanField('статус доступности: true/false')

