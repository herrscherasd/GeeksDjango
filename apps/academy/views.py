from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from apps.academy.models import Academy
from apps.academy.forms import CourseFeedBackForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    queryset = Academy.objects.all()
    context_object_name = "courses"

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ContactsView(generic.TemplateView):
    template_name = 'contact.html'

class UserFeedbackView(generic.FormView):
    form_class = CourseFeedBackForm
    success_url = "index"
    template_name = 'contact.html'