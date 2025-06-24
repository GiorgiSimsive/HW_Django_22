from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import ProductForm
from .models import Product
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views import View
from django.core.exceptions import PermissionDenied


class UnpublishProductView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.publication_status = 'draft'
        product.save()
        return redirect('catalog:product_detail', pk=product.pk)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user
        if product.owner == user or user.has_perm('catalog.delete_product'):
            return product
        raise PermissionDenied("Нет прав для удаления этого продукта")


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'
