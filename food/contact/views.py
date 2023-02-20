from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import ContactForm
# Create your views here.


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/food-contact.html', context={"form": form})


class CreateFeedback(CreateView):
    template_name = 'contact/food-contact.html'
    form_class = ContactForm
    success_url = "/"
