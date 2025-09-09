from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.record_index, name='record-index'),
    path('records/<int:record_id>/', views.record_detail, name="record-detail"),
]
