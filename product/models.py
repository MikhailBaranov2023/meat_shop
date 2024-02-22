from django.db import models
from django.utils import timezone

NULLABLE = {
    'null': True,
    'blank': True
}


class HalfCarcasses(models.Model):
    price = models.PositiveIntegerField(default=0, verbose_name='цена за кг', **NULLABLE)

    def __str__(self):
        return f'Полутуши: цена за кг - {self.price}'

    class Meta:
        verbose_name = 'полутуша'
        verbose_name_plural = 'полутуши'


class ByProduct(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название продукта', **NULLABLE)
    price = models.PositiveIntegerField(default=0, verbose_name='цена за кг', **NULLABLE)

    def __str__(self):
        return f'Субпродукт: {self.title}, цена за кг - {self.price}'

    class Meta:
        verbose_name = 'субпродукты'
        verbose_name_plural = 'субпродукты'


class Date(models.Model):
    date = models.DateField(verbose_name='дата', unique=True, **NULLABLE)
    half_carcasses = models.ForeignKey(HalfCarcasses, on_delete=models.CASCADE, verbose_name='полутуши', **NULLABLE)
    half_carcasses_quantity = models.IntegerField(verbose_name='доступное количество в кг', **NULLABLE)
    by_product = models.ForeignKey(ByProduct, on_delete=models.CASCADE, verbose_name='субпродукты', **NULLABLE)
    by_product_quantity = models.IntegerField(verbose_name='доступное количество субпродуктов в кг', **NULLABLE)

    def __str__(self):
        return f'{self.date}  {self.half_carcasses} - доступно({self.half_carcasses_quantity}кг)  и {self.by_product} - доступно({self.by_product_quantity}кг)'

    class Meta:
        verbose_name = 'доступные даты для заказа'
        verbose_name_plural = 'доступные даты для заказа'
