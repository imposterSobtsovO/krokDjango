from django.urls import path
from .views import *


urlpatterns = [
    path('', menu_format_view),
    path('banner_form', banner_format_view),
    path('category_form', category_format_view),
    path('dish_form', dish_format_view),
    path('event_form', event_format_view),

]