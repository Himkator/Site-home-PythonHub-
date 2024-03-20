
import decimal
from dis import disco
from email.policy import default
from enum import unique
from pyexpat import model
from tabnanny import verbose
from turtle import mode
from unicodedata import category
from django.db import models

# Create your models here.

class Categories(models.Model):
    name=models.CharField(max_length=150, unique=True, verbose_name="Name")
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='category'
        verbose_name='Category'
        verbose_name_plural='Categories'
        


class Products(models.Model):
    name=models.CharField(max_length=150,  verbose_name="Name")
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description=models.TextField(blank=True, null=True, verbose_name="Description")
    image=models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Picture')
    price=models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='Price')
    discount=models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='Discount in procent')
    quantity=models.PositiveIntegerField(default=0, verbose_name='Quantity')
    category=models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Category')
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='product'
        verbose_name='Product'
        verbose_name_plural='Products'
        ordering=('id',)
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price-self.price*self.discount/100, 2)
        return self.price
