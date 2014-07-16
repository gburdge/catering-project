from models import *
from rest_framework import serializers


class CatererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caterer

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem


class MenuSerializer(serializers.ModelSerializer):

    FoodItem = FoodItemSerializer()

    class Meta:
        model = Menu


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order


class Food_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOrder

class NestedCaterer(serializers.ModelSerializer):

    menu = MenuSerializer()

    class Meta:
        model = Caterer
