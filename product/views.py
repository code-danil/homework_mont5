from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Products, Review
from .serializers import CategorySerializer, ProductsSerializer, ReviewSerializer


class CategoryListView(APIView):
    def get(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class CategoryDetailView(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id):
        category = get_object_or_404(Category, id=id)
        category.delete()
        return Response({'message': 'Удалено!'})


class ProductsListView(APIView):
    def get(self, request):
        serializer = ProductsSerializer(Products.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductsDetailView(APIView):
    def get(self, request, id):
        product = get_object_or_404(Products, id=id)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Products, id=id)
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        product = get_object_or_404(Products, id=id)
        product.delete()
        return Response({'message': 'Удалено!'})


class ReviewListView(APIView):
    def get(self, request):
        serializer = ReviewSerializer(Review.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class ReviewDetailView(APIView):
    def get(self, request, id):
        review = get_object_or_404(Review, id=id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, id):
        review = get_object_or_404(Review, id=id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        review = get_object_or_404(Review, id=id)
        review.delete()
        return Response({'message': 'Удалено!'})
    
class ProductReviewsView(APIView):
    def get(self, request):
        serializer = ProductsSerializer(Products.objects.all(), many=True)
        return Response(serializer.data)