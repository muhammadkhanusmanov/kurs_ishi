from django.urls import path
from ..views import LoginView, AdminView,GetData,CategoryView,Getimg,ProductView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('add/category/', AdminView.as_view()),
    path('add/product/', AdminView.as_view()),
    path('get/category/<str:id>', GetData.as_view()),
    path('get/product/<str:id>',Getimg.as_view()),
    path('allcategory/',CategoryView.as_view()),
    path('allproduct/',ProductView.as_view()),
]