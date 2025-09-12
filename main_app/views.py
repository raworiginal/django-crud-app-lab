from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Record, Track
from .forms import TrackForm, RecordForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class RecordCreate(LoginRequiredMixin, CreateView):
  model = Record
  form_class = RecordForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class RecordUpdate(LoginRequiredMixin, UpdateView):
  model = Record
  fields = "__all__"


class RecordDelete(LoginRequiredMixin, DeleteView):
  model = Record
  success_url = "/records/"


class Home(LoginView):
  template_name = 'home.html'


def about(request):
  return render(request, "about.html")


@login_required
def record_index(request):
  records = Record.objects.filter(user=request.user)
  return render(request, "records/index.html", {"records": records})


@login_required
def record_detail(request, record_id):
  record = Record.objects.get(id=record_id)
  track_form = TrackForm()
  return render(request, "records/detail.html", {"record": record, "track_form": track_form})


@login_required
def add_track(request, record_id):
  form = TrackForm(request.POST)
  if form.is_valid():
    new_track = form.save(commit=False)
    new_track.record_id = record_id
    new_track.save()
  return redirect("record-detail", record_id=record_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('record-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as:
  # return render(
  #     request,
  #     'signup.html',
  #     {'form': form, 'error_message': error_message}
  # )
