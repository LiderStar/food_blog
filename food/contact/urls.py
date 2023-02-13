from django.urls import path

from blog import views
from contact.views import ContactView, CreateFeedback


urlpatterns = [
    path('contact/', ContactView.as_view(), name="contact"),
    path('feedback/', CreateFeedback.as_view(), name="feedback"),

]