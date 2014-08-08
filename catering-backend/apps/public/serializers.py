from models import *
from rest_framework import serializers


class CatererSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caterer


class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order


class FoodOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodOrder


class NestedCatererSerializer(serializers.ModelSerializer):
    food_item = FoodItemSerializer()

    class Meta:
        model = Caterer