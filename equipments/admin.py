from django.contrib import admin
from .models import Tractor, Implement, ImplementCategory, TractorCategory, ImplementSubCategory

admin.site.register(Tractor)
admin.site.register(Implement)
admin.site.register(ImplementCategory)
admin.site.register(TractorCategory)
admin.site.register(ImplementSubCategory)
