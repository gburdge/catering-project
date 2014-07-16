from django.shortcuts import render
from rest_framework import generics
from serializers import *
# Create your views here.


class CatererList(generics.ListAPIView):
    model = Caterer
    serializer_class = NestedCaterer
    queryset = Caterer.objects.all()


class CatererDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Caterer
    serializer_class = NestedCaterer
    queryset = Caterer.objects.all()



class FoodItem(generics.ListAPIView):
    model = FoodItem
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()



class OrderList(generics.ListAPIView):
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()



class FoodOrderList(generics.ListAPIView):
    model = FoodOrder
    serializer_class = Food_orderSerializer
    queryset = FoodOrder.objects.all()


