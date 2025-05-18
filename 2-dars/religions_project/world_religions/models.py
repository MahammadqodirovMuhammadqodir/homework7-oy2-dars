from django.db import models

class Religion(models.Model):
    name = models.CharField(max_length=100)
    founder = models.CharField(max_length=100, blank=True, null=True)
    origin_date = models.CharField(max_length=50, blank=True, null=True)
    origin_place = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
