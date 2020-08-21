from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    occ_count = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    def save_neighbourhood(self):
        self.save()

    def del_neighbourhood(self):
        self.delete()        

class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.name}'

    def save_business(self):
        self.save()

    def del_business(self):
        self.delete()        