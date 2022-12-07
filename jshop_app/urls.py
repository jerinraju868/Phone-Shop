from django.urls import path
from jshop_app import views

urlpatterns = [
    path('', views.Shop, name='shop'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.Signup, name='signup'),
    path('about/', views.About, name='about'),
    path('search/', views.Search, name='search'),
    path('product/<slug:c_slug>/', views.shop,name='prod_cat'),
    path('product-detail/<slug:c_slug>/<slug:p_slug>/', views.Productdetails, name='productdetails'),


]
