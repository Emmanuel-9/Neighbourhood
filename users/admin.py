from django.contrib import admin

# Register your models here.
from .models import UserProfile, Neighbourhood, Business

admin.site.register(UserProfile)
admin.site.register(Neighbourhood)
admin.site.register(Business)
