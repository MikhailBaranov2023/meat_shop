from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class HalfCarcasses(models.Model):
    price = models.PositiveIntegerField(default=0, verbose_name='цена', **NULLABLE)
    kg = models.BooleanField(default=False, verbose_name='кг', **NULLABLE)
    piece = models.BooleanField(default=False, verbose_name='штуки', **NULLABLE)

    def __str__(self):
        if self.kg is True:
            return f'Полутуши-{self.price}р/кг '
        else:
            return f'Полутуши-{self.price}р/шт'

    class Meta:
        verbose_name = 'полутуша'
        verbose_name_plural = 'полутуши'


class ByProduct(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название продукта', **NULLABLE)
    price = models.PositiveIntegerField(default=0, verbose_name='цена', **NULLABLE)
    kg = models.BooleanField(default=False, verbose_name='кг', **NULLABLE)
    piece = models.BooleanField(default=False, verbose_name='штуки', **NULLABLE)

    def __str__(self):
        if self.kg is True:
            return f'{(self.title).title()}-{self.price}р/кг '
        else:
            return f'{(self.title).title()}-{self.price}р/шт'

    class Meta:
        verbose_name = 'субпродукты'
        verbose_name_plural = 'субпродукты'


class Date(models.Model):
    date = models.DateField(verbose_name='дата', unique=True, **NULLABLE)
    half_carcasses = models.ForeignKey(HalfCarcasses, on_delete=models.CASCADE, verbose_name='полутуши', **NULLABLE)
    half_carcasses_quantity = models.IntegerField(verbose_name='доступное количество в кг', **NULLABLE)
    by_product = models.ManyToManyField(ByProduct, verbose_name='субпродукты', blank=True, through='ByProductItem')

    def __str__(self):
        return f'{self.date}  {self.half_carcasses} - доступно({self.half_carcasses_quantity}кг)  )'

    class Meta:
        verbose_name = 'доступные даты для заказа'
        verbose_name_plural = 'доступные даты для заказа'


class ByProductItem(models.Model):
    by_product = models.ForeignKey(ByProduct, on_delete=models.CASCADE, verbose_name='субпродукт')
    date = models.ForeignKey(Date, on_delete=models.CASCADE, verbose_name='дата')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество субпродукта')

    class Meta:
        verbose_name = 'Количество субпродукта на дату'
        verbose_name_plural = 'Количество субпродукта на дату'


class Announcement(models.Model):
    body = models.TextField(max_length=500, verbose_name='Объявление', **NULLABLE)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
