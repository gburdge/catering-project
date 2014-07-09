from django.db import models

# Create your models here, i.e.: #photo, ingredients, description, instructions, prep time, total time, tags, favorited


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField(max_length=10)
    cuisine = models.ForeignKey("Cuisine")
    menu = models.OneToOneField("Menu", null=True, blank=True)
    image = models.CharField(max_length=500, default="image")

    def __unicode__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    type = models.TextField()
    price = models.IntegerField(max_length=9)
    image = models.CharField(max_length=500, default="no image")

    def __unicode__(self):
        return self.name


class Cuisine(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name