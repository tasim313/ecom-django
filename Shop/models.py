from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title} --- {self.price} -- {self.discount_price} ---{self.category}'


class Order(models.Model):
    items = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    total = models.CharField(max_length=200)