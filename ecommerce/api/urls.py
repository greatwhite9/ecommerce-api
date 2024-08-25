from django.urls import path
from .views import SignUpView, SignInView, AddProductView, UpdateProductView, DeleteProductView, ListProductsView, AddToCartView, UpdateCartView, DeleteFromCartView, GetCartView, PlaceOrderView, ListOrdersView, CustomerOrdersView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="EMS API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@ems.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('addproduct/', AddProductView.as_view(), name='addproduct'),
    path('updateproduct/<int:id>/', UpdateProductView.as_view(), name='updateproduct'),
    path('deleteproduct/<int:id>/', DeleteProductView.as_view(), name='deleteproduct'),
    path('products/', ListProductsView.as_view(), name='products'),
    path('cart/add/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/update/<int:id>/', UpdateCartView.as_view(), name='update_cart'),
    path('cart/delete/<int:id>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('cart/', GetCartView.as_view(), name='get_cart'),
    path('placeorder/', PlaceOrderView.as_view(), name='place_order'),
    path('getallorders/', ListOrdersView.as_view(), name='get_all_orders'),
    path('orders/customer/', CustomerOrdersView.as_view(), name='customer_orders'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
