from django.shortcuts import redirect
from django.views import generic

from apps.academy.models import Academy, Courses
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
    success_url = "follow"
    template_name = 'order.html'

    def saveorder(self, request):
        if request.method == 'POST':
            form = CourseFeedBackForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('index')
                except:
                    form.add_error(None, "Ошибка при отправлении записи")