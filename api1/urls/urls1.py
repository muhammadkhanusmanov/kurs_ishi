from django.urls import path
from ..views import LoginView, AdminView,GetData,CategoryView,Getimg,ProductView,GetProduct,DeleteView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('add/category/', AdminView.as_view()),
    path('add/product/', AdminView.as_view()),
    path('get/category/<str:id>', GetData.as_view()),
    path('get/product/<str:id>',Getimg.as_view()),
    path('allcategory/',CategoryView.as_view()),
    path('allproducts/',GetProduct.as_view()),
    path('products/bycategory/<str:id>',ProductView.as_view()),
    path('delete/product/<str:id>',DeleteView.as_view())
]   