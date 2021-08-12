from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField






# Create your models here.
class user(AbstractUser):
    is_admin= models.BooleanField(default=False)
    is_club= models.BooleanField(default=False)
    

    



class eventc(models.Model):
    user=models.ForeignKey(user,on_delete=CASCADE)
    title =models.CharField( max_length=100)
    date = models.DateField(("date"), auto_now=False, auto_now_add=False)
    add_date=models.DateTimeField(auto_now=True)
    description =models.TextField()
    place =models.CharField(max_length=50)
    poster =models.ImageField( upload_to='pics')
    choice = (
            ('approved', 'approved'),
            ('pending...', 'pending...'),
            ('refused', 'refused'),
        )
    status = models.CharField(max_length=30, default='pending...', choices=choice)
    feedback=models.TextField(default='',blank=True)
    
class EventRegistration(models.Model):
    event = models.ForeignKey(eventc,on_delete=CASCADE)
    user = models.ForeignKey(user,on_delete=CASCADE)


class club(models.Model):
    chef=models.ForeignKey(user,on_delete=CASCADE)
    name=models.CharField(max_length=200)
    about=models.TextField()
    image=models.ImageField(upload_to='pics')

   



    

   

    
    
