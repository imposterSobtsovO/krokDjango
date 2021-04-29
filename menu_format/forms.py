from django import forms
from main_gusto.models import *


class BannerForm(forms.ModelForm):

    CHOICES = [('True', 'Да'),
               ('False', 'Нет')]
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'id': 'title', 'class': 'form-control',
                                                              'placeholder': 'Название', 'required': 'required'}))
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={ 'placeholder': 'Фото', 'class': 'form-control',
                                                                'required': 'required'}))
    is_visible = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(
                                       attrs={'name': 'visible'}))

    class Meta():
        model = Banner
        fields = ('title', 'photo', 'is_visible')


class CategoryForm(forms.ModelForm):
    CHOICES = [('True', 'Да'),
               ('False', 'Нет')]
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'id': 'title', 'class': 'form-control',
                                                              'placeholder': 'Название', 'required': 'required'}))
    category_order = forms.IntegerField(widget=forms.NumberInput(attrs={ 'placeholder': 'Номер', 'class': 'form-control',
                                                                'required': 'required'}))
    is_visible = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(
                                       attrs={'name': 'visible'}))
    is_special = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(
                                       attrs={'name': 'special',}))

    class Meta():
        model = Category
        fields = ('title', 'category_order', 'is_visible', 'is_special')


class DishForm(forms.ModelForm):

    categories = Category.objects.order_by('title')
    CATEGORY_CHOICES = []
    for item in categories:
        CATEGORY_CHOICES.append((item, item.title))

    CHOICES = [('True', 'Да'),
                ('False', 'Нет')]

    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'id': 'title', 'class': 'form-control',
                                                              'placeholder': 'Название', 'required': 'required'}))

    category = forms.ModelChoiceField(queryset=categories)

    description = forms.CharField(max_length=600,
                                   widget=forms.Textarea(
                                       attrs={'name': 'desc', 'id': 'desc', 'class': 'form-control',
                                              'rows': '4', 'placeholder': 'Описание',
                                              'required': 'required'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={ 'placeholder': 'Цена', 'class': 'form-control',
                                                                'required': 'required'}))
    photo = forms.ImageField(widget=forms.ClearableFileInput( attrs={ 'placeholder': 'Фото', 'class': 'form-control',
                                                                'required': 'required'}))
    is_visible = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(
                                       attrs={'name': 'visible'}))

    class Meta():
        model = Dish
        fields = ('title', 'category', 'description', 'price', 'photo', 'is_visible')


class EventForm(forms.ModelForm):

    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'id': 'title', 'class': 'form-control',
                                                              'placeholder': 'Название', 'required': 'required'}))
    photo = forms.ImageField(widget=forms.ClearableFileInput( attrs={ 'placeholder': 'Фото', 'class': 'form-control',
                                                                'required': 'required'}))
    description = forms.CharField()
    event_date = forms.DateInput()
    event_time = forms.TimeInput()
    price = forms.DecimalField()

    class Meta():
        model = Events
        fields = ('title', 'photo', 'description', 'event_date', 'event_time', 'price')
