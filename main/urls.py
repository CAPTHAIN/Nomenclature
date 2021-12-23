from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *


urlpatterns = [
    path('', cache_page(60)(ShowCategoryView.as_view()), name='home'),
    path('<int:cat_pk>', cache_page(None)(ShowProductView.as_view()), name='products'),
]