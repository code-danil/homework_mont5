from rest_framework import serializers
from .models import Category, Products, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_stars(self, value):
            if value < 1 or value > 5:
                raise serializers.ValidationError('Stars must be between 1 and 5')
            return value
        
    def validate_text(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Текст слишком короткий')
        return value
    
    
class ProductsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, source='review_set')
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews', 'rating']

    def get_rating(self, obj):
        stars_list = [review.stars for review in obj.review_set.all()]
        if not stars_list:
            return 0
        return sum(stars_list) / len(stars_list)
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Цена должен быть больше нуля')
        return value
    
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError('Название слишком короткое')
        return value.strip()


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()


    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']


    def get_products_count(self, obj):
        return obj.products_set.count()
    
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError('Название слишком короткое')
        return value.strip()