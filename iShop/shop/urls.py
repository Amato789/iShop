from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.main, name='index'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
]
