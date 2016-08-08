from django.db import models


# Create your models here.
class PublicModel(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        abstract = True
