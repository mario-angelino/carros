from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=255, blank=False,
                             null=False)  # modelo do carro
    brand = models.CharField(max_length=255, blank=False,
                             null=False)  # marca do carro
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
