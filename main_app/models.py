from django.db import models
from django.urls import reverse

# Create your models here.


class Record(models.Model):
  title = models.CharField()
  artist = models.CharField()
  release_date = models.DateField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("record-detail", kwargs={"record_id": self.id})
