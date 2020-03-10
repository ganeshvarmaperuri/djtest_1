from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmpModelView),
    path('thanks', views.thanks, name ='thanks')
]