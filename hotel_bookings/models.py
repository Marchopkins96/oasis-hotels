from django.db import models
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Extras(models.Model):
    """
    Add a new Extra as Admin in admin panel
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
