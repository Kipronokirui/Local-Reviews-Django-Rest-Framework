from django.contrib.auth.models import User, Group
from rest_framework import serializers
from review.models import Review, Business, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']

class ReviewReadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Review
		depth = 1
		fields = '__all__'

class ReviewWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Review
		fields = '__all__'

class BusinessReadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Business
		depth = 1
		fields = [
			'url',
			'name',
			'slug',
			'description',
			'price_range',
			'street_address',
			'city',
			'region',
			'postal_code',
			'country',
			'website',
			'phone',
			'hours',
			'reviews',
		]

class BusinessWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Business
		fields = [
			'url',
			'name',
			'slug',
			'description',
			'price_range',
			'street_address',
			'city',
			'region',
			'postal_code',
			'country',
			'website',
			'phone',
			'hours',
			'reviews',
		]

class CategoryReadSerializer(serializers.HyperlinkedModelSerializer):
	business = BusinessReadSerializer(many=True)
	class Meta:
		model = Category
		depth = 1
		fields = [
			'url',
			'name',
			'slug',
			'ordinal',
			'business'
		]

class CategoryWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = [
			'url',
			'name',
			'slug',
			'ordinal',
			'business'
		]