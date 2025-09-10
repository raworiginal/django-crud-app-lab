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


class Track(models.Model):
  track_no = models.IntegerField()
  title = models.CharField()
  duration = models.DurationField()

  record = models.ForeignKey(Record, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
