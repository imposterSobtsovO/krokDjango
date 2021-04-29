from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def banner_format_view(request):
    if request.method == 'POST':

        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/menu_format/banner_form')

    add_banner_form = BannerForm()
    return render(request, 'banner_form.html', context={'form': add_banner_form
                                                        })
def category_format_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/menu_format/category_form')
    add_category_form = CategoryForm()
    return render(request, 'category_form.html', context={'form': add_category_form
                                                        })
def dish_format_view(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/menu_format/dish_form')
    add_dish_form = DishForm()
    return render(request, 'dish_form.html', context={'form': add_dish_form
                                                        })

def event_format_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/menu_format/event_form')
    add_event_form = EventForm()
    return render(request, 'event_form.html', context={'form': add_event_form
                                                        })

def menu_format_view(request):

    return render(request, 'menu_format.html')

