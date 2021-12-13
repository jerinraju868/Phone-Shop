from django.urls import path
from jshop_app import views

urlpatterns = [
    path('', views.Shop, name='shop'),
    path('login/', views.login, name='login'),
    path('about/', views.About, name='about'),
    path('signup/', views.Signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.Search, name='search'),
    path('<slug:c_slug>/', views.shop,name='prod_cat'),
    path('<slug:c_slug>/<slug:p_slug>/', views.Productdetails, name='productdetails'),


]
