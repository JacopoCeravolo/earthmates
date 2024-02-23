from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from . models import Startup

# Create your views here.
class CustomLogin(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
class CustomRegister(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('startup-create')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegister, self).form_valid(form)
    
def HomePage(request):
    return render(request, template_name="base/home.html")

class StartupDetail(LoginRequiredMixin, DetailView):
    model = Startup
    context_object_name = "startup"
    template_name = "base/startup.html"
    
class StartupCreate(LoginRequiredMixin, CreateView):
    model = Startup
    fields = [field.name for field in model._meta.fields if not (field.primary_key or field.name in ["user", "created_at"])]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StartupCreate, self).form_valid(form)
    
class StartupUpdate(LoginRequiredMixin, UpdateView):
    model = Startup
    fields = [field.name for field in model._meta.fields if not (field.primary_key or field.name in ["user", "created_at"])]
    print(fields)
    success_url = reverse_lazy('home')

class StartupDelete(LoginRequiredMixin, DeleteView):
    model = Startup
    context_object_name = "startup"
    success_url = reverse_lazy('home')