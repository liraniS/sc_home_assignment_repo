from django.urls import path
from . import views

app_name = 'einstein_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('hebrew/', views.hebrewVer, name='hebrew'),

]