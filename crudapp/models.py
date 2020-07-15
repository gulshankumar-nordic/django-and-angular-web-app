from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, default=None, unique=True, blank=False)


