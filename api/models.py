import uuid

from django.db import models


# Create your models here.

class Books(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=400)
