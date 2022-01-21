from django.views import generic
from django.contrib.auth import forms
from django.urls import reverse_lazy
from .forms import profile

class register(generic.CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class profile(generic.UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')
    form_class = profile

    def get_object(self):
        return self.request.user
