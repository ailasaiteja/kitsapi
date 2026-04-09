from django.urls import path
from .views import create_order, home, get_kits, get_payments

urlpatterns = [
    path('', home, name='home'),
    # path('kits/', home),
    path('api/kits/', get_kits,),
    path('create-order/', create_order),
    path('payments/<int:order_id>/', get_payments),
    path('kits/', get_kits,),
]