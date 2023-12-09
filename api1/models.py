from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=75)
    img = models.ImageField(upload_to='category')

    def __str__(self) -> str:
        return self.name

