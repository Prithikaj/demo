from django.db import models

class Contactt(models.Model):

    name = models.CharField(max_length=200)
    phone = models.IntegerField()

