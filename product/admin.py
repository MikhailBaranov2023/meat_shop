from django.contrib import admin
from product.models import HalfCarcasses, ByProduct, Date, Announcement, ByProductItem


@admin.register(HalfCarcasses)
class AdminHalfCarcasses(admin.ModelAdmin):
    list_display = ('price',)


@admin.register(ByProduct)
class AdminByProduct(admin.ModelAdmin):
    list_display = ('title', 'price',)


@admin.register(Date)
class AdminDate(admin.ModelAdmin):
    list_display = ('date', 'half_carcasses', 'half_carcasses_quantity',)
    filter_horizontal = ['by_product', ]


@admin.register(Announcement)
class AdminAnnouncement(admin.ModelAdmin):
    list_display = ('body',)


