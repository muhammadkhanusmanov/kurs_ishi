from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=75)
    img = models.ImageField(upload_to='category')

    def __str__(self) -> str:
        return self.name

class Mahsulot(models.Model):
    name = models.CharField(max_length=75)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.CharField(max_length=45)
    description = models.TextField()
    img = models.ImageField(upload_to='mahsulot')

    def __str__(self) -> str:
        return self.name