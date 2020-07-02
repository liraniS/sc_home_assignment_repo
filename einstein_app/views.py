from django.shortcuts import render
from django.views import generic
from .models import Course, Category

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'einstein_app/home.html'
    context_object_name = 'my_lists'

    def get_queryset(self):
        categories_list = Category.objects.all()
        courses_list = Course.objects.all()[:6]

        return {'categories_list':categories_list,
                'courses_list':courses_list,
            }
