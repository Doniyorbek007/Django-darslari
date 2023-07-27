from django.views.generic import ListView
from .models import Post, Contact, About

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'barcha_postlar'

class AboutPageView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'

class ContactPageView(ListView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = 'contact'