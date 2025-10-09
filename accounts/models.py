from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False)

    def __str__(self):
        return self.name
