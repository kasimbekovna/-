from django.urls import path
from .import views

urlpatterns = [
    path("", views.techno_view, name="techno_view"),
    path("", views.techno_detail_view, name="techno_detail_view"),
]