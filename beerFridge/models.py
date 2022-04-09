from django.db import models

class Beer(models.Model):
    type=models.CharField(max_length=200)
    caloriesPerLiter=models.PositiveIntegerField()
    color=models.CharField(max_length=200)
    alcoholPercentage=models.PositiveIntegerField()

