from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def Home(request):
	return redirect(reverse('empresas:api'))