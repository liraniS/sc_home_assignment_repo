from django.shortcuts import render, redirect
from django.views import generic
from .models import *

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'einstein_app/home.html'
    context_object_name = 'categories'

    def get_queryset(self):
        categories_list = Category.objects.all()
        courses_list = Course.objects.all()

        category_dict = {}
        for current_category in categories_list:
            current_courses =  [course for course in courses_list if course.category == current_category]
            category_dict[current_category.name] = current_courses[:6]
        
        return category_dict

def hebrewVer(request):
    return render(request, 'einstein_app/hebrew.html')
