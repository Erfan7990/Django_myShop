from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.


  

class BillingAddress(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    country = models.CharField(max_length= 100)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length= 100)
    zipcode = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=100)


    def __str__(self):
        return self.user.username
    
    


