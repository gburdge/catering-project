from django.shortcuts import render
from rest_framework import generics
from serializers import *
# Create your views here.


class CompanyList(generics.ListAPIView):
    model = Company
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class MenuList(generics.ListAPIView):
    model = Menu
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class FoodItem(generics.ListAPIView):
    model = FoodItem
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()


class CuisineList(generics.ListAPIView):
    model = Cuisine
    serializer_class = CuisineSerializer
    queryset = Cuisine.objects.all()