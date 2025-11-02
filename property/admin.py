from django.contrib import admin

from .models import Property
from .models import Category , Reserve

admin.site.register(Property)

admin.site.register(Category)
admin.site.register(Reserve)
