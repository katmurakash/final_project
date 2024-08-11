from rest_framework.serializers import ModelSerializer
from ..models import Product, Image


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'