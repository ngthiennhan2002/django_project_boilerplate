from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout', checkout_page, name='checkout'),
    path('checkout/', checkout_page, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product')
]