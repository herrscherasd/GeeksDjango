from django.urls import path
from django.views import generic

from apps.academy import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="main_page"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),




]