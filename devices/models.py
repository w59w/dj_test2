from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    image = models.ImageField(upload_to='devices/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='devices')
    features = models.ManyToManyField(Feature, related_name='devices')

    def __str__(self):
        return self.name
