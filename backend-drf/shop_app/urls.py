from django.urls import path
# from .views import * its not a good practice to import * | it imports everything
from . import views # good practice mainly used in larger projects

urlpatterns = [
    path('products/', views.products, name='products'),
]
