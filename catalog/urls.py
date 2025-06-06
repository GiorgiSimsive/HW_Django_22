from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import (
    HomeView, ContactsView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView
)

app_name = NewappConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),

    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:product_id>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
