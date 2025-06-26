from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import (
    HomeView, ContactsView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView, UnpublishProductView, CategoryProductListView
)

app_name = NewappConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', UnpublishProductView.as_view(), name='unpublish_product'),
    path('category/<int:category_id>/', CategoryProductListView.as_view(), name='products_by_category'),
]
