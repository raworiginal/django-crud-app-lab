from django.db import models

# Create your models here.


class Record(models.Model):
  title = models.CharField()
  artist = models.CharField()
  release_date = models.DateField()


def __str__(self):
  return self.title
