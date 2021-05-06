from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from accounts.forms import SignUpForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Profile
from .decorators import allowed_users
# Create your views here.
