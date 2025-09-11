from django import forms
from .models import Track, Record


class RecordForm(forms.ModelForm):
  class Meta:
    model = Record
    fields = ['title', 'artist', 'release_date']
    widgets = {'release_date': forms.DateInput(
        format=('%Y-%m-%d'), attrs={
            'placeholder': 'Select a date', 'type': 'date'
        }
    ),
    }


class TrackForm(forms.ModelForm):
  class Meta:
    model = Track
    fields = ['track_no', 'title', 'duration']
