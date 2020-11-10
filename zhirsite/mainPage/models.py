from django.db import models

class Measurements(models.Model):
    class Meta:
        db_table = "measurements"

    weight = models.IntegerField()
    data = models.DateField()

    class Meta:
        ordering = ["data"]

    def __str__(self):
        return f"{self.data}: {self.weight}"

    measure = models.Manager()