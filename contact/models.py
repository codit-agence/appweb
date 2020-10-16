from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()
    message= models.TextField()
    title=models.CharField(max_length=256, default='contact web')
    tel=models.IntegerField(max_length=10)
    ville=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactInscription(models.Model):
    name    =models.CharField(max_length=100)
    email   = models.EmailField()
    tel     =models.IntegerField(max_length=10)
    ville   =models.CharField(max_length=100)
    message = models.CharField(max_length=256)

    def __str__(self):
        return self.name