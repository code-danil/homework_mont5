from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Products, Review
from .serializers import CategorySerializer, ProductsSerializer, ReviewSerializer


@api_view(['GET'])
def category_list_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detail_view(request, id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['GET'])
def product_list_view(request):
    Product = Products.objects.all()
    serializer = ProductsSerializer(Product, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def product_detail_view(request, id):
    Product = Products.objects.get(id=id)
    serializer = ProductsSerializer(Product)
    return Response(serializer.data)



@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['GET'])
def product_reviews_list(request):
    serializer = ProductsSerializer(Products.objects.all(), many=True)
    return Response(serializer.data)
