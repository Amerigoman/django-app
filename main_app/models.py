from django.db import models


class Location (models.Model):
    name = models.CharField(max_length=50)
    predators = models.CharField(max_length=100)
    num_restaurants = models.IntegerField()
    img = models.ImageField(upload_to='location_images', default='location_images/default.png')

    def __str__(self):
        return self.name
