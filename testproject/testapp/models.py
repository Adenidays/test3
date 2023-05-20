
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price} - {self.categories}"

class Review(models.Model):
    product = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.product} - {self.author} - {self.text} - {self.rating}"
