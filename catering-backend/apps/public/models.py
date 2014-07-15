from django.db import models

# Create your models here, i.e.: #photo, ingredients, description, instructions, prep time, total time, tags, favorited


class Caterer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=60, null=True, blank=True)
    phone = models.IntegerField(max_length=10, null=True, blank=True)
    menu = models.ForeignKey("Menu", null=True, blank=True)

    def __unicode__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50)
    FoodItem = models.ForeignKey("FoodItem",null=True,blank=True)

    def __unicode__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=500, default="no image")

    def __unicode__(self):
        return self.name


class Order(models.Model):
    delivery_date = models.DateField(max_length=25)
    delivery_time = models.TimeField(max_length=10)
    order = models.TextField(max_length=100)

    def __unicode__(self):
        return self.name


class FoodOrder(models.Model):
    FoodItem = models.CharField(max_length=25)
    quantity = models.IntegerField(max_length=10)

    def __unicode__(self):
        return self.name