from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.name
