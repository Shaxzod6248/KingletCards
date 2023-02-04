from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Color)
admin.site.register(Orders)
admin.site.register(Variants)
admin.site.register(Product)