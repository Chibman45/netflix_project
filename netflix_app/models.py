from django.db import models

# Create your models here.from django.db import models

class NetflixData(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=100, null=True, blank=True)
    release_year = models.IntegerField()
    duration = models.CharField(max_length=50, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
