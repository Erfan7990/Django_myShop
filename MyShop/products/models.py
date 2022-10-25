from distutils.command.upload import upload
from enum import unique
from unicodedata import name
from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to = "category")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name

class Product(BaseModel):
    product_name = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name="product_category")
    price = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

class product_details(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="product")
    brand = models.CharField(max_length = 100)
    product_description = models.TextField()
    
    def __str__(self):
        return self.product.product_name
    
class productImage(BaseModel):
    products = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to = "product")

    def __str__(self) -> str:
        return self.products.product_name
    

    