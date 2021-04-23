
from django.contrib import admin

from .models import Advisor,Book,user




admin.site.register(Advisor)
admin.site.register(Book)
admin.site.register(user)