from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import HomeView, ContactsView, ProductDetailView

app_name = NewappConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]
