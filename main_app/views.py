from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Record, Track
from .forms import TrackForm, RecordForm

# Create your views here.


class RecordCreate(CreateView):
  model = Record
  form_class = RecordForm


class RecordUpdate(UpdateView):
  model = Record
  fields = "__all__"


class RecordDelete(DeleteView):
  model = Record
  success_url = "/records/"


def home(request):
  return render(request, "home.html")


def about(request):
  return render(request, "about.html")


def record_index(request):
  records = Record.objects.all()
  return render(request, "records/index.html", {"records": records})


def record_detail(request, record_id):
  record = Record.objects.get(id=record_id)
  track_form = TrackForm()
  return render(request, "records/detail.html", {"record": record, "track_form": track_form})


def add_track(request, record_id):
  form = TrackForm(request.POST)
  if form.is_valid():
    new_track = form.save(commit=False)
    new_track.record_id = record_id
    new_track.save()
  return redirect("record-detail", record_id=record_id)


def update_track(request, record_id, track_id):
  track = get_object_or_404(Track, id=track_id)
  form = TrackForm(request.POST)
  if form.is_valid():
    updated_track = form.save(commit=False)
    updated_track.save()
  return redirect("record-detail", record_id=record_id)
