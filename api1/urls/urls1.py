from django.urls import path
from ..views import LoginView, AdminView,GetData,CategoryView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('add/category/', AdminView.as_view()),
    path('get/category/<str:id>', GetData.as_view()),
    path('allcategory/',CategoryView.as_view())
]