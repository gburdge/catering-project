from django.db import models

# Create your models here, i.e.: #photo, ingredients, description, instructions, prep time, total time, tags, favorited


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    phone = models.IntegerField(max_length=10)
<<<<<<< HEAD
    menu = models.ForeignKey("Menu", null=True, blank=True)
=======
    menu = models.ForeignKey("Menu", null=False, blank=False)
>>>>>>> 01c29ec234fce5f061962bf55586b2b50a19f0cc


    def __unicode__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50)
<<<<<<< HEAD
    FoodItem = models.ForeignKey("FoodItem",null=True,blank=True)
=======
    FoodItem = models.ForeignKey("FoodItem", null=False, blank=False)
>>>>>>> 01c29ec234fce5f061962bf55586b2b50a19f0cc

    def __unicode__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
<<<<<<< HEAD
    price = models.DecimalField(max_digits=9,decimal_places=2)
=======
    price = models.DecimalField(max_digits=7, decimal_places=2)
>>>>>>> 01c29ec234fce5f061962bf55586b2b50a19f0cc
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