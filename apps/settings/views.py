from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .forms import CourseFeedBackForm
from .models import Setting,About,Slide,Course
# Create your views here.
def index(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")
    slide = Slide.objects.latest("id")
    course = Course.objects.all()
    context = {
        'setting': setting,
        'about':about,
        'slide':slide,
        'course':course,
    }
    return render(request, "index.html", context)

def contact(request):
    setting = Setting.objects.latest("id")
    context = {
        'setting': setting
    }
    return render(request, "contact.html", context)

class UserFeedbackView(generic.FormView):
    form_class = CourseFeedBackForm
    success_url = reverse_lazy('index')
    template_name = 'order.html'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)