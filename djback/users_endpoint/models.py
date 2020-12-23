from django.db import models

class User(models.Model):
   name = models.CharField(max_length=150)
   followed = models.BooleanField()
   uniqueUrlName = models.CharField(max_length=255, blank=True)
   country = models.CharField(max_length=150, blank=True)
   city = models.CharField(max_length=150, blank=True)
   status = models.CharField(max_length=255, blank=True)
   def __str__(self):
       return r'{self.name}'

class Photo(models.Model):
   small = models.ImageField(upload_to='small_avatars', null=True, blank=True)
   large = models.ImageField(upload_to='large_avatars', null=True, blank=True)
   user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='photos', blank=True)
