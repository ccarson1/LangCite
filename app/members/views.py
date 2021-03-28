from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import UserRegForm
import os
from django.contrib.auth.models import User


class UserRegistrationView(generic.CreateView):
	form_class = UserRegForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

	