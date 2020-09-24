from django.contrib import admin
from .models import (Tractor, Implement, ImplementCategory,
                     TractorCategory, ImplementSubCategory)


@admin.register(Tractor)
class TractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'tractor_type', 'agree_terms',
                    'approved', )


@admin.register(Implement)
class ImplementAdmin(admin.ModelAdmin):
    list_display = ('name', 'agree_terms', 'approved', )


admin.site.register(ImplementCategory)
admin.site.register(TractorCategory)
admin.site.register(ImplementSubCategory)
