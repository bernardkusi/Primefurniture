from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class items(models.Model):
    itemname=models.CharField(max_length=50)
    itemimage=models.CharField(max_length=50)
    itemprice=models.IntegerField()
    itemdescription=models.TextField(max_length=225)
    itemrating=models.IntegerField(default=5)
    image=models.ImageField(upload_to='static/images/',null=True)

    def __str__(self):
        return self.itemname


class purchase(models.Model):
    itemid=models.ForeignKey(items,on_delete=models.CASCADE)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)


class message(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField(max_length=225)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
