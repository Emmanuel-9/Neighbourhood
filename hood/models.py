from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    fire_dept = models.CharField(max_length=100, null=True)
    health_eme = models.CharField(max_length=100, null=True)
    police_cont = models.CharField(max_length=100, null=True)
    occ_count = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

<<<<<<< HEAD
    def save_neighbourhood(self):
        self.save()

    def del_neighbourhood(self):
        self.delete()        
=======
    def get_absolute_url(self):
        return reverse('welcome') 

    @classmethod
    def get_all_neighbourhoods(cls):
        return cls.objects.all()
    
>>>>>>> 15b27912935d5a569e31d841086d970048fee0e0

class Business(models.Model):
    
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    desc = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'

<<<<<<< HEAD
    def save_business(self):
        self.save()

    def del_business(self):
        self.delete()        
=======
    def get_absolute_url(self):
        return reverse('welcome') 

    @classmethod
    def get_all_businesses(cls):
        return cls.objects.all()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pics', default='default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('welcome') 

    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by('-date_posted')
>>>>>>> 15b27912935d5a569e31d841086d970048fee0e0
