from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from apps.academy.models import Academy

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    queryset = Academy.objects.all()
    context_object_name = "courses"

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ContactsView(generic.TemplateView):
    template_name = 'contacts.html'

# class CourseDetailView(generic.DetailView):
    