from django.db import models
import datetime


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254, default='Cardigan')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    teacher = models.CharField(max_length=254)
    date = models.DateField(default=datetime.date.today)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name