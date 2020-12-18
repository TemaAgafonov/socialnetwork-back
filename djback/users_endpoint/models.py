from django.db import models

class User(models.Model):
   name = models.CharField(max_length=150)
   followed = models.BooleanField()
   photo = models.URLField()
   country = models.CharField(max_length=150)
   city = models.CharField(max_length=150)
   #datereg = models.DateTimeField(auto_now_add = True)

   def __str__(self):
       return r'{self.name}'