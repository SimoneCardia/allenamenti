from django.db import models

# Create your models here.
from django.db.models import CharField, IntegerField


class Workout (models.Model):
    name = CharField (max_length=200)
    num_repetition = IntegerField (default=1)

    def __str__(self):
        return self.name
