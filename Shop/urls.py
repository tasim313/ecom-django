from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('details/<id>', details, name='details'),
    path('checkout/', checkout, name='checkout'),
]