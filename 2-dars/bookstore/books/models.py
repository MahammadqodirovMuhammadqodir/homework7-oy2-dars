from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserSetting(models.Model):
    country = models.CharField(max_length=100)
    lang = models.CharField(max_length=10)
