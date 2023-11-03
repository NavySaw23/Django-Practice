from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)                    #the max_length is mandatory for CharField
    description = models.TextField(blank = True, null = True)   #if blank is false, blank values will not be allowed i.e. mandatory field
    price = models.TextField(default='100')
    checkbox = models.BooleanField(null=False)                  #if null is true it will become a trinary instead of boolean with Yes, No and Unknown state
    
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types  <-complete list
