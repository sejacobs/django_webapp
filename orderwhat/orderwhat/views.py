from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class SplashView(TemplateView):
	template_name = 'index.html'
