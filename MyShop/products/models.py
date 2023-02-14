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
    brand = models.CharField(max_length = 100, null = True)
    is_stock = models.BooleanField(default=True)
    product_description = models.TextField(null = True)

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    
class productImage(BaseModel):
    products = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to = "product")

    def __str__(self) -> str:
        return self.products.product_name


class variationManager(models.Manager):
    def sizes(self):
        return super(variationManager, self).filter(variation = 'size')

    def colors(self):
        return super(variationManager, self).filter(variation = 'color')
    

VARIATION_TYPE =  (
    ('size', 'size'),
    ('color', 'color')
)

class variationValue(BaseModel):
    variation = models.CharField(max_length=50, choices=VARIATION_TYPE)
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()

    objects = variationManager()
    def __str__(self):
        return self.name

    