from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Record

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
  return render(request, "records/detail.html", {"record": record})
