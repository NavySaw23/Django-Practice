from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField(default='100')
    
    # Other possible options -
    # id = models.IntegerField()
    # link = models.URLField()
    # upload = models.FileField()
