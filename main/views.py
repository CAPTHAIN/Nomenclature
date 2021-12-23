from django.views.generic import ListView

from .models import *


class ShowCategoryView(ListView):
    model = Category
    template_name = 'main/category.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShowProductView(ListView):
    paginate_by = 50
    model = Product
    template_name = 'main/product.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['cat_pk'])
        return context

    def get_queryset(self):
        return Product.objects.filter(category=Category.objects.get(pk=self.kwargs['cat_pk']))
