from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("records/", views.record_index, name="record-index"),
    path("records/<int:record_id>/", views.record_detail, name="record-detail"),
    path("records/create", views.RecordCreate.as_view(), name="record-create"),
    path("records/<int:pk>/update/",
         views.RecordUpdate.as_view(), name="record-update"),
    path("records/<int:pk>/delete/",
         views.RecordDelete.as_view(), name="record-delete"),
    path("records/<int:record_id>/add-track/",
         views.add_track, name="add-track")
]
