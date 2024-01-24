from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_wishlist, name='wishlist_add'),
]