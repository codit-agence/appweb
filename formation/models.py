from django.db import models


class Offres(models.Model):
    name=models.CharField(max_length=200)
    prix=models.IntegerField()
    date_come= models.DateField()
    date_end= models.DateField()
    attestation=models.BooleanField(default=True)
    pratique=models.BooleanField(default=True)
    projet=models.BooleanField(default=True)
    jours=models.IntegerField()

    def __str__(self):
        return self.name

