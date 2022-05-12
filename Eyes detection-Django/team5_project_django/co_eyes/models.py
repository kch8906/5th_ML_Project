from django.db import models


# Create your models here.

class Predictlabel(models.Model):
    label = models.CharField(max_length=10)
    total_sleep_count = models.IntegerField()
    register_date = models.DateTimeField()

    def __str__(self):
        return self.label, self.total_sleep_count, self.register_date


class Temp(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    co2 = models.IntegerField(null=True)
    register_date = models.DateTimeField()
