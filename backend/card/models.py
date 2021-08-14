from django.db import models

class Card(models.Model):
    new = models.BooleanField(default=False)
    description = models.CharField(max_length=70)

