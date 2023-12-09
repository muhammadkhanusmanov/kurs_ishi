from rest_framework.serializers import ModelSerializer

from .models import Category,Mahsulot

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MahsulotSerializer(ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'