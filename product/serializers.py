from rest_framework import serializers
from .models import Category, Products, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, source='review_set')
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = 'id title description category reviews rating'.split()

    def get_rating(self, obj):
        stars_list = [review.stars for review in obj.review_set.all()]
        if not stars_list:
            return 0
        return sum(stars_list) / len(stars_list)



class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = 'id name products_count'.split()


    def get_products_count(self, obj):
        return obj.products_set.count()

