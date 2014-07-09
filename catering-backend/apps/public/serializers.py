from models import *
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
