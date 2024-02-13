from django.db import models
from product.models import HalfCarcasses, ByProduct, Date
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
    half_carcasses_quantity = models.IntegerField(verbose_name='количество полутуш в кг', **NULLABLE)
    by_product_quantity = models.IntegerField(verbose_name='количество субпродукты в кг', **NULLABLE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, verbose_name='дата заказа', default=timezone.now,
                             **NULLABLE)
    status = models.CharField(default=STATUS_ACCEPTED, choices=STATUSES, verbose_name='статус заказа')
    description = models.TextField(max_length=500, verbose_name='описание', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE,
                             **NULLABLE)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
