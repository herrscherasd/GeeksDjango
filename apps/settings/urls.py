from django.urls import path
from .views import index,contact, UserFeedbackView

urlpatterns = [
    path('', index, name="index"),
    path('contact', contact, name="contact"),
    path('follow/', UserFeedbackView.as_view(), name='order')
]