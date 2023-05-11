from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from apps.academy.models import Academy, Courses, SettingsModel,AboutModel,SlideModel,CourseModel
from apps.academy.forms import CourseFeedBackForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    queryset = Academy.objects.all()
    context_object_name = "courses"

class ContactsView(generic.TemplateView):
    template_name = 'contact.html'

class UserFeedbackView(generic.FormView):
    form_class = CourseFeedBackForm
    success_url = reverse_lazy('index')
    template_name = 'order.html'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    
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