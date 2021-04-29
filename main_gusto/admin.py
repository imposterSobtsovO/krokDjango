from django.contrib import admin
from .models import Category, Dish, Events, Banner, UsersMessages



# Register your models here.
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Events)
admin.site.register(Banner)
admin.site.register(UsersMessages)