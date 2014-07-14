from models import *
from rest_framework import serializers


class CatererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caterer


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order


class Food_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOrder
