from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Record
from .forms import TrackForm

# Create your views here.


class RecordCreate(CreateView):
  model = Record
  fields = "__all__"


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
