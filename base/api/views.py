from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product, Image
from .serializers import ProductSerializer, ImageSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        "GET /api",
        "GET /api/products",
        "GET /api/product/:id",
        "GET /api/images",
        "GET /api/image/:id"
    ]
    return Response(routes)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_images(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_image(request, id):
    image = Image.objects.get(id=id)
    serializer = ImageSerializer(image, many=False)
    return Response(serializer.data)
