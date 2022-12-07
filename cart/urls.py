from django.urls import path

from cart import views

urlpatterns = [
    path('cartdetails/', views.Cartdetails, name='cartdetails'),
    path('add/<int:product_id>/', views.Add_items, name='add'),
    path('delete/<int:product_id>/', views.Delete_items, name='delete'),
    path('remove/<int:product_id>/', views.Remove, name='remove'),
    path('place-order', views.placeorder, name='place-order')
]