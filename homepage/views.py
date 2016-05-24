from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import Landing_Page


class Landing(TemplateView):
	template_name = "landing.html"

	def get_context_data(self, **kwargs):
		context = super(Landing, self).get_context_data(**kwargs)
		return context

	def landing():
		landing = Landing_Page.objects.all()
		return landing


class Contact(TemplateView):
	template_name = "photo.html"

	def get_context_data(self, **kwargs):
		context = super(Contact, self).get_context_data(**kwargs)
		return context
