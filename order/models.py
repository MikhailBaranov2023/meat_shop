from django.db import models
from product.models import ByProduct, Date
from django.conf import settings
from django.utils import timezone

NULLABLE = {
    'null': True,
    'blank': True
}


class Order(models.Model):
    STATUS_COMPLETED = 'completed'
    STATUS_ACCEPTED = 'accepted'
    STATUS_CANCEL = 'cancel'

    STATUSES = (
        (STATUS_COMPLETED, 'Исполнено'),
        (STATUS_ACCEPTED, 'Принят'),
        (STATUS_CANCEL, 'Отменен')
    )
    half_carcasses_quantity = models.IntegerField(verbose_name='количество полутуш в шт', **NULLABLE)
    by_product = models.ManyToManyField(ByProduct, verbose_name='субпродукты', blank=True, through='ByProductOrders')
    date = models.ForeignKey(Date, on_delete=models.CASCADE, verbose_name='дата заказа', default=timezone.now,
                             **NULLABLE)
    status = models.CharField(default=STATUS_ACCEPTED, choices=STATUSES, verbose_name='статус заказа')
    description = models.TextField(max_length=500, verbose_name='описание', **NULLABLE)
    cancel_date = models.DateField(verbose_name='крайняя дата отмены заказа', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE,
                             **NULLABLE)

    def __str__(self):
        return f"{self.user} - {self.date}"

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class ByProductOrders(models.Model):
    by_product = models.ForeignKey(ByProduct, on_delete=models.CASCADE, verbose_name='субпродукт')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество субпродукта')

    class Meta:
        verbose_name = 'Количество субпродуктов в заказе'
        verbose_name_plural = 'Количество субпродуктов в заказе'
